

import pandas as pd

"""
1204. Last Person to Fit in the Bus (https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/)

sort the table by the turns column
iterate through the people until the total weight exceeds 1000

idk how to do this properly with pandas fucntions
surely this is good enough

runtime: O(n logn)
space: O(1)
"""

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn', inplace=True)

    capacity = 1000
    for person, weight in zip(queue['person_name'], queue['weight']):
        if weight > capacity:
            break
        capacity -= weight
        prev = person

    return pd.DataFrame({'person_name': [prev]})

