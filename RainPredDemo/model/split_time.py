import os
import json
import pandas as pd 

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
    df1.to_csv((os.path.join(config['directory'], '{}_MD.csv').format(filename)),index=False)


if __name__ == '__main__':
    split_time('train_resample')
    split_time('val_resample')
    split_time('test_resample')