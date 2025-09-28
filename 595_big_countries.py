
from pandas import pd

"""
595. Big Countries (https://leetcode.com/problems/big-countries/description/)

just select rows with area at least 3 million area or at least 25 million population
filter out the proper columns

runtime: O(n)
space: O(n)
"""

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    df = df[['name', 'population', 'area']]
    return df