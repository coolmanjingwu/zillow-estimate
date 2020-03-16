### I wrote a different main.py for the test suites, this one will load the model from s3, which will save a lot of time. <br /> 

Unit test 1: Set limit on built year. <br /> 

  Since our data was from 2016, which means any house that is built after 2016 won't be taken into consideration.<br /> 

Unit test 2: Set limit on transaction year month.<br /> 

  Since our data was from 2016, which means any house that is transacted after 201612 won't be taken into consideration.<br /> 

Unit test 3: <br /> 
  Input an invalid built year, see if it will throw error. <br /> 

Unit test 4: <br /> 
  Input an invalid transaction yearmonth, see if it will throw error. <br /> 

Integration test:<br /> 

  Make a prediction on the log_error(i.e. model output) using unit test1 and unit test2 along with other user inputs.
