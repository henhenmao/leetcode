
import pandas as pd

"""
1890. The Latest Login in 2020 (https://leetcode.com/problems/the-latest-login-in-2020/description/)

filter out logins with time_stamps not in 2020
grouping by the user_id, get the max time_stamp
    you can use max() aggregate functions for datetimes 🥰
rename the time_stamp column to last_stamp

runtime: O(n)
space: O(n)
"""

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[logins['time_stamp'].dt.year == 2020]
    logins = logins.groupby(by='user_id', as_index=False).max()
    logins.rename(columns={'time_stamp': 'last_stamp'}, inplace=True)
    return logins 