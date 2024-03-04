# Try implementing a cache from scratch yourself. The cache could
# be an LRU cache or another type of cache. Test your cache to get
# predictions with the model we trained earlier.

# from ch4.ml_model import MlModel
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
import pandas as pd
import time
from functools import lru_cache

if __name__ == "__main__":

    # parameters = {"n_estimators": (50, 100, 150, 200),
    #             "max_depth": (1, 2),
    #             "min_samples_split": (100, 250, 500, 750, 1000)
    #                 }

    # forest_model = MlModel(ml_model = RandomForestRegressor(),
    #                 parameters = parameters,
    #                 n_jobs = 10,
    #                 scoring = "neg_mean_squared_error",
    #                 n_iter = 5,
    #                 random_state = 0)


    # artists = pd.read_csv("data/artists.csv")

    # artists = artists.dropna().reset_index(drop = True)

    # artists['num_genres'] = artists.genres.map(len)
    # features = ["followers", "num_genres"]

    # forest_model.tune(artists[features], artists.popularity)

    # @lru_cache(maxsize=10)
    # def get_model_predictions(model, inputs):
        
        
    #     formatted_inputs = pd.DataFrame.from_dict({"followers": inputs[0], 
    #                             "num_genres": inputs[1]}, orient = "index").transpose()
    #     #pd.DataFrame(artists[features].iloc[10]).transpose()
    #     return model.predict(formatted_inputs)


    # inputs = (2, 4)

    # start = time.time()
    # get_model_predictions(forest_model, inputs)
    # end = time.time()
    # print("Model predictions runtime (w/o) cache: ", end - start)

    # start = time.time()
    # get_model_predictions(forest_model, inputs)
    # end = time.time()
    # print("Model predictions runtime (w/) cache: ", end - start)

    # Can you do more complex NumPy vectorization tasks with arrays?
    #  Try timing them, and then implementing versions of your code
    #  using lists. What’s the compute time difference?

    import numpy as np
    import math
    import time

    # # Create a large array of numbers
    # array_size = 1000000
    # np_array = np.linspace(0, 100, array_size)
    # list_array = list(np_array)

    # # NumPy version
    # start_time_np = time.time()
    # np_result = np.exp(np.sin(np_array))
    # end_time_np = time.time()
    # np_time = end_time_np - start_time_np

    # # List version
    # start_time_list = time.time()
    # list_result = [math.exp(math.sin(x)) for x in list_array]
    # end_time_list = time.time()
    # list_time = end_time_list - start_time_list

    # print(np_time, list_time)

    # Time how long it takes to find all the artist names in the
    # artists dataset that start with the letters a, e, i, o, or u.
    #  Try doing this with a list and with a set for comparison.

    import stopit

    artists = pd.read_csv("data/artists.csv")
    artists['name'] = artists['name'].astype('str').str.lower()
    
    def get_artists_with_high_followers(
        artists, w_list=False):

        with stopit.ThreadingTimeout(60) as context_manager:            
            
            if w_list:

                # with a list
                artist_letters = ["a","e","i","o","u"]
                names = artists[[any(n.startswith(letter) for letter in artist_letters) for n in artists['name']]]

            
            else:
                # with a set
                artist_letters = {"a","e","i","o","u"}
                names = artists[[any(name.startswith(letter) for letter in artist_letters) for name in artists['name']]]

            
            # for name in names['name']:
            #     print(name)


        if context_manager.state == context_manager.EXECUTED:
            print("FINISHED...")

        elif context_manager.state == context_manager.TIMED_OUT:
            print("""DID NOT FINISH
            WITHIN TIME LIMIT""")


    start = time.time()
    get_artists_with_high_followers(
        artists = artists)
    end = time.time()
    print(end - start)

    # Test doing hyperparameter tuning with different values
    #  for n_jobs. You can use the class we created in chapter
    #   4 to handle hyperparamter tuning. Try out the class 
    #  using the artists dataset that was introduced in this chapter.
    #  What’s the compute time for each value you try?

    # ALready tried this b4

