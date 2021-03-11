import pandas as pd
df = pd.read_excel(r"E:\rainfall\Negative_ions\data\wsl\W0004.xlsx")
df= df.drop('Unnamed: 0', 1)
df.set_index('time', inplace=True)
df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.index)))
df = df.resample('M').mean() 
df.to_excel(r"E:\rainfall\Negative_ions\data\wsl\W0004_M.xlsx")