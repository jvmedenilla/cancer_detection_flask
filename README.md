# Cancer Detection using XGBoost, Flask

This project is mainly about implementing XGBoost and deploying it on the web using Flask.

## The Task: Cancer Classification
Given a csv file containing the measurements of cells to evaluate, the task is to classify 
each cell as benign or malignant.

## The Dataset: Cancer Data (Kaggle)
I got the dataset from Kaggle: https://www.kaggle.com/datasets/erdemtaha/cancer-data.
This dataset contains 570 cancer cells and 30 features to determine 
whether the cancer cells are benign or malignant.

However, there are too many features. For a machine learning model to be robust and operate relatively fast,
the number of features should be minimized -- only selecting the most relevant features. So, I did some pre-processing work.
As can be seen in [cancer_detection.ipynb](https://github.com/jvmedenilla/cancer_detection_flask/blob/main/cancer_detection.ipynb).

I made a correlation matrix to see which features are highly correlated to the diagnosis feature/label.
![image](https://user-images.githubusercontent.com/98763090/236375506-19828723-09c8-4b90-914b-4fda81285c1e.png)

Then, I only selected the top 9 features. There's not reason for choosing 9, other than I wanted to minimize the
number of features without leaving out too many. Also, it would be really hard to test the model on Flask if
I have a thousand forms to fill (LOL).

## The Model: XGBoost

Gradient boosting is a powerful machine learning model that is regarded as one of the fastest and 
accurate model to use for regression and classification. Boosting is a method widely used in 
machine learning to minimize the errors during inference. For more info about boosting, see:
a) https://aws.amazon.com/what-is/boosting/
b) https://www.analyticsvidhya.com/blog/2021/09/gradient-boosting-algorithm-a-complete-guide-for-beginners/

I installed XGBoost from [XGBoost documentation](https://xgboost.readthedocs.io/en/stable/install.html).
![image](https://user-images.githubusercontent.com/98763090/236376841-41a06895-2c36-498a-8545-9e8df9190b7c.png)

## The Deployment: Flask

Flask is a web framework in Python that is easy to use and very accessible. It is ideal for simple machine learning
projects due to its simple abstraction and general ease of use. For more info, visit [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/).

### Files:

My project directory looks like this:
![image](https://user-images.githubusercontent.com/98763090/236378264-48d80347-db78-4409-93e6-e7ca62121948.png)

* The Application folder: contains all the working files in Python and HTML
* Cancer_Data.csv: the downloaded dataset 
* config.py: the configuration items
* model.pkl: pickled model from running models.py (Run: "python models.py")
* requirements.txt: contains the packages needed in this project

## Running the model:
To run the model, simply run: 
![image](https://user-images.githubusercontent.com/98763090/236379334-31700018-34f5-4cdb-b73f-033afeabb768.png)

Then, this will show in the terminal: 
![image](https://user-images.githubusercontent.com/98763090/236379388-38ecaaaa-dc6d-4511-ab5b-03f65814fbdf.png)


The home page looks like this: 
![image](https://user-images.githubusercontent.com/98763090/236379458-d858115b-54da-401a-8224-36ba96fe3ca8.png)


### Output

To test the model, I fill up the forms as shown:
![image](https://user-images.githubusercontent.com/98763090/236379587-b5376744-098d-4262-8656-677ad554056c.png)

Then after clicking the button below it, I can finally see the result!
Ta-dah!
![image](https://user-images.githubusercontent.com/98763090/236379678-d9a101eb-f33f-48b2-9c14-1b13b8b7eaf6.png)

Alternatively, if the news was bad:
![image](https://user-images.githubusercontent.com/98763090/236379754-7e424788-5ea0-4a76-acfd-b2e256d7072a.png)

Thanks for making it to this point. Hope you liked my project :)


