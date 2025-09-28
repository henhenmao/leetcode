
import pandas as pd

"""
1407. Top Travellers (https://leetcode.com/problems/top-travellers/description/)

join the Users and Rides tables by the user_id in Rides and id in Users
    rename the id column in Users table to user_id to make joining easier
groupby by the [names, user_id] of each user and get the sum all ride distances for each user
    groupby both of these attributes because two people with different user_ids can have different names

sort by the distance in descending order
filter columns to just display the name and distance
rename the distance colkumn to match the output

runtime: O(n * logn)
space: O(n)
"""

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    users.rename(columns={'id': 'user_id'}, inplace=True)
    users = pd.merge(users, rides, on='user_id', how='outer')
    users = users.groupby(by=['name', 'user_id'], as_index=False).sum()

    users.sort_values('distance', ascending=False, inplace=True)
    users = users[['name', 'distance']]
    users.rename(columns={'distance': 'travelled_distance'}, inplace=True)

    return users