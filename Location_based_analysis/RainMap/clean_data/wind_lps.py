import pandas as pd 
import os

directories =['WG005','WG006','WG007']

for directory in directories:
    dir = "C:\\Users\\11016\\Desktop\\data\\lps\\"+directory
    filenames = os.listdir(dir)
    index = 0
    temp_df =[]
    print(directory)
    for file in filenames:
        print(index)
        df = pd.read_excel(os.path.join(dir,file))
        df['时间']=df['时间'].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S')
        df['Date'],df['Time'] = df['时间'].apply(lambda x:x.date()), df['时间'].apply(lambda x:x.time())
        df= df[['Date','Time','风向(°)','风速(m/s)']]
        df.rename(columns={"风向(°)":'WD',"风速(m/s)":'WV'}, inplace=True)
        temp_df.append(df)
        index = index +1 
    df=pd.concat(temp_df)
    df.to_excel(os.path.join("C:\\Users\\11016\\Desktop\\data\\lps", '{}.xlsx').format(directory))