### 0, Architecture Diagrams:

The shared components bewteen training and scoring are feature engineering and data processing.

![architecture Diagram Training](https://user-images.githubusercontent.com/56213599/76169583-e406ca80-6136-11ea-99b0-ba9486c31a31.png)

![architecture Diagram scoring](https://user-images.githubusercontent.com/56213599/76169599-04368980-6137-11ea-9210-bc188d53b117.png)

## Input and output specs:<br />
Input: <br />
numpy array containing: <br />
'bathroomcnt': Number of bathroom. <br />
'bedroomcnt': Number of bedroom. <br />
'taxamount': The total property tax assessed for that assessment year. <br />
'yearbuilt': The Year the principal residence was built. <br />
'calculatedfinishedsquarefeet': Calculated total finished living area of the home. <br />
'transaction_yearmonth_i': The specific year and month the residence was traded.  <br />

Output: <br />
'log_error': log error is defined as logerror=log(Zestimate)−log(SalePrice)  <br />

EX: <br />
Input: np.array([[4,4,5888,1999,2000,201002]]) <br />
Output: array([0.009104])  <br />
