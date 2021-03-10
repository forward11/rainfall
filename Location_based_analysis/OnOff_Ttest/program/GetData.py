import pandas as pd 
import os

directories =['R0001','R0002','R0003','R0004','R0005','R0006','R0007','R0008']

for directory in directories:
    dir = "C:\\Users\\11016\\Desktop\\output_data\\wsl_19\\" + directory
    filenames = os.listdir(dir)
    index = 0
    temp_df =[]
    print(directory)
    for file in filenames:
        print(index)
        df = pd.read_excel(os.path.join(dir,file))
        df['时间']=df['时间'].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S')
        df['Date'],df['Time'] = df['时间'].apply(lambda x:x.date()), df['时间'].apply(lambda x:x.time())
        df= df[['Date','Time','分钟雨量(mm)']]
        df.rename(columns={"分钟雨量(mm)":'rain_day'}, inplace=True)
        temp_df.append(df)
        index = index +1 
    df=pd.concat(temp_df)
    df.to_excel(os.path.join("C:\\Users\\11016\\Desktop\\output_data\\wsl_19", '{}.xlsx').format(directory))