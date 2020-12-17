import os
import json
import numpy
import pandas as pd 

def resample_month(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df=df.rename(columns={'Unnamed: 0':'time'})
    df.set_index('time', inplace=True)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
    df1 = df.resample('M').sum()
    df1 =df1.drop(df1[df1['RPH']<0.1].index)
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

def delete_month(filename):
    """
    keep months with liupanshan
    """
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
            config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df =df.drop(df[df['time']=='2008-04-30'].index)
    df =df.drop(df[df['time']=='2008-05-31'].index)
    df =df.drop(df[df['time']=='2009-04-30'].index)
    df =df.drop(df[df['time']=='2009-05-31'].index)
    df =df.drop(df[df['time']=='2010-05-31'].index)
    df =df.drop(df[df['time']=='2011-05-31'].index)
    df =df.drop(df[df['time']=='2011-05-31'].index)
    df =df.drop(df[df['time']=='2012-04-30'].index)
    df =df.drop(df[df['time']=='2012-05-31'].index)
    df =df.drop(df[df['time']=='2013-05-31'].index)
    df =df.drop(df[df['time']=='2015-01-31'].index)
    df =df.drop(df[df['time']=='2015-02-28'].index)
    df =df.drop(df[df['time']=='2015-03-31'].index)
    df =df.drop(df[df['time']=='2018-12-31'].index)
    df.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)),index=False)


if __name__ == '__main__':
    resample_month('train')
    resample_month('val')
    resample_month('test')
    split_time('train_resample')
    split_time('val_resample')
    split_time('test_resample')
    delete_month('train_resample')
    delete_month('val_resample')
    delete_month('test_resample')

