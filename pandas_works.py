import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#################################################################################

'''
Pandas Fundamentals
'''

'''
1. Series and DataFrame Creation
Exercise 1.1: Create a Pandas Series and DataFrame from different data sources.
'''

s = pd.Series([1,3,4,np.nan, 6,8])
#print(f"Series: {s}")

df_s = pd.DataFrame(s)
#print(f"DataFrame from series: {df_s}")

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Boston', 'Chicago', 'Denver']
}

df_dict = pd.DataFrame(data)
#print(f"DataFrame from dictionary: {df_dict}")s


# Create a DataFrame from a NumPy array
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns = list('ABCD'))
#print(df)




#################################################################################

'''
2. Data Selection and Filtering
Exercise 2.1: Select and filter data from a DataFrame.
'''

# Find and count the missing values in each column
# Fill missing names with "Unknown" and missing ages with the mean age
# Filter the DataFrame to show only customers from New York
# Calculate the average purchase amount by city
# Sort the DataFrame by purchase amount in descending order

data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John Smith', 'Jane Doe', 'Bob Johnson', np.nan, 'Alice Brown', 'Charlie Davis', np.nan, 'Eve Wilson', 'Frank Miller', 'Grace Lee'],
    'age': [35, 28, 42, 50, np.nan, 31, 39, np.nan, 45, 36],
    'city': ['New York', 'Boston', 'Chicago', 'Seattle', 'San Francisco', 'New York', 'Boston', 'Chicago', np.nan, 'San Francisco'],
    'purchase_amount': [150.25, 200.50, np.nan, 300.75, 150.00, 250.25, 175.50, np.nan, 225.75, 350.00]
}

df = pd.DataFrame(data)

# Find and count the missing values in each column
#print(df.isnull())

#print(df.isnull().sum())

###
# Fill missing names with "Unknown" and missing ages with the mean age
df1 = df.copy()
df1['name'] = np.where(df1['name'].isnull(),"Unknown",df1['name'])


#print(f"Missing Names df:{df}")
#print(f"Imputed Missing Names df:{df1}")

###
# Filter the DataFrame to show only customers from New York
#print(df1[df1['city']== 'New York']['name'])

###
# Calculate the average purchase amount by city
#print(df.groupby('city')['purchase_amount'].mean())

###
# Sort the DataFrame by purchase amount in descending order
#print(df.sort_values(by='purchase_amount',ascending=False))


#################################################################################

'''
Problem 2: Data Merging, Reshaping, and Time Series Analysis
In this problem, you'll work with sales data across different stores and products.
'''
# Sales data
sales_data = {
    'date': pd.date_range(start='2023-01-01', periods=10),
    'store_id': [1, 2, 1, 3, 2, 1, 3, 2, 1, 3],
    'product_id': [101, 102, 103, 101, 103, 102, 102, 101, 103, 101],
    'quantity': [5, 7, 3, 8, 4, 6, 2, 9, 5, 7],
    'sales_amount': [50.25, 70.50, 30.75, 80.00, 40.25, 60.50, 20.75, 90.00, 50.25, 70.50]
}

sales_df = pd.DataFrame(sales_data)

# Store information
store_data = {
    'store_id': [1, 2, 3, 4],
    'location': ['New York', 'Boston', 'Chicago', 'Denver'],
    'manager': ['John Smith', 'Jane Doe', 'Bob Johnson', 'Alice Brown']
}

store_df = pd.DataFrame(store_data)

# Product information
product_data = {
    'product_id': [101, 102, 103, 104],
    'product_name': ['Widget A', 'Widget B', 'Widget C', 'Widget D'],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Home Goods'],
    'price': [10.00, 12.50, 8.75, 15.00]
}

product_df = pd.DataFrame(product_data)

# Merge the sales data with store and product information to create a comprehensive dataset
df_combined1 = pd.merge(sales_df,store_df, how='inner',on='store_id')
#print(df_combined1)

df_combined_full = pd.merge(df_combined1,product_df,how='inner',on='product_id')
#print(df_combined_full)

###
# Calculate total sales amount and quantity by store
#print(df_combined_full.groupby('store_id')[['sales_amount','quantity']].sum().reset_index())


### 
# Find the best-selling product by quantity
#print(df_combined_full.groupby(['product_name','product_id'])['quantity'].sum().reset_index().sort_values(by='quantity',ascending=False).iloc[0])

###
# 4. Reshape the data to show sales amount by store and product (pivot table)
# Create a pivot table with store_id as rows, product_name as columns, and sales_amount as values

df_new = df_combined_full[['store_id','product_name','sales_amount']]

table = pd.pivot_table(df_new, values='sales_amount',index='store_id',columns='product_name',aggfunc='sum')
#print(table)

###
# 5. Resample the data to show weekly sales totals

#df_combined_full['week'] = df_combined_full['date'].dt.strftime('%U')

#print(df_combined_full.groupby('week')['sales_amount'].sum().reset_index())

df_time = df_combined_full.set_index('date')

weekly_sales = df_time.resample('W')['sales_amount'].sum()

#print(weekly_sales)


###
# 6. Calculate a 3-day rolling average of sales
#print(df_time['sales_amount'].rolling(3).mean())