
import pandas as pd

"""
1148. Article Views I (https://leetcode.com/problems/article-views-i/description/)

drop duplicate rows that share the same author_id and viewer_id
select only the rows where the author_id and viewer_id are equal 
    this means that the viewer of the article and the author of the article are the same people
select one of the columns since they're both the same and rename the column
sort the id column in ascending order

runtime: O(n logn)
space: O(n)
"""

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views.drop_duplicates(subset=['author_id', 'viewer_id'], inplace=True)
    views = views[views['author_id'] == views['viewer_id']]
    views = views[['author_id']]
    views.rename(columns={'author_id': 'id'}, inplace=True)
    views.sort_values('id', inplace=True)
    return views
    