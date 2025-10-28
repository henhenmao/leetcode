
import pandas as pd

"""
1045. Customers Who Bought All Products (https://leetcode.com/problems/customers-who-bought-all-products/description/)

drop duplicate rows because duplicate purchases from the same person are meaningless
groupby each customer_id group and get the size of the group
any group with a size of len(product) bought from each group

runtime: O(n)
space: O(n)
"""

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer = customer.drop_duplicates() # customers can buy same thing multiple times
    customer = customer.groupby(by='customer_id', as_index=False).size()
    customer = customer[customer['size'] == len(product)]
    return customer[['customer_id']]