
import pandas as pd

"""
1907. Count Salary Categories (https://leetcode.com/problems/count-salary-categories/description/)

simply select low income, average income, and high income from the accounts table
manually construct new dataframe from the three split sections

runtime: O(n)
space: O(n)
"""


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts['income'] < 20000])
    avg = len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)])
    high = len(accounts[accounts['income'] > 50000])

    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low, avg, high]
    })