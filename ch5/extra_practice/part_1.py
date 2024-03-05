# Download the Spotify hit zip file from Kaggle 
# (https://www.kaggle.com/datasets/theoverman/the-spotify-hit-predictor-dataset).
# This file contains a collection of datasets across
# multiple song-release decades (90s, 00s, 10s, etc).
# Use tqdm to monitor the progress of reading each in as part of a loop.

import sys
import os
from tqdm import tqdm
from pathlib import Path

import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spty_path = Path('software_engineering_for_data_scientists\data\spotify')
spty_files = os.listdir(spty_path)

all_ds = []

for file in tqdm(spty_files):
    final_path = spty_path / file
    all_ds.append(pd.read_csv(final_path))
