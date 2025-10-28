
import pandas as pd

"""
1327. List the Products Ordered in a Period (https://leetcode.com/problems/list-the-products-ordered-in-a-period/)

filter out orders not made in february 2020
merge the two tables by the product id
grouping by the product name, aggregate the sum of each product
filter out the products with less than 100 orders 

runtime: O(n)
space: O(n)
"""

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'].dt.year == 2020) & (orders['order_date'].dt.month == 2)]
    df = pd.merge(products, orders, on='product_id')
    df = df.groupby(by='product_name', as_index=False)['unit'].sum()
    df = df[df['unit'] >= 100]
    return df