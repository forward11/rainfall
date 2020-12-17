import os
import json
import numpy
import pandas as pd

def add_guyuan(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    
    df1.to_csv((os.path.join(config['directory'], '{}_resample.csv').format(filename)),index='time')

if __name__ == '__main__':
    add_guyuan('train_reasample')
    add_guyuan('val_resample')
    add_guyuan('test_resample')