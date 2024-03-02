import pandas as pd 

def data_processing(path_to_data):
    # import data
    df = pd.read_csv(path_to_data)

    # further processing steps...

    return df