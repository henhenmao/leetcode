
import pandas as pd

"""
627. Swap Salary (https://leetcode.com/problems/swap-salary/description/)

swap the values with pandas replace function

runtime: O(n)
space: O(1)
"""

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary.replace({'m':'f', 'f':'m'}, inplace=True)
    return salary