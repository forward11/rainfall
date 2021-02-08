import os
import json
from read_data import Reader
import pandas as pd

def merge(filename):
    """
    merge lps and ld and jy, generate train,val,test
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as json_file:
        config = json.load(json_file)
    df_lps = pd.read_csv(os.path.join(config['directory'],'{}_lps.csv').format(filename))
    df_ld = pd.read_csv(os.path.join(config['directory'],'{}_ld.csv').format(filename))
    df_jy = pd.read_csv(os.path.join(config['directory'],'{}_jy.csv').format(filename))
    df_lps = df_lps.drop(df_lps[df_lps['RPH']>99999].index)
    df_ld = df_ld.drop(df_ld[df_ld['RPH_ld']>99999].index)
    df_jy = df_jy.drop(df_jy[df_jy['RPH_jy']>99999].index)
    df_lps = df_lps.drop(['Unnamed: 0'],axis=1)
    df_ld = df_ld.drop(['time'],axis=1)
    df_jy = df_jy.drop(['time'],axis=1)
    data = pd.merge(df_lps, df_ld, on=['year','month','day'])
    data = pd.merge(data, df_jy, on=['year','month','day'])
    data.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)))
    print(data.mean())

if __name__ == '__main__':
    merge('train')
    merge('val')
    merge('test')

