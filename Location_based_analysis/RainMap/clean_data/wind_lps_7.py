import pandas as pd 
import os


dir = "C:\\Users\\11016\\Desktop\\wind_7\\"
filenames = os.listdir(dir)
for file in filenames:
    df = pd.read_excel(os.path.join(dir,file))
    df['时间']=df['时间'].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S')
    df['Date'],df['Time'] = df['时间'].apply(lambda x:x.date()), df['时间'].apply(lambda x:x.time())
    df= df[['Date','Time','风向(°)','风速(m/s)']]
    df.rename(columns={"风向(°)":'WD',"风速(m/s)":'WV'}, inplace=True)
    df.to_excel(os.path.join("C:\\Users\\11016\\Desktop\\wind_7", '{}_M.xlsx').format(file))