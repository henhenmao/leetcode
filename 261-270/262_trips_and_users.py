
import pandas as pd

"""
262. Trips and Users (https://leetcode.com/problems/trips-and-users/description/)

filter out the trip requests made outside dates from 2013-10-01 and 2013-10-03 inclusive from Trips table
filter out users who are banned from Users table
join the Users table to the Trips twice, one for the client_ids and one for the driver_ids
    this removes the trips made from banned users from Users

grouping by the request date, calculate the percentage of cancelled requests
    you can check for a cancelled request if the status is != 'completed
    i wasn't sure how to make the aggregate function return a dataframe so i just reset_index and renamed/changed the columns 

runtime: O(n)
space: O(n)
"""

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    def cancellation(series):
        return ((series != 'completed').mean()).round(2)

    start = pd.to_datetime("2013-10-01")
    end = pd.to_datetime("2013-10-03")
    users = users[users['banned'] == 'No']
    trips = trips[(pd.to_datetime(trips['request_at']) >= start) & (pd.to_datetime(trips['request_at']) <= end)]

    # merge twice for clients and drivers
    # removes the banned users
    df = pd.merge(trips, users, left_on='client_id', right_on='users_id')
    df = pd.merge(df, users, left_on='driver_id', right_on='users_id')

    df = df.groupby(by='request_at', as_index=False)['status'].agg(cancellation).reset_index()
    df.rename(columns={'request_at': 'Day', 'status': 'Cancellation Rate'}, inplace=True)
    return df[['Day', 'Cancellation Rate']]