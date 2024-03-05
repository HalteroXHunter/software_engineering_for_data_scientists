
from stopit import threading_timeoutable as timeoutable
from pathlib import Path
import pandas as pd

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from ch5.dataset_model_with_methods import Dataset

spty_path = Path('software_engineering_for_data_scientists\data\spotify\dataset-of-00s.csv')
df = pd.read_csv(spty_path)

numerical_df = df.select_dtypes(include=['int64', 'float64'])
numerical_df.drop(columns='target',inplace=True)
numerical_columns_list = numerical_df.columns.tolist()

customer_obj = Dataset(feature_list = numerical_columns_list,
                    file_name = "software_engineering_for_data_scientists\data\spotify\dataset-of-00s.csv",
                    label = "target"                    
                    )

@timeoutable()
def train_model(features, labels):

    forest_model = RandomForestClassifier(verbose=1,n_estimators = 500).fit(features,
                                                                  labels)

    return forest_model

forest_ml = train_model(
    timeout=60*3,
    features=customer_obj.train_features,
    labels=customer_obj.train_labels
    )

if forest_ml:
    print("FINISHED TRAINING MODEL...")

# Did code timeout?
else:

    raise AssertionError("DID NOT FINISH MODEL TRAINING WITHIN TIME LIMIT")

