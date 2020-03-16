"""Module for integration testing of 'adjust_price' functions.
"""
import math
import pandas as pd
import numpy as np
import boto3
import joblib
import requests
import s3fs

from year_adjustment.limit_on_years import built_year, yearmonth_transaction

def initialize_model():
    """this function will load from aws s3 and initialize the model"""
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('stats404-project-jingwu')
    bucket.download_file('knn_zillow.joblib', 'knn_zillow.joblib')
    #load model
    knn_dict = joblib.load('knn_zillow.joblib')
    return knn_dict

knn_dict = initialize_model()

def test_year_adjustment_integration():
    """Integration test to check that we can get the final price of an item
       in case the item is discounted, before taxes are applied.
    """
    expected_output_log_error = 0.032336
    yearbuilt = built_year(1962)
    bathroomcnt = 4
    bedroomcnt = 5
    taxamount = 13245
    calculatedfinishedsquarefeet = 4000 
    transaction_yearmonth_i = yearmonth_transaction(200909)
    user_inputs = np.array([[4, 5, 13245, yearbuilt, 4000, transaction_yearmonth_i]])
    user_inputs_final = user_inputs.astype(np.float64)
    output_log_error = knn_dict.predict(user_inputs_final)
    assert math.fabs(output_log_error - expected_output_log_error) < 0.001, \
   
                                                                       
                                                                               
                                                                              
                                                                              
                                                                               


