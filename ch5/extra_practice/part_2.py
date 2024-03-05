# Using the Spotify dataset file dataset-of-00s.csv
# (from the zip file you downloaded in step 1), can you
# monitor the progress of tuning the hyperparameters
# for a random forest model? The label of the dataset is in the target column.
from stopit import threading_timeoutable as timeoutable
import stopit
import sys
import os
from tqdm import tqdm
from pathlib import Path
import pandas as pd
# sys.path.append('C:\\Users\\IanBorregoObrador\\Desktop\\formation\\software_engineering\\software_engineering_for_data_scientists\\')

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from ch5.dataset_model_with_methods import Dataset

spty_path = Path('data\spotify\dataset-of-00s.csv')
df = pd.read_csv(spty_path)
print("done")
exit()


numerical_df = df.select_dtypes(include=['int64', 'float64'])
numerical_df.drop(columns='target',inplace=True)
numerical_columns_list = numerical_df.columns.tolist()


customer_obj = Dataset(feature_list = numerical_columns_list,
                    file_name = "software_engineering_for_data_scientists\data\spotify\dataset-of-00s.csv",
                    label = "target"                    
                    )

print(customer_obj.train_features,customer_obj.train_labels) 


parameters = {"max_depth":range(2, 8),
            "min_samples_leaf": range(5, 55, 5),
            "min_samples_split": range(10, 110, 5),
            "max_features": [2, 3],
            "n_estimators": [100, 150, 200, 250, 300, 350, 400]}


clf = RandomizedSearchCV(GradientBoostingClassifier(),
                        parameters,
                        n_jobs=1,
                        scoring = "roc_auc",
                        n_iter = 10,
                        random_state = 0,
                        verbose = 2)

# Can you set a timeout of 5 minutes for the hyperparameter tuning process using a with block?
# Can you repeat #3 using a decorator instead?
with stopit.ThreadingTimeout(60*5) as context_manager:
    clf.fit(customer_obj.train_features, customer_obj.train_labels)
    
if context_manager.state == context_manager.EXECUTED:
    print("FINISHED TRAINING MODEL...")

# Did code timeout?
elif context_manager.state == context_manager.TIMED_OUT:
    
    # or raise an error if desired
    raise AssertionError("DID NOT FINISH MODEL TRAINING WITHIN TIME LIMIT")


