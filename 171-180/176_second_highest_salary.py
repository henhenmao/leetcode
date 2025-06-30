
import pandas as pd

"""
176. Second Highest Salary (https://leetcode.com/problems/second-highest-salary/)

use drop_duplicate to only see distinct salary vlaues
sort the salaries so that the second highest salary always shows up at index 1 to us to check
use iloc[1] to access the salary at index 1

return the second highest salary in the form of a dataframe labelled "SecondHighestSalary"

runtime: O(r * log(r))
space: O(r) since sorted
"""

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee["salary"].drop_duplicates().sort_values(ascending=False)
    secondSalary = employee.iloc[1] if len(employee) >= 2 else None
    
    return pd.DataFrame({"SecondHighestSalary": [secondSalary]})

