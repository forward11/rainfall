import pandas as pd 
import os

files =['RG001','RG002','RG003','RG004','RG005','RG006','RG007','RG008']

for file in files:
    dir = "C:\\Users\\11016\\Desktop\\output_data\\lps\\"+file+'.xlsx'
    df= pd.read_excel(dir)
    df['Date']=df['Date'].apply(lambda x: x.strftime("%Y-%m-%d"))
    df['date']= pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df=df[['date','rain_day']]
    df.rename(columns={"date":'Date'},inplace=True)
    df.to_excel(os.path.join("E:\\rainfall\\Location_based_analysis\\under_wind\\data\\lps", '{}.xlsx').format(file))
    print("1")