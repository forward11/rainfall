import os
import json
import pandas as pd 


def process_form(filename):
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
    process_form('train')
    process_form('val')
    process_form('test')