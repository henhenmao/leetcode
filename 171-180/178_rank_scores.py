
import pandas as pd

"""
178. Rank Scores (https://leetcode.com/problems/rank-scores/description/)

pandas rank method: computes numerical ranks from 1 through n
    method='dense': gives equal values the same rank instead of an average

add a new column with the scores converted to rank in ascending order
select just the score and rank column and sort the table by the rank in ascending order

runtime: O(n logn)
space: O(n)
"""

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores = scores[['score', 'rank']].sort_values('rank')
    return scores