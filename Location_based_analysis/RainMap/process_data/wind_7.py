import pandas as pd 
import os


dir = "C:\\Users\\11016\\Desktop\\wind_7\\"
index = 0
filenames = os.listdir(dir)
temp_df =[]
for file in filenames:
    print(index)
    df = pd.read_excel(os.path.join(dir,file))
    
    df = df.groupby(['Date'])['WD'].mean()
    df = df.groupby(['Date'])['WV'].mean()
    result[lambda df: df.columns[files.index(file)-1]] = rain_sum / rain_count * 1440
    temp_df.append(df)
    index = index +1 
    df.to_excel(os.path.join("C:\\Users\\11016\\Desktop\\lps_7", '{}_M.xlsx').format(file))
