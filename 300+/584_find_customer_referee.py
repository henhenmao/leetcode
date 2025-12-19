
import pandas as pd

"""
584. Find Customer Referee (https://leetcode.com/problems/find-customer-referee/)

just filter for (isnull()) or (!= 2) and output the name column

runtime: O(n)
space: O(n)
"""

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer['referee_id'].isnull()) | ~(customer['referee_id'] == 2)][['name']]