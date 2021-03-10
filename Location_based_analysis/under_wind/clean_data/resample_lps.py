import pandas as pd 
import os

files =['RG001','RG002','RG003','RG004','RG005','RG006','RG007','RG008']

for file in files:
    dir = "E:\\rainfall\\Location_based_analysis\\under_wind\\data\\lps\\"+file+'.xlsx'
    df=pd.read_excel(dir)
    df=df[['Date','rain_day']]
    df.set_index('Date', inplace=True)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
    df = df.resample('H').sum()
    df.to_excel(os.path.join("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\lps", '{}_h.xlsx').format(file))
