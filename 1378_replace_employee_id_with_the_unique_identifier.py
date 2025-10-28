
import pandas as pd

"""
1378. Replace Employee ID With The Unique Identifier (https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/)

literally just an left join between two tables
    employees that do not exist in unique_ids get null
    left join because all employees should be shown but not all unique_ids

runtime: O(n)
space: O(n)
"""

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, on='id', how='outer')[['unique_id', 'name']]