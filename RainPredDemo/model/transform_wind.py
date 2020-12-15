import os
import json
import numpy
import pandas as pd 

def resample_day(filename):
    with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as json_file:
        config = json.load(json_file)
    df = pd.read_csv(os.path.join(config['directory'],'{}.csv').format(filename))
    df['WV_X'] = numpy.cos( numpy.radians(df['WD'])) * df['WV'] 
    df['WV_Y'] = numpy.sin( numpy.radians(df['WD'])) * df['WV'] 
    df.to_csv((os.path.join(config['directory'], '{}.csv').format(filename)),index='time')

if __name__ == '__main__':
    resample_day('train_resample_MD')
    resample_day('val_resample_MD')
    resample_day('test_resample_MD')