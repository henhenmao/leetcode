

import pandas as pd

"""
626. Exchange Seats (https://leetcode.com/problems/exchange-seats/)

look through every two indexes in the table and swap every i and i+1 values in the student column

runtime: O(n)
space: O(1)
"""

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    for i in range(0, len(seat)-1, 2):
        seat.loc[i, 'student'], seat.loc[i+1, 'student'] = seat.loc[i+1, 'student'], seat.loc[i, 'student']
    return seat