import numpy as np
import pandas as pd

months = ['01','02','04','05','06','07','08','09','10','11','12']
for month in months:
    s1 = "C:\\Users\\11016\\Desktop\\landa_data\\2019\\" + str(month) + "\\Date.txt"
    s2 = "C:\\Users\\11016\\Desktop\\landa_data\\2019\\" + str(month) + "\\Date.csv"
    txt = np.loadtxt(s1)
    df = pd.DataFrame(txt)
    df.columns= ['year','month','day','hour','donnotcare']
    df=df[['year','month','day','hour']]
    #df["year"]=df.apply(lambda x:x+2000,axis=1)
    periods = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df['hour'], freq="H")
    df=df.set_index(periods)
    df.to_csv(s2)