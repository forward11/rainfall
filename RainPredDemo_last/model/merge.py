import os
import json
import pandas as pd

def merge(filename):
    """
    merge lps and LongDe and JingYuan
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
            config = json.load(json_file)
    df_ld = pd.read_csv(os.path.join(config['directory'],'{}_ld.csv').format(filename))
    df_jy = pd.read_csv(os.path.join(config['directory'],'{}_jy.csv').format(filename))
    df_lps = pd.read_csv(os.path.join(config['directory'],'{}_lps.csv').format(filename))
    df_lps['RPH_ld'] = df_ld['RPH']
    df_lps['RPH_jy'] = df_jy['RPH']
    df_lps.drop(['Unnamed: 0'], axis=1, inplace=True)
    df_lps.to_csv((os.path.join(config['directory'], '{}_resample.csv').format(filename)),index=False)

if __name__ == '__main__':
    merge('train')
    merge('val')
    merge('test')