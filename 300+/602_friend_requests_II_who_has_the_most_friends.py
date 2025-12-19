
import pandas as pd

"""
602. Friend Requests II: Who Has the Most Friends (https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/)
Follow up: In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?

get the value counts of both requester and accepter rows 
merge the two value counts together, fill null values with 0s
add the two value counts together into a new column

runtime: O(n)
space: O(n)
"""

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    requests = request_accepted['requester_id'].value_counts().reset_index().rename(columns={'requester_id':'id'})
    accepts = request_accepted['accepter_id'].value_counts().reset_index().rename(columns={'accepter_id':'id'})
    friends = pd.merge(requests, accepts, on='id', how='outer').fillna(0)
    friends['num'] = friends['count_x'] + friends['count_y']

    largest_friends = friends['num'].max()

    friends = friends[friends['num'] == largest_friends][['id', 'num']]
    return friends