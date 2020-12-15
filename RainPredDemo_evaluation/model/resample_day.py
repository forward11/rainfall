import os
import json
import pandas as pd 

def resample_day(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df=df.rename(columns={'Unnamed: 0':'time'})
    df.set_index('time', inplace=True)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
    df = df[:-2]
    df1 = df.resample('D').sum()
    df1['P'] = df1['P']/24
    df1['T'] = df1['T']/24
    df1['RH'] = df1['RH']//24
    df1['WD'] = df1['WD']//24
    df1['WV'] = df1['WV']/24
    df1 =df1.drop(df1[df1['P']<0.1].index)
    df1.to_csv((os.path.join(config['directory'], '{}_resample.csv').format(filename)),index='time')

if __name__ == '__main__':
    resample_day('train')
    resample_day('val')
    resample_day('test')
