


import pandas as pd

"""
620. Not Boring Movie (https://leetcode.com/problems/not-boring-movies/description/)

filter for (odd id number) and (description not equal to 'boring')
sort the final filtered table in descending order by rating

runtime: O(n log n)
space: O(n)
"""


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['id'] % 2 == 1) & ~(cinema['description'] == 'boring')].sort_values('rating', ascending=False)