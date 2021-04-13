import numpy as np
import pandas as pd
 
txt = np.loadtxt("C:\\Users\\11016\\Desktop\\landa_data\\2018\\01\\wushaoling.txt")
data = pd.DataFrame(txt)
data.columns = ['stationID','lon','lat','altitude','siteLevel','totalCloud','WD','WV','airPressure','Transformation_3h',
'pastWeather1','pastWeather2','rainfall_6h','lowCloudiness','lowCloudCover','lowCloudHigh','dewPoint','visibility','currentWeather','temperature',
'lowCloudiness','highCloudiness','flag1','flag2','temperatureChange_24h','transformer_24h']

time = pd.read_csv("C:\\Users\\11016\\Desktop\\landa_data\\2018\\01\\Date.csv")
time = time.rename(columns={'Unnamed: 0':'time'})

data[['time','year','month','day','hour']]=time[['time','year','month','day','hour']]
data.to_csv("C:\\Users\\11016\\Desktop\\landa_data\\2018\\01\\wushaoling.csv")