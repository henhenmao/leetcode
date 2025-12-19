
import pandas as pd

"""
184. Department Highest Salary (https://leetcode.com/problems/department-highest-salary/description/)

rename the columns in department to be distinct from columns in employee
merge the two tables together, put department on the left to make life easier
grouping by the department ids, make a table containing the max salary for each department
filter out the rows that do not have a max salary
rename the columns for the output

runtime: O(n)
space: O(n)
"""

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns={'id': 'departmentId', 'name':'departmentName'})
    df = pd.merge(department, employee, on='departmentId')
    max_salaries = df.groupby('departmentId')['salary'].transform('max')
    df = df[df['salary'] == max_salaries][['departmentName', 'name', 'salary']]
    df = df.rename(columns={'departmentName': 'Department', 'name': 'Employee', 'salary': 'Salary'})
    return df