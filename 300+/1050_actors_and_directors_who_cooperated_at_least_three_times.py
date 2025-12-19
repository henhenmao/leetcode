
import pandas as pd

"""
1050. Actors and Directors Who Cooperated at Least Three Times (https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)

group by actor-director pairs and get the frequency of each distinct grouped pair
select actor-director pairs that have a frequency of at least 3 times

idk group by time complexity
runtime: O(n)
space: O(n)
"""

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    df = df[df['count'] >= 3][['actor_id', 'director_id']]
    return df