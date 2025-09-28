
import pandas as pd


"""
570. Managers with at Least 5 Direct Reports (https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/)

get the value counts of the managerId's and filter out managerId's with a count less than 5
for each remaining managerId, inner join with the ids in the original table and return the names of each person left

runtime: O(n)
space: O(n)
"""


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.value_counts('managerId').reset_index()
    counts = counts[counts['count'] >= 5]
    employee = pd.merge(employee, counts, left_on='id', right_on='managerId')
    return employee[['name']]