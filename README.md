
python version: 3.7.6 <br />

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

### How to use input

Users input from command line. <br />
Input values: np.array([[4,4,5888,1999,2000,201002]]) <br />
Output: array([0.0166721])  <br />

### Architecture Diagrams:

The shared components bewteen training and scoring are feature engineering and data processing.

![architecture Diagram Training](https://user-images.githubusercontent.com/56213599/76169583-e406ca80-6136-11ea-99b0-ba9486c31a31.png)

![architecture Diagram scoring](https://user-images.githubusercontent.com/56213599/76169599-04368980-6137-11ea-9210-bc188d53b117.png)


### 1, Statement of problem:

Say for example, if you want to buy yourself a place, you look up Zillow, you will see this Zestimate price on the websit, which indicates an estimated price for the potential buyers/sellers' reference.

However, the actual sale price can't be the same with Zestimate, there is always a difference between the estimated price and the execution price. And my job here is to build a model to predict the difference between estimated price and this execution price by using a concept called log-error.

Also, starting June 2018, Zillow had started buying and selling homes with an average price of 250000 dollars as an agency. Thus, it is more and more important for them to know the value of their own purchases and the profit these properties will generate in the market.

### 2, Client:

Zillow Group, Inc.

### 3, Key Business Question

Are there any models for us to improve the accurancy of Zillow's home valuation estimation?

### 4, Data Source

Zillow's kaggle dataset

### 5, Business Impact of Work:

1, The resulting model stand to impact the home values of 110M homes across the U.S.

2, A home is often the largest and most expensive purchase a person makes. Ensuring homeowners have a trusted way to monitor this asset is incredibly important. 

3, Meet the need of the current Zillow users and attract more clients i.e. potential sellers/buyers/tenants.


### 6, How business will use (predicted) model to make decisions:

1, Help Zillow estimate home values effectively and efficiently by just adding the new predictions on top of the existing ones, resulting in prediction improvement.

2, Similar model can be applied to study other global markets and help Zillow grow more.

3, Our model will also help them make better purchase and selling decisions for their own Zillow properties.

