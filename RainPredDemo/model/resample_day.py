import os
import json
import numpy
import pandas as pd 

def resample_day(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df=df.rename(columns={'Unnamed: 0':'time'})
    df.set_index('time', inplace=True)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
    if filename!='val':
        df=df[:-2]
    df1 = df.resample('D').sum()
    df1['P'] = df1['P']/24
    df1['T'] = df1['T']/24
    df1['RH'] = df1['RH']//24
    df1['WD'] = df1['WD']//24
    df1['WV'] = df1['WV']/24
    df1 =df1.drop(df1[df1['P']<0.1].index)
    df1.to_csv((os.path.join(config['directory'], '{}_resample.csv').format(filename)),index='time')

def DateSplit(df):
    temp_df = df['time'].str.split('-',expand=True)
    temp_df.columns = ["year","month","day"]
    df = pd.concat([df,temp_df],axis=1)
    return df

def split_time(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
            config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df1 = DateSplit(df)
    df1.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)),index=False)

def transform_wind(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df['WV_X'] = numpy.cos( numpy.radians(df['WD'])) * df['WV'] 
    df['WV_Y'] = numpy.sin( numpy.radians(df['WD'])) * df['WV'] 
    df.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)),index='time')


if __name__ == '__main__':
    resample_day('train')
    resample_day('val')
    resample_day('test')
    split_time('train_resample')
    split_time('val_resample')
    split_time('test_resample')
    transform_wind('train_resample')
    transform_wind('val_resample')
    transform_wind('test_resample')
