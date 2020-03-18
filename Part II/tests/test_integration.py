"""Module for integration testing of 'adjust_price' functions.
"""
import math
import pandas as pd
import numpy as np


from year_adjustment.limit_on_years import built_year, yearmonth_transaction
from year_adjustment.limit_on_years import inputs_not_nan



def test_input_integration():
    """Integration test to check that we can get the final price of an item
       in case the item is discounted, before taxes are applied.
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
    """Should show that the price is reduced by less than 25%, after taxes
       are applied to the discounted price.
    """
                                                                       
                                                                               
                                                                              
                                                                              
                                                                               

