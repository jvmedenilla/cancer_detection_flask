# Cancer Detection using XGBoost, Flask

This project is mainly about implementing XGBoost and deploying it on the web using Flask.

## The Task: Cancer Classification
Given a csv file containing the measurements of cells to evaluate, the task is to classify 
each cell as benign or malignant.

## The Dataset: Cancer Data (Kaggle)
I got the dataset from Kaggle: https://www.kaggle.com/datasets/erdemtaha/cancer-data
This dataset contains 570 cancer cells and 30 features to determine 
whether the cancer cells are benign or malignant.

However, there are two many features. For a machine learning model to be robust and operate relatively fast,
the number of features should be minimized -- only selecting the most relevant features. So, I did some pre-processing work.
As can be seen in [cancer_detection.ipynb](https://github.com/jvmedenilla/cancer_detection_flask/blob/main/cancer_detection.ipynb).

I made a correlation matrix to see which features are highly correlated to the diagnosis feature/label.
![image](https://user-images.githubusercontent.com/98763090/236375506-19828723-09c8-4b90-914b-4fda81285c1e.png)

Then, I only selected the top 9 features. There's not reason for choosing 9, other than I wanted to minimize the
number of features without leaving out too many. Also, it would be really hard to test the model on Flask if
I have a thousand forms to fill (LOL).

## The Model: XHBoost

Gradient boosting is a powerful machine learning model that is regarded as one of the fastest and 
accurate model to use for regression and classification. Boosting is a method widely used in 
machine learning to minimize the errors during inference. For more info about boosting, see:
a) https://aws.amazon.com/what-is/boosting/
b) https://www.analyticsvidhya.com/blog/2021/09/gradient-boosting-algorithm-a-complete-guide-for-beginners/

I installed XGBoost from [XGBoost documentation](https://xgboost.readthedocs.io/en/stable/install.html).
![image](https://user-images.githubusercontent.com/98763090/236376841-41a06895-2c36-498a-8545-9e8df9190b7c.png)

