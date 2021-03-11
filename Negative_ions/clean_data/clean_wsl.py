import pandas as pd 
import os

directories =['W0001','W0002','W0003','W0004']

for directory in directories:
    dir = "E:\\rainfall\\Negative_ions\\data\\wsl\\"+directory
    filenames = os.listdir(dir)
    index = 0
    temp_df =[]
    print(directory)
    for file in filenames:
        print(index)
        df = pd.read_excel(os.path.join(dir,file))
        df['时间']=df['时间'].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S')
        df.rename(columns={"时间":'time'}, inplace=True)
        df= df[['time','负离子数']]
        temp_df.append(df)
        index = index +1 
    df=pd.concat(temp_df)
    df.to_excel(os.path.join("E:\\rainfall\\Negative_ions\\data\\wsl", '{}.xlsx').format(directory))