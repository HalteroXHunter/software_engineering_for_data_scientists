

import pandas as pd
from tqdm import tqdm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class Chunk_pipeline:

    def __init__(self, filename: str, test_filename:str, label: str, 
                 numeric_signals: list, cat_signals: list,
                 chunksize: int):
        self.filename = filename
        self.test_filename = test_filename
        self.label = label
        self.numeric_signals = numeric_signals
        self.cat_signals = cat_signals
        self.keep_cols = [self.label] + self.numeric_signals + self.cat_signals
        self.chunksize = chunksize
    
    def get_chunks(self):
        return pd.read_csv(self.filename, 
                            chunksize=self.chunksize,
                            usecols = self.keep_cols)
    
    @profile
    def train_model(self):
        
        data_chunks = self.get_chunks()
      
        sgd_model = SGDClassifier(random_state = 0,
                                  loss = "log_loss")
        
        
        keep_fields = []
        for frame in tqdm(data_chunks):
    
            features = pd.concat([frame[self.numeric_signals], 
                                  pd.get_dummies(frame[self.cat_signals])],
                                 axis = 1)
            
            
            if not keep_fields:
                
                for signal in self.cat_signals:
                    top_categories = set(frame[signal].value_counts().\
                                      head().index.tolist())
                
                
                    fields = [field for field in features.columns.tolist() 
                              if field in top_categories]
                
                    
                    keep_fields.extend(fields)
                
                keep_fields.extend(self.numeric_signals)
            
            
            sgd_model.partial_fit(features[keep_fields], 
                                  frame[self.label], 
                                  classes = (0, 1))
    
    
        self.sgd_model = sgd_model
        
    @profile    
    def evaluate_model(self):
        
        test_chunks = pd.read_csv(self.test_filename, chunksize=self.chunksize, usecols=self.keep_cols)
                
        accuracies = []
        precisions = []
        recalls = []
        f1_scores = []
        
        for frame in tqdm(test_chunks):
            features = pd.concat([frame[self.numeric_signals], 
                                  pd.get_dummies(frame[self.cat_signals])], 
                                 axis=1)
            
            # Filter the features to keep only the fields used in training
            keep_fields = [field for field in features.columns if field in self.sgd_model.feature_names_in_]
            features = features[keep_fields]
            
            true_labels = frame[self.label]
            predictions = self.sgd_model.predict(features)
            
            accuracies.append(accuracy_score(true_labels, predictions))
            precisions.append(precision_score(true_labels, predictions))
            recalls.append(recall_score(true_labels, predictions))
            f1_scores.append(f1_score(true_labels, predictions))
        
        print(f"Average Accuracy: {sum(accuracies) / len(accuracies)}")
        print(f"Average Precision: {sum(precisions) / len(precisions)}")
        print(f"Average Recall: {sum(recalls) / len(recalls)}")
        print(f"Average F1 Score: {sum(f1_scores) / len(f1_scores)}")        
        
        
pipeline = Chunk_pipeline(filename = "data/ads_train_data_v1.csv",
                          test_filename = "data/ads_test_data_v1.csv",
                          label = "click",
                          numeric_signals=["banner_pos"],
                          cat_signals=["site_category"],
                          chunksize=1000000)

pipeline.train_model()
pipeline.evaluate_model()


