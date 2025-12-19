
import pandas as pd

"""
607. Sales Person (https://leetcode.com/problems/sales-person/)

get a table of people who have been involved with RED company
return all people who are not in that table

runtime: O(a + b + c) where a b c are the sizes of each table
space: O(a + b + c)
"""

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red = company[company['name'] == "RED"][['com_id']]
    df = orders[orders['com_id'].isin(red['com_id'])]
    res = sales_person[~sales_person['sales_id'].isin(df['sales_id'])][['name']]

    return res