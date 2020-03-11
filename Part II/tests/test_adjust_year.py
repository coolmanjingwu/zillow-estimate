"""Module for unit testing of 'year_adjustment'
   functions.
"""
import math
import pytest
from year_adjustment.limit_on_years import built_year, yearmonth_transaction

def test_built_year():
	"""Unit test to showcase functionality of applying a limit to user\
	input built year"""
	
	expected_output = 1999
	output_year = built_year(1999)
	assert math.fabs(output_year-expected_output) < 0.001, \
	"""Should show that the built_year entered is valid"""


def test_transaction_yearmonth():
	"""Unit test to showcase functionality of applying a limit to user\
	input transaction_yearmonth"""
	
	expected_output = 200404
	output_year = yearmonth_transaction(200404)
	assert math.fabs(output_year-expected_output) < 0.001, \
	"""Should show that the transaction_yearmonth entered is valid"""
	
		
def test_built_year_throws_error_beyond_limit():
    """Unit test to showcase edge case behavior of throwing an error when
       user input a year that is beyond 2016.
    """
    with pytest.raises(ValueError):
        built_year(2029)
        
        

        
