import pandas as pd

df1 = pd.read_excel(r"E:\rainfall\Negative_ions\data\lps\WG005_M.xlsx")
df2 = pd.read_excel(r"E:\rainfall\Negative_ions\data\lps\WG006_M.xlsx")
df3 = pd.read_excel(r"E:\rainfall\Negative_ions\data\lps\WG007_M.xlsx")

df = pd.merge(df1, df2, on='time')
df = pd.merge(df, df3, on='time')
col_names=['Date','W5','W6','W7']
df.columns=col_names

df.to_csv(r"E:\rainfall\Negative_ions\data\lps_M.csv")
