import time
import joblib
from dask.distributed import Client
import dask.dataframe as dd
import dask
import coiled
from sklearn.ensemble import RandomForestClassifier
from dask_ml.model_selection import train_test_split

if __name__ == "__main__":

    keep = ["dask", "coiled", "xarray", "pandas", "numpy", "sklearn", "joblib"]


    cluster = coiled.Cluster(
        name="new",
        n_workers=8,
        worker_memory='8Gib',
        shutdown_on_close=False,
        package_sync = keep
    )    

    client = Client(cluster)

    ad_frame = dd.read_csv("data/ads_train_data.csv")
    # ad_frame = ad_frame.head(1000)


    ad_frame["site_category_28905ebd"] = ad_frame.site_category.map(
            lambda val: 1 if val == "28905ebd" else (0 if val is not None else None),
            meta=('site_category', 'int')
        )

    ad_frame["site_category_50e219e0"] = ad_frame.site_category.map(
        lambda val: 1 if val == "50e219e0" else (0 if val is not None else None),
        meta=('site_category', 'int'))

    inputs = ["banner_pos",
            "site_category_28905ebd",
            "site_category_50e219e0"]
    
    train, test = train_test_split(ad_frame,
        train_size = 0.7,
        shuffle = True,
        random_state = 0)

    with joblib.parallel_backend("dask"):
        forest = RandomForestClassifier(n_estimators = 100,
            max_depth = 2,
            min_samples_split = 40,
            verbose = 1)
        forest.fit(train[inputs],
            train.click)