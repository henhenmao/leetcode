

import pandas as pd

"""
1341. Movie Rating (https://leetcode.com/problems/movie-rating/)

getting the user who has given the most ratings
    get the value counts of user_id from the MovieRatings table
    filter out the rows that do not have the largest count of ratings
    merge the resulting count table to the Users table
    note down the row with the lexicographically smallest name, ['name'].min()

getting the movie with the highest average rating in february 2020
    from MovieRatings, filter out the movies that were not rated in the proper time frame
    grouping by the movie_id, get the mean average of each movie_id and get the row with the max average rating
    filter out movies that contain the highest rating 
    merge the resulting movies with the Movies table
    get the lexicographically smallest name of the movie

with the name of the person with the most amount of ratings and the movie with the highest rating
    put them in a dataframe and return

runtime: O(n)
space: O(n)
"""

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:

    # first part
    user_ratings = movie_rating.value_counts('user_id').reset_index()
    user_ratings = user_ratings[user_ratings['count'] == user_ratings['count'].max()]
    user_ratings = pd.merge(user_ratings, users, on='user_id')
    user_most_ratings = user_ratings['name'].min()

    # second part
    movie_rating = movie_rating[(movie_rating['created_at'].dt.year == 2020) & (movie_rating['created_at'].dt.month == 2)]
    movie_rating = movie_rating.groupby(by='movie_id', as_index=False).mean()
    movie_rating = movie_rating[movie_rating['rating'] == movie_rating['rating'].max()]
    movie_rating = pd.merge(movie_rating, movies, on='movie_id')
    movie_highest_rating = movie_rating['title'].min()

    return pd.DataFrame({'results': [user_most_ratings, movie_highest_rating]})
