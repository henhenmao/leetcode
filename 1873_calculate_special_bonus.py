
import pandas as pd

"""
1873. Calculate Special Bonus (https://leetcode.com/problems/calculate-special-bonus/description/)

create boolean mask of employees who fulfilled the bonus conditions
create a new bonus column as the product of the salary and bonus fulfillment (either 0 or 1)
filter proper rows and sort resulting table by employee id

runtime: O(n logn)
space: O(n)
"""

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees['employee_id'] % 2 == 1) & (employees['name'].str[0] != 'M')
    employees['bonus'] = employees['salary'] * mask
    return employees[['employee_id', 'bonus']].sort_values('employee_id')