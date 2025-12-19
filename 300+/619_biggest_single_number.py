
import pandas as pd

"""
619. Biggest Single Number (https://leetcode.com/problems/biggest-single-number/)

get the value counts of every number
    select only those with a value count of 1

if the table is empty, there are no single numbers so return empty dataframe
else, return the max index of the value counts

runtime: O(n)
space: O(n)
"""

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers['num'].value_counts()
    singles = df[df == 1]

    if singles.empty:
        return pd.DataFrame({'num': [None]})
    
    return pd.DataFrame({'num': [singles.index.max()]})
