import pandas as pd

wsl_path = "E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl"
df1 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0001.xlsx")
df2 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0002.xlsx")
df3 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0003.xlsx")
df4 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0004.xlsx")
df5 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0005.xlsx")
df6 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0006.xlsx")
df7 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0007.xlsx")
df8 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\R0008.xlsx")
df9 = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\wind.xlsx")
df = pd.merge(df1, df2, on='Date')
df = pd.merge(df, df3, on='Date')
df = pd.merge(df, df4, on='Date')
df = pd.merge(df, df5, on='Date')
df = pd.merge(df, df6, on='Date')
df = pd.merge(df, df7, on='Date')
df = pd.merge(df, df8, on='Date')
df = pd.merge(df, df9, on='Date')
col_names=['Date','R1','R2','R3','R4','R5','R6','R7','R8','WD','WV']
df.columns=col_names
df.to_csv("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\data_wsl.csv")
