
import pandas as pd

"""
1484. Group Sold Products By The Date (https://leetcode.com/problems/group-sold-products-by-the-date/description/)

drop duplicate columns with the same product and date

create two separate groupby dataframes
grouping by each separate day products were sold
    one groupby aggregates each product sold in that day and joins them all into a string separated by commas
    the second groupby aggregates each product sold in that day and counts the number of products

    all products are distinct for a given day because duplicates were dropped beforehand

merge the two groupby tables by the sell_date
rename the columns

runtime: O(n logk) where n is the number of rows and k is the number of unique days
space: O(n)
"""

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    def getProducts(series):
        series = ",".join(series.sort_values())
        return series

    activities.drop_duplicates(inplace=True)
    products = activities.groupby(by='sell_date', as_index=False)['product'].agg(getProducts)
    num_sold = activities.groupby(by='sell_date', as_index=False)['product'].count()
    df = pd.merge(num_sold, products, on='sell_date')
    df.rename(columns={'product_x': 'num_sold', 'product_y': 'products'}, inplace=True)
    return df