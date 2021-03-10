import pandas as pd 

df = pd.read_csv("C:\\Users\\11016\\Desktop\\output_data\\wsl_19\\data\\RainGauge19_wsl.csv")
df['Unnamed: 0']=df['Unnamed: 0'].apply(pd.to_datetime,format='%Y-%m-%d')
df.rename(columns = {"Unnamed: 0": "time"},inplace=True)
df.set_index('time', inplace=True)
df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
df = df.resample('M').sum()
df.to_csv("C:\\Users\\11016\\Desktop\\output_data\\wsl_19\\data\\RainGauge19_wsl_M.csv")