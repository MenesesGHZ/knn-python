import os
import math
from knn import KNN
from ..reader import read_dataset

def run():
    # Reading dataset
    data_path = os.path.join(os.path.dirname(__file__),"iris.csv")
    x_train,y_train,x_test,y_test = read_dataset(data_path)
    
    # Loading Model
    euclidean_norm = lambda v1,v2: math.sqrt(sum((v1-v2)**2))
    knn_model = KNN(x_train,y_train,norm=euclidean_norm,k=5)
    
    # Predicting
    pred = knn_model.predict(x_test)
    


