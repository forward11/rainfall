import pandas as pd

df1 = pd.read_excel(r"E:\rainfall\Negative_ions\data\wsl\W0001_D.xlsx")
df2 = pd.read_excel(r"E:\rainfall\Negative_ions\data\wsl\W0002_D.xlsx")
df3 = pd.read_excel(r"E:\rainfall\Negative_ions\data\wsl\W0003_D.xlsx")
df4 = pd.read_excel(r"E:\rainfall\Negative_ions\data\wsl\W0004_D.xlsx")

df = pd.merge(df1, df2, on='time')
df = pd.merge(df, df3, on='time')
df = pd.merge(df, df4, on='time')
col_names=['Date','W1','W2','W3','W4']
df.columns=col_names

df.to_csv(r"E:\rainfall\Negative_ions\data\wsl_D.csv")
