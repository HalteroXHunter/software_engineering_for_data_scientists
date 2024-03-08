

import pandas as pd

ad_data = pd.read_csv("data/ads_train_data_v1.csv", chunksize=1000000)

ad_frame = ad_data.get_chunk()

print(ad_frame.memory_usage(deep = True))