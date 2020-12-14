import os
import json
import pandas as pd 

def drop_zero(filename):
    """
    after resample there are many columns filled zero
    this function is aimed to drop these columns
    """
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df_clear =df.drop(df[df['P']<0.1].index)
    df_clear.set_index(['time'],inplace=True)
    df_clear.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)),index='time')


if __name__ == '__main__':
    drop_zero('train_resample')
    drop_zero('val_resample')
    drop_zero('test_resample')