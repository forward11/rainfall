import pandas as pd 
import os

files =['R0001','R0002','R0003','R0004','R0005','R0006','R0007','R0008']

for file in files:
    dir = "E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl\\"+file+'.xlsx'
    df=pd.read_excel(dir)
    df=df[['Date','rain_day']]
    df.set_index('Date', inplace=True)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
    df = df.resample('H').sum()
    df.to_excel(os.path.join("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl", '{}_h.xlsx').format(file))
