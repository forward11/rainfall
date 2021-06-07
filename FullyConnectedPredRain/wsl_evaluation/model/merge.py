import os
import json
from read_data import Reader
import pandas as pd

def merge(filename):
    """
    generate train,val,test
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'all_data.csv'))
    train_df=df[:927]   # 2019-06-30
    val_df = df[927:1292]  #2020-06-30
    test_df=df[1292:]   #2020-10-31
    train_df.to_csv(os.path.join(config['directory'],'train.csv'))
    val_df.to_csv(os.path.join(config['directory'],'val.csv'))
    test_df.to_csv(os.path.join(config['directory'],'test.csv'))

if __name__ == '__main__': 
    merge('train')
    merge('val')
    merge('test')

