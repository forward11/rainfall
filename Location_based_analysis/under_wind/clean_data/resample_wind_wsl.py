import pandas as pd 

dir = "E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl\\wind.xlsx"
df=pd.read_excel(dir)
df=df[['Date','WD','WV']]
df.set_index('Date', inplace=True)
df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
df = df.resample('H').mean()
df.to_excel("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl\\wind_h.xlsx")