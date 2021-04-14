import numpy as np
import pandas as pd



txt = np.loadtxt("C:\\Users\\11016\\Desktop\\landa_data\\2020\\12\\Data.txt")
df = pd.DataFrame(txt)
df.columns= ['year','month','day','hour','donnotcare']
df=df[['year','month','day','hour']]
#df["year"]=df.apply(lambda x:x+2000,axis=1)
periods = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df['hour'], freq="H")
df=df.set_index(periods)
df.to_csv('C:\\Users\\11016\\Desktop\\landa_data\\2020\\12\\Date.csv')