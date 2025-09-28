

import pandas as pd

"""
183. Customers Who Never Order (https://leetcode.com/problems/customers-who-never-order/description/)

Customers contain matches of ids to names
Orders contain a column of customer ids who have ordered

select the customers in Customers whose id's do NOT exist in the database of Orders, and display the names of each selected customer
select only the name column of the returned dataframe and rename to the proper output name

runtime: O(n)
space: O(n)
"""

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # select customers that don't exist in the orders
    df = customers[~customers['id'].isin(orders['customerId'])]
    # select only the name column and rename it to the output specifications
    df = df[['name']].rename(columns={'name' : 'Customers'})
    return df