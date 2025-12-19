
import pandas as pd

"""
1075. Project Employees I (https://leetcode.com/problems/project-employees-i/description/)

merge the two tables by employee id to add the number of hours each employee worked beside each employee id in project table
groupby the resulting table by the project_id and apply the mean aggregate on each project group, remember to round each value to 2 decimal points
rename the hours column

runtime: O(n)
space: O(n)
"""

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project, employee, on='employee_id')
    hours = df.groupby('project_id', as_index=False)['experience_years'].mean().round(2)
    hours = hours.rename(columns={'experience_years': 'average_years'})
    return hours