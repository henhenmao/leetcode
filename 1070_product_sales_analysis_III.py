
import pandas as pd

"""
1070. Product Sales Analysis III (https://leetcode.com/problems/product-sales-analysis-iii/)

use groupby transform min on the years to find the first year each product was sold
    first_years will be a series that is aligned with the Sales table, containing the first year each product was sold
filter out the products which has a year that does not match with the product's first year
rename the columns

runtime: O(n)
space: O(n)
"""

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_years = sales.groupby('product_id')['year'].transform('min')
    sales = sales[sales['year'] == first_years]
    sales.rename(columns={'year': 'first_year'}, inplace=True)
    return sales[['product_id', 'first_year', 'quantity', 'price']]