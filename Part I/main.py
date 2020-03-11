"""
Project: Zillow housing project.
Purpose: The model will make prediction on log_error base on user inputs.
Author: Jingwu Fang
Date: 03/09/2020
Contact Email: jingwufang94@outlook.com
PLEASE NOTE: This program will take around 150 seconds to run.
"""

import logging

import pandas as pd
import numpy as np
from sklearn import neighbors


# training part

def load_process_data():
    """load two datasets from s3"""
    file_name = "s3://stats404-project-jingwu/properties_2016.csv"
    prop = pd.read_csv(filepath_or_buffer=file_name,
                       encoding='latin-1')

    file_name = "s3://stats404-project-jingwu/train_2016_v2.csv"
    train = pd.read_csv(filepath_or_buffer=file_name,
                        encoding='latin-1')

    """feature engineering/data cleaning/merging"""
    X = prop[['parcelid', 'taxamount', 'yearbuilt', 'bathroomcnt', 'bedroomcnt',
              'calculatedfinishedsquarefeet']]
    X = X.dropna()
    # drop na
    X = X[(X.bathroomcnt > 0) & (X.bedroomcnt > 0) &
          (X.calculatedfinishedsquarefeet > 0)]
    # drop missing values
    X = pd.merge(X, train, on='parcelid')  # Merge X and train
    X.sort_values(by=['parcelid', 'transactiondate'], inplace=True)
    X['transactiondate'] = pd.to_datetime(X['transactiondate'], errors='coerce')
    X['transaction_yearmonth'] = 100 * X['transactiondate'].dt.year + \
                                 X['transactiondate'].dt.month
    min_transaction_yearmonth = X.transaction_yearmonth.min()
    X['transaction_yearmonth_i'] = X.transaction_yearmonth - \
                                   min_transaction_yearmonth

    return X


def split_data_X():
    """split data for model fitting."""
    X_final = load_process_data()[['bathroomcnt', 'bedroomcnt', 'taxamount',
                                   'yearbuilt', 'calculatedfinishedsquarefeet',
                                   'transaction_yearmonth_i']]
    return X_final


def split_data_y():
    """split data for model fitting."""
    y = load_process_data().logerror
    return y


def fit_model():
    """fit the model"""
    knn = neighbors.KNeighborsRegressor(n_neighbors=50, weights='distance', p=2,
                                        metric='minkowski', n_jobs=4)
    knn_fit = knn.fit(split_data_X(), split_data_y())
    return knn_fit


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
KNN_DICT = fit_model()


def model_output():
    """this function will initialize the model and output result"""

    log_error_pred = KNN_DICT.predict(user_inputs())
    LOGGER.info("---Output model result...")
    print("The log_error: " + str(log_error_pred))
    return log_error_pred


if __name__ == "__main__":
    model_output()
