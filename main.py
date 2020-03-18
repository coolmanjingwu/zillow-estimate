"""
Project: Zillow housing project.
Purpose: The model will make prediction on log_error base on user inputs.
Author: Jingwu Fang
Date: 03/17/2020
Contact Email: jingwufang94@outlook.com
"""

import logging
import tempfile

import numpy as np
import boto3
import joblib

def initialize_model():
    """this function will load and initialize the model"""
    s3 = boto3.client('s3',
                      aws_access_key_id="AKIAJ7WVXAIXRCQKY4DA",
                      aws_secret_access_key="E9upXw25HkXoxmmrhniY1Cqr"
                                            "GhHdFGSLeH2pio5O")

    with tempfile.TemporaryFile() as fp:
        s3.download_fileobj(Fileobj=fp, Bucket='stats404-project-jingwu',
                            Key='knn_zillow.joblib')
        fp.seek(0)
        knn_dict = joblib.load(fp)
    #loading model from s3
    return knn_dict

# scoring/prediction part

logging.basicConfig(level=logging.INFO)
# Define one logger for current file
LOGGER = logging.getLogger(__name__)

def user_inputs():
    """this function will take user inputs for later calculation"""
    LOGGER.info("---Taking user inputs...")
    bathroomcnt = input("Please enter the number of bathrooms: ")
    bedroomcnt = input("Please enter the number of bedrooms: ")
    taxamount = input("Please enter the taxamount of the house: ")
    yearbuilt = input("Please enter the year the house is built as 'yyyy': ")
    calculatedfinishedsquarefeet = \
        input("Please enter the calculatedfinishedsquarefeet: ")
    transaction_yearmonth_i = \
        input("Please enter the transaction_yearmonth as 'yyyymm': ")
    # creating lists based on user input
    user_inputs = np.array(
        [[bathroomcnt, bedroomcnt, taxamount, yearbuilt,
          calculatedfinishedsquarefeet, transaction_yearmonth_i]])
    return user_inputs.astype(np.float64)

LOGGER.info("---Initializing model...")
KNN_DICT = initialize_model()

def model_output():
    """this function will initialize the model and output result"""

    log_error_pred = KNN_DICT.predict(user_inputs())
    LOGGER.info("---Output model result...")
    print("The log_error: " + str(log_error_pred))
    return log_error_pred

if __name__ == "__main__":
    model_output()
