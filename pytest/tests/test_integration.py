"""Module for integration testing of user inputs related functions.
"""
import math
import pandas as pd
import numpy as np


from year_adjustment.limit_on_years import built_year, yearmonth_transaction
from year_adjustment.limit_on_years import inputs_not_nan



def test_input_integration():
    """Integration test to check that the model is taking the valid inputs.
       First a test on year inputs, then test whether there's a nan value in
       the input array.
    """
    expected_inputs = np.array([[4, 5, 13245, 1962, 4000, 200909]])
    yearbuilt = built_year(1962)
    bathroomcnt = 4
    bedroomcnt = 5
    taxamount = 13245
    calculatedfinishedsquarefeet = 4000 
    transaction_yearmonth_i = yearmonth_transaction(200909)
    inputs = np.array([[4, 5, 13245, yearbuilt, 4000, transaction_yearmonth_i]])
    actual_inputs = inputs_not_nan(inputs)
    assert np.array_equal(expected_inputs, actual_inputs), \
    """Should show that the user inputs are valid this time.
    """
                                                                       
                                                                               
                                                                              
                                                                              
                                                                               


