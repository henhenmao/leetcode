
import pandas as pd

"""
2879. Display the First Three Rows (https://leetcode.com/problems/display-the-first-three-rows/description/)

display the first three rows in pandas
that's it

runtime: O(1)
space: O(1)
"""

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]