
import pandas as pd

"""
511. Game Play Analysis I (https://leetcode.com/problems/game-play-analysis-i/)

sort the database by the event date of each login
remove all play id duplicate while keeping the first occurence (earlies login occurence)
rename the event date column to first_login

runtime: O(n logn)
space: O(n)
"""

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['event_date'], inplace=True)
    activity.drop_duplicates(subset=["player_id"], inplace=True)
    activity = activity[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})
    return activity