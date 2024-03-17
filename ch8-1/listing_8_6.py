import time
import dask.dataframe as dd
from dask.distributed import LocalCluster, Client


if __name__ == "__main__":
    cluster = LocalCluster()
    client = Client(cluster)

    start = time.time()
    ad_frame = dd.read_parquet(
        "data/ads_train_data_v2.parquet",
        columns=("click", "banner_pos",
        "site_category"))


    print(ad_frame[[
        "click", "site_category"]].\
        groupby("site_category").\
        mean().\
        compute())

    end = time.time()

    print("Time to execute code: ",
        end - start)