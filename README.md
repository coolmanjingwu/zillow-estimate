# HW1 Six components of my business use case(Zillow)

## Name: Jingwu Fang

### 0, Architecture Diagrams:

The shared components bewteen training and scoring are feature engineering and data processing.

![architecture Diagram Training](https://user-images.githubusercontent.com/56213599/76169583-e406ca80-6136-11ea-99b0-ba9486c31a31.png)

![architecture Diagram scoring](https://user-images.githubusercontent.com/56213599/76169599-04368980-6137-11ea-9210-bc188d53b117.png)

## Input and output specs:
Input: 
numpy array containing:
'bathroomcnt': Number of bathroom.
'bedroomcnt': Number of bedroom.
'taxamount': The total property tax assessed for that assessment year.
'yearbuilt': The Year the principal residence was built.
'calculatedfinishedsquarefeet': Calculated total finished living area of the home.
'transaction_yearmonth_i': The specific year and month the residence was traded.

Output: 
'log_error': log error is defined as logerror=log(Zestimate)−log(SalePrice)

EX: 
Input: np.array([[4,4,5888,1999,2000,201002]])
Output: array([0.009104])



### 1, Statement of problem:

In US, millions of people use Zillow to estimate home valuation. It is essential for Zillow to provide consumers with useful and accurate information about homes and the housing market.

Also, starting 2019, Zillow had started buying and selling homes as an agency. Thus, it is more and more important for them to know the value of their own purchases and the profit these properties will generate in the market.

However, each property has hundreds of data points and varys significantly from each other. It is quite difficult to improve the margin of error. 

### 2, Client:

Zillow Group, Inc.

### 3, Key Business Question

Are there any models for us to improve the Zillow's home valuation estimation?

### 4, Data Source

Zillow's kaggle dataset

### 5, Business Impact of Work:

1, The resulting model stand to impact the home values of 110M homes across the U.S.

2, A home is often the largest and most expensive purchase a person makes. Ensuring homeowners have a trusted way to monitor this asset is incredibly important. 

3, Meet the need of the current Zillow users and attract more clients i.e. potential sellers/buyers/tenants.


### 6, How business will use (predicted) model to make decisions:

1, Help Zillow estimate home values effectively and efficiently.

2, The resulting model will let Zillow know who and where are the potential buyers or sellers, also will improve its advertising stats.

3, Similar model can be applied to study other global markets and help Zillow grow more.

4, Our model will also help them make better purchase and selling decisions for their own Zillow properties.



