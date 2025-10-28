
import pandas as pd

"""
185. Department Top Three Salaries (https://leetcode.com/problems/department-top-three-salaries/)

merge the two tables together by the department id
grouping by the department id, rank the salaries of each department group
    make sure to use method='dense' so that equal salaries get the same rank
    also remember to rank in non ascending order
select the rows with a rank of 3 or less
rename the columns

runtime: O(n logn)
space: O(1)
"""

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department.rename(columns={'id': 'departmentId'}, inplace=True)
    df = pd.merge(employee, department, on='departmentId')
    df['rank'] = df.groupby(by='departmentId')['salary'].rank(method='dense', ascending=False)
    df = df[df['rank'] <= 3]
    df.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}, inplace=True)
    return df[['Department', 'Employee', 'Salary']]