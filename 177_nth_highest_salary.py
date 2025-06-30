

import pandas as pd

"""
177. Nth Highest Salary (https://leetcode.com/problems/nth-highest-salary/)

do the same thing as 176. Second Highest Salary but use N instead of 2
remove duplicates and sort the values in non ascending order
get the salary at index N-1 only if index N is a valid index between 1 and df.size-1
return the nth highest salary in the form of a dataframe

runtime: O(r * log(r))
space: O(r)
"""

def nth_highest_salary(df: pd.DataFrame, N: int) -> pd.DataFrame:
    df = df["salary"].drop_duplicates().sort_values(ascending=False)
    nthSalary = df.iloc[N-1] if (N >= 1 and N <= df.size) else None

    return pd.DataFrame({f"getNthHighestSalary({N})": [nthSalary]})