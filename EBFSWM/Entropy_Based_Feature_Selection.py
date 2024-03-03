import pandas as pd
import multiprocessing
import numpy as np
from datetime import datetime


df = pd.read_csv("Kaggle_Customer_Churn_Prediction.csv")
all_feats = df.columns.to_list()
all_feats.remove('churn')
all_feats.remove("customer_id")
target_col = "churn"

X = df[all_feats]
y = df[target_col]


def entropy(y):
    probs = [] # Probabilities of each class label
    for c in set(y): # Set gets a unique set of values. We're iterating over each value
        num_same_class = sum(y == c)  # Remember that true == 1, so we can sum.
        p = num_same_class / len(y) # Probability of this class label
        probs.append(p)
    return np.sum(-p * np.log2(p) for p in probs)


# let's write some entropy functions
def class_probability(feature, y):
    """Calculates the proportional length of each value in the set of instances"""
    # This is doc string, used for documentation
    probs = []
    for value in set(feature):
        select = feature == value # Split by feature value into two classes
        y_new = y[select]         # Those that exist in this class are now in y_new
        probs.append(float(len(y_new))/len(X))  # Convert to float, because ints don't divide well
    return probs



def class_entropy(feature, y):
    """Calculates the entropy for each value in the set of instances"""
    ents = []
    for value in set(feature):
        select = feature == value # Split by feature value into two classes
        y_new = y[select]         # Those that exist in this class are now in y_new
        ents.append(entropy(y_new))
    return ents

def proportionate_class_entropy(feature, y):
    """Calculatates the weighted proportional entropy for a feature when splitting on all values"""
    probs = class_probability(feature, y)
    ents = class_entropy(feature, y)
    return np.sum(np.multiply(probs, ents))


result = []
res = {}

def finalized_entropy(feature):
    new_entropy = proportionate_class_entropy(X[feature],y)
    try:
        res[feature] = (entropy(y) - new_entropy)
    except KeyError:
        print(feature)
    return res


def entropy_with_parallel(feature ,result_queue):
# create a multiprocessing Queue to store the results
    result =  finalized_entropy(feature)
    result_queue.put(result)


def entropy_with_multiprocessing(features):
    result_queue = multiprocessing.Queue()
    
    processes = []
    for col in features:
        process = multiprocessing.Process(target = entropy_with_parallel, args = (col, result_queue))
        processes.append(process)
        process.start()

    ## wait for all processes finished
    for process in processes:
        process.join()

    ## collect results from queue
    for _ in range(len(processes)):
        result.append(result_queue.get())
    
    return result


start_time = datetime.now()
if __name__ == "__main__":
    numbers_to_calc = all_feats
 
    iv_results = entropy_with_multiprocessing(numbers_to_calc)

    end_time = datetime.now()
    print("Information Value", iv_results,(end_time-start_time))
