import time
import joblib
from dask.distributed import Client
import dask.dataframe as dd
import dask
import coiled
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":

    cluster = coiled.Cluster(
        name="new",
        n_workers=8,
        worker_memory='8Gib',
        shutdown_on_close=False    
    )


    client = Client(cluster)

    ad_frame = dd.read_csv("data/ads_train_data.csv")


    ad_frame["site_category_28905ebd"] = ad_frame.site_category.map(lambda val: 1 if val == "28905ebd" else 0)

    ad_frame["site_category_50e219e0"] = ad_frame.site_category.map(lambda val: 1 if val == "50e219e0" else 0)

    inputs = ["banner_pos",
            "site_category_28905ebd",
            "site_category_50e219e0"]


    with joblib.parallel_backend("dask"):
        forest = RandomForestClassifier(n_estimators = 100,
            max_depth = 2,
            min_samples_split = 40,
            verbose = 1)
        forest.fit(ad_frame[inputs], ad_frame.click)