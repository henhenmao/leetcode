

import pandas as pd

"""
180. Consecutive Numbers (https://leetcode.com/problems/consecutive-numbers/description/)

my solution is iterative and is probably really slow and defeats the whole purpose of the pandas library

just iterates through one pass of the dataframe and checks if logs[i] == logs[i+1] == logs[i+2]
and i also convert to a set and back to a list to get rid of duplicates lmao

runtime: O(n) where n is the number of rows in logs
space: O(n)
"""


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    consecutive = []
    for i in range(len(logs)-2):
        if logs.iloc[i]["num"] == logs.iloc[i+1]["num"] and logs.iloc[i+1]["num"] == logs.iloc[i+2]["num"]:
            consecutive.append(logs.iloc[i]["num"])
    
    return pd.DataFrame(list(set(consecutive)), columns=["ConsecutiveNums"])


