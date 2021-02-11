import numpy as np
import pandas as pd

def calculate_expected_value(collection_stamp):
    #initialize stamps size
    trials = 0
    collection_stamp=collection_stamp
    
    for i in range(collection_stamp, 0, -1):
        trials = trials + (1/(i/collection_stamp))
    iterations = 200
    df = pd.DataFrame()
    df['iteration'] = range(1,iterations+1)
    df['average_num_trials_required'] = None
    for i in range(0, iterations):
        full_set = set(range(0,collection_stamp))
        current_set = set([])
        total_collection = 0
        while(current_set != full_set):
            total_collection = total_collection+1
            random_n= (np.random.randint(low=0, high=collection_stamp, size=1)).item()
            update_set = list(current_set)
            update_set.append(random_n)
            current_set = set(update_set)
            del random_n, update_set
        
        if(i+1 == 1):
            df.loc[df['iteration']==i+1, 'average_num_trials_required'] = total_collection
        else:
            df.loc[df['iteration']==i+1, 'average_num_trials_required'] = float(((df.loc[df['iteration']==i, 'average_num_trials_required']*i) + total_collection)/(i+1))
    return df['average_num_trials_required'][i]

print(calculate_expected_value(6))