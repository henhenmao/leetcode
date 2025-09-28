
import pandas as pd

"""
577. Employee Bonus (https://leetcode.com/problems/employee-bonus/description/)

do an outer join between the employee and bonus dataframes
    employees without a matching bonus value get a null bonus

select only rows with a bonus of null or less than 1000

runtime: O(n + m)
space: O(n + m)
"""

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # outer join matches bonus values to the matching empIds
    # empIds that do not get a match have no bonus, and are set to null
    df = pd.merge(employee, bonus, how="outer")

    # cleaning the dataframe to only have name and bonus
    df = df[['name', 'bonus']]

    # only selecting rows where bonus is either null or less than 1000
    df = df[(df['bonus'].isnull()) | (df['bonus'] < 1000)]
    return df