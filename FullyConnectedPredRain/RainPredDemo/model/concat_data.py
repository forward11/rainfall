import os
import json
from read_data import Reader
import pandas as pd


def concat_data():
    """
    To concat raw data to one csv, used for training, validation, and testing.
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as json_file:
        config = json.load(json_file)
    features = config['features_data']
    path = config['directory']
    reader = Reader()
    for year_used_for, years in config['years'].items():
        temp_list = []
        for year in years:
            temp = reader.read_many(year, features)
            temp_list.append(temp)
        temp_frame = pd.concat(temp_list)
        temp_frame.to_csv((os.path.join(path, '{}.csv').format(year_used_for)), index=False)

def add_time(filename):
    """
    add datatime to train,val,test file 
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    periods = pd.to_datetime(df[['year','month','day','hour']])
    df = df.set_index(periods)
    df.drop(labels=['year','month','day','hour'],axis=1, inplace=True)
    #df = df.resample('H').sum()
    df.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)),index='time')

if __name__ == '__main__':
    concat_data()
    add_time('train')
    add_time('val')
    add_time('test')