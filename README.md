![S1](https://user-images.githubusercontent.com/74737545/109413024-5b311080-79d1-11eb-816e-45898d69786e.jpg)

# Banglore Housing Price Prediction
This is a Supervised Learning Problem where the Prediction of Housing Prices are done by understanding & evaluating the trends of price of the historical data.

# Introduction

Supervised Learning is the type of Machine Learning where a historical data are used to analyse future trends. The input data, when fed to model, is the defining aspect of the Machine Learning Model. The input data would be required to be fitted properly to the model, to make sure the model is able to utilize the input data to give output.

The Supervised Learning problems can further be devided into Classification & Regression. The Classification would assign the input data into specific categories. It would recognise the categorical entities, and would attempt to draw conclusions on how those entities are labled or defined. The Regression is useful to understand the relationship between dependent & independent variables, and is highly used to make projections of the data.

As the goal of our analysis is to predict the prices, the regression models are best suited for the problem statement. In order to achieve our goal, we would be required to understand the relationship & dependecny of the variables with respect to our output. It will help us to identify the independent & dependent variables, which would be further utilized to project the data.

# Understand the Problem Statement

Let’s go through the problem statement once as it is very crucial to understand the objective before working on the dataset. The problem statement is as follows:

The objective of this task is to predict the price of the house located in Bangalore. For the sake of simplicity, we can say that the house price will depend upon the area & locality. The dataset also includes rooms & area type which would further categorise the data.

Once, the model is ready, deploy the model using Amazon Web Services.

# Preprocessing and Cleaning


For an instance, if one is searching for a document in an office space, what is the probability of finding the document easily? Of course, if the files are documented in propely manner, it would be an easy task. The data cleaning exercise is quite similar. If the data is arranged in a structured format then it becomes easier to find the right information.

The preprocessing of the data is an essential step as it makes the raw data ready for mining, i.e., it becomes easier to extract information from the data and apply machine learning algorithms to it. If we skip this step then there is a higher chance that you are working with noisy and inconsistent data. The objective of this step is to clean noise those are less relevant to find variables which don’t carry much weightage in context to the price.

Let’s first read our data and load the necessary libraries.

# Deployment of Model

Once we have evaluated & selected the best model for our problem data set, it is now ready to be deployment. So, with the use of front end languages, we will deploy the server through Amazon Web Services.

Before deployment, it is advisable to extrapolate if the model is working for local host. We would be using PostMan to debug the webpage, and once it is ready, we would be deploying the same using nginx & Amazon EC2 Services.

# End Notes

In this article, we learned how to approach a Prediction analysis problem. We started with preprocessing and exploration of data. Then we extracted features from the cleaned data using various correlation. Finally, we were able to build a couple of models using both the feature sets to predict the prices.
