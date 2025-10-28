
import pandas as pd

"""
1965. Employees With Missing Information (https://leetcode.com/problems/employees-with-missing-information/description/)

get the list of employees that exist in employees but not in salaries
get the list of employees that exist in salaries but not in employees
merge the two lists together

runtime: O(n)
space: O(n)
"""

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df1 = employees[~employees['employee_id'].isin(salaries['employee_id'])]
    df2 = salaries[~salaries['employee_id'].isin(employees['employee_id'])]
    df = pd.merge(df1, df2, on='employee_id', how='outer')
    return df[['employee_id']]