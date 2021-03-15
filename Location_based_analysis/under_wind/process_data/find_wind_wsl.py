import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\rainfall\Location_based_analysis\under_wind\data\data_wsl.csv")
df = df[['Date','WD','WV']]
df.replace(np.nan, 0, inplace=True) 
df.replace(np.inf, 0, inplace=True)
df['WD']=df['WD'].astype(int)

WD = df['WD'].values
WV = df['WV'].values
most_WD=[]
result=[]
for x in range(83):
    temp_WD =WD[:24]
    temp_WV = WV[:24]
    WD=WD[24:]
    WV=WV[24:]
    value_arr=[]
    most=np.argmax(np.bincount(temp_WD))
    most_WD.append(most)
    for i in range(24):
        if temp_WD[i]==most:
            value_arr.append(temp_WV[i])
    result.append( sum(value_arr)/len(value_arr) )
df['WV_d'] = pd.Series(result)
df['WD_d'] = pd.Series(most_WD)
df.to_csv(r"E:\rainfall\Location_based_analysis\under_wind\wsl.csv")