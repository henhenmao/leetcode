

import pandas as pd

"""
1158. Market Analysis I (https://leetcode.com/problems/market-analysis-i/)

user_id and join_date are already matched together
just need to get the number of orders that each user_id made in 2019

filter out all 2019 purchases from the table of orderrs
    from the filtered table, get the value_count of user_ids to get the number of orders from each distinct user_id

merge the value counts and the user table together, filter out proper columns

runtime: O(n)
space: O(n)
"""


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders2019 = orders[orders['order_date'].dt.year == 2019]
    count2019 = orders2019['buyer_id'].value_counts().reset_index()
    users = users.rename(columns={'user_id': 'buyer_id'})
    count2019 = count2019.rename(columns={'count': 'orders_in_2019'})
    users = pd.merge(users, count2019, on='buyer_id', how='outer').fillna(0)[['buyer_id', 'join_date', 'orders_in_2019']]
    return users