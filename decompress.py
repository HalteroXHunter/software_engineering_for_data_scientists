import gzip
import pandas as pd

# Input .gz file
gz_file = 'data/ads_test_data.gz'
# Output file (uncompressed)
csv_file = 'data/ads_test_data_v1.csv'
parquet_file = 'data/ads_test_data_v2.parquet'

# Decompress .gz file and load into a DataFrame
with gzip.open(gz_file, 'rt', encoding='utf-8') as f:
    df = pd.read_csv(f)

# Save DataFrame to CSV
df.to_csv(csv_file, index=False)

# Save DataFrame to Parquet
df.to_parquet(parquet_file, index=False)