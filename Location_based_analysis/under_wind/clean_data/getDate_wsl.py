import pandas as pd 
import os

files =['R0001','R0002','R0003','R0004','R0005','R0006','R0007','R0008']

for file in files:
    dir = "E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl\\"+file+'.xlsx'
    df= pd.read_excel(dir)
    df['Date']=df['Date'].apply(lambda x: x.strftime("%Y-%m-%d"))
    df['date']= pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df=df[['date','rain_day']]
    df.rename(columns={"date":'Date'},inplace=True)
    df.to_excel(os.path.join("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\wsl", '{}_1.xlsx').format(file))
