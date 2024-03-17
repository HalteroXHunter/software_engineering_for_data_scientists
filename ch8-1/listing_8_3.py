import time
import dask.dataframe as dd

if __name__ == "__main__":
    start = time.time()
    ad_frame = dd.read_parquet(
        "data/ads_train_data_v2.parquet",
        usecols=("click", "banner_pos",
        "site_category"))

    end = time.time()
    print("Read data in ", end - start, " seconds")