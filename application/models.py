'''
This models file is used for defining the pre-processing of the data and the training
of the model I am using.
'''

from sklearn.metrics import accuracy_score, confusion_matrix  # i used these packages in the jupyter notebook
from sklearn.model_selection import train_test_split
import xgboost as xgb
import pickle
import pandas as pd

df = pd.read_csv('Cancer_Data.csv')
# encode diagnosis values into binary
df['diagnosis'].replace({'B': 0, 'M': 1}, inplace=True)

# here, df.corr() gives the correlation of each feature with all the other features
# I did this because I wanted to select features that are most relevant/related to
# the diagnosis
df_corr = df.corr()
relevant_features = df_corr['diagnosis'].sort_values(ascending=False)
features_list = list(relevant_features[1:10].keys()) # get top 9 highest correlated features to diagnosis
irrelevant_features = list(relevant_features[10:].keys())
# delete irrelevant features from the dataframe
for item in irrelevant_features:
  df.drop(item, inplace=True, axis=1)

# made a copy of the original dataframe, then I extracted
# the values of df['diagnosis'] and made it the target values
# for the training
df_data = df.copy(deep=True)
df_target = df['diagnosis']
df_data = df.drop(columns='diagnosis')

df_target.replace({1:True, 0:False}, inplace=True)
df_target

# by convention, X is data and Y is labels
X = df_data
Y = df_target
#split the dataset into 80% training data and 20% testing data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=7)

# used binary logistic XGBoost classifier with standard randome state of 42
xgb_model = xgb.XGBClassifier(objective='binary:logistic', random_state=42)
xgb_model.fit(X_train,y_train)

# saved model in pickle
pickle.dump(xgb_model, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))

