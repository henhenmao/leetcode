

import pandas as pd

"""
1068. Product Sales Analysis I (https://leetcode.com/problems/product-sales-analysis-i/description/)

do an inner join of the sales and product table to match the product id to the product name
thats it

runtime: O(n)
space: O(n)
"""

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sales, product)
    return df[['product_name', 'year', 'price']]