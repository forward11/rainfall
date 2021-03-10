import pandas as pd 
import os

files =['WG005','WG006','WG007']

for file in files:  
    print("1")
    dir = "E:\\rainfall\\Location_based_analysis\\under_wind\\data\\lps\\"+ file +".xlsx"
    df=pd.read_excel(dir)
    df=df[['Date','WD','WV']]
    df.set_index('Date', inplace=True)
    df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
    df = df.resample('H').mean()
    df.to_excel(os.path.join("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\lps", '{}_h.xlsx').format(file))