import pandas as pd
import stopit
import time

artists = pd.read_csv("data/artists.csv")

def get_artists_with_high_followers(
    artists):

    with stopit.ThreadingTimeout(60) as context_manager:

        top_percentile = artists.\
            followers.\
            quantile(.999)

        names = artists[
            artists.\
            followers > top_percentile].\
            name

        for name in names:
            print(name)


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