"""
Purpose: The following model will make prediction on log_error base on the user inputs.
Author: Jingwu Fang
Date: 03/09/2020
Contact Email: jingwufang94@outlook.com
"""

import pandas as pd
import numpy as np
import logging
import boto3
import joblib
import requests

import s3fs

logging.basicConfig(level=logging.INFO)
# Define one logger for current file
LOGGER = logging.getLogger(__name__)

def user_inputs():
    """this function will take user inputs for later calculation""" 
    LOGGER.info("---Taking user inputs...")
    bathroomcnt=input("Please enter the number of bathrooms: ")
    bedroomcnt=input("Please enter the number of bedrooms: ")
    taxamount=input("Please enter the taxamount of the house: ")
    yearbuilt=input("Please enter the year the house is built as 'yyyy': ")
    calculatedfinishedsquarefeet=input("Please enter the calculatedfinishedsquarefeet: ")
    transaction_yearmonth_i=input("Please enter the transaction_yearmonth as 'yyyymm': ")
    # creating lists based on user input
    user_inputs = np.array([[bathroomcnt, bedroomcnt, taxamount, yearbuilt, calculatedfinishedsquarefeet, transaction_yearmonth_i]])
    return user_inputs.astype(np.float64)

def initialize_model():
    """this function will load and initialize the model"""
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('stats404-project-jingwu')
    bucket.download_file('knn_zillow.joblib', 'knn_zillow.joblib')
    #load model
    knn_dict = joblib.load('knn_zillow.joblib')
    return knn_dict

knn_dict = initialize_model()


def model_output():
    # this function will initialize the model and output result

    log_error_pred = knn_dict.predict(user_inputs())
    LOGGER.info("---Initializing model...")
    LOGGER.info("---Output model result...")
    print("The log_error: " + str(log_error_pred))
    return log_error_pred

if __name__ == "__main__":
    model_output()
