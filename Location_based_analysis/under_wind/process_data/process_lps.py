import pandas as pd

df1 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG001.xlsx")
df2 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG002.xlsx")
df3 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG003.xlsx")
df4 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG004.xlsx")
df5 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG005.xlsx")
df6 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG006.xlsx")
df7 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG007.xlsx")
df8 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\RG008.xlsx")
df9 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\WG005.xlsx")
df10 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\WG006.xlsx")
df11 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\WG007.xlsx")
df = pd.merge(df1, df2, on='Date')
df = pd.merge(df, df3, on='Date')
df = pd.merge(df, df4, on='Date')
df = pd.merge(df, df5, on='Date')
df = pd.merge(df, df6, on='Date')
df = pd.merge(df, df7, on='Date')
df = pd.merge(df, df8, on='Date')
df = pd.merge(df, df9, on='Date')
df = pd.merge(df, df10, on='Date')
df = pd.merge(df, df11, on='Date')
col_names=['Date','R1','R2','R3','R4','R5','R6','R7','R8','WD5','WV5','WD6','WV6','WD7','WV7']
df['WD5']=df['WD5']//22
df.columns=col_names
df.to_csv("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\data_lps.csv")
