import pandas as pd
import time
import numpy as np

artists = pd.read_csv("data/artists.csv")


def create_follower_genre_feature(
    followers, genres):

    return 1 if followers > 10 and len(genres) > 0 else 0


vec_create_follower_genre_feature = np.\
    vectorize(create_follower_genre_feature)


col = "high_followers_has_genre"
artists[col] = vec_create_follower_genre_feature(
    artists.followers,
    artists.genres)