

import pandas as pd

"""
1934. Confirmation Rate (https://leetcode.com/problems/confirmation-rate/description/)

use groupby() and agg() to groupby with a custom aggregate function
    create a function that takes a groupby series and returns the percentage of 'confirmed'
    remember to round answers to two decimal places

outer join the groupby table with the Signups table and fillna with 0s
rename the action columnn to confirmation_rate

runtime: O(n)
space: O(n)
"""

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    def confirmation(series):
        return ((series == 'confirmed').mean()).round(2)

    confirmations = confirmations.groupby(by='user_id', as_index=False)['action'].agg(confirmation)
    signups = pd.merge(signups, confirmations, on='user_id', how='outer').fillna(0)
    signups.rename(columns={'action': 'confirmation_rate'}, inplace=True)
    return signups[['user_id', 'confirmation_rate']]