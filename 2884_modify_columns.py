import pandas as pd


"""
2884. Modify Columns (https://leetcode.com/problems/modify-columns/description/)

multiplies each salary in each row by 2

runtime: O(n)
space: O(1)
"""

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"]*=2
    return employees