"""Module containing helper function(s) to test if user inputs(year) make sense.
"""
import math
import numpy as np

def built_year(yearbuilt):
    """Function to set a limit on built_year."""
    #since our database does not contain any info after 2016
    if yearbuilt > 2016 or yearbuilt<1900:
        raise ValueError("Error: invalid built year.")
    else:
        return yearbuilt

def yearmonth_transaction(transaction_yearmonth_i):
    """Function to set a limit on transaction yearmonth."""
    # once again, our dataset doesn't include transaction data beyond 2016
    if transaction_yearmonth_i >201612 or transaction_yearmonth_i<199009:
        raise ValueError("Error: invalid transaction_yearmonth value.")
    else:
        return transaction_yearmonth_i

def inputs_not_nan(user_inputs):
	"""Function to check if any input is nan."""
	inputsum = np.sum(user_inputs)
	if inputsum == True:
		raise ValueError("Error: inputs contain nan")
	else:
		return user_inputs
