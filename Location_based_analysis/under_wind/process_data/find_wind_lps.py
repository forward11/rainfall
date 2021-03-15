import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\rainfall\Location_based_analysis\under_wind\data\data_lps.csv")
df = df[['Date','WD7','WV7']]
df.replace(np.nan, 0, inplace=True) 
df.replace(np.inf, 0, inplace=True)
df['WD7']=df['WD7'].astype(int)

WD = df['WD7'].values
WV = df['WV7'].values
most_WD=[]
result=[]

for x in range(112):
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

df.to_csv(r"E:\rainfall\Location_based_analysis\under_wind\lps_7.csv")