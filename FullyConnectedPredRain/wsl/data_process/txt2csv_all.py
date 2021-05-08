import numpy as np
import pandas as pd
import os

year= '2019'
months = ['01','02','04','05','06','07','08','09','10','11','12']

for month in months:
    date_now = year + month
    path = "C:\\Users\\11016\\Desktop\\landa_data\\"+year+"\\"+month
    path_csv = "C:\\Users\\11016\\Desktop\\landa_data\\"+year
    

    txt = np.loadtxt(os.path.join(path,'wushaoling.txt'))
    data = pd.DataFrame(txt)
    data.columns = ['stationID','lon','lat','altitude','siteLevel','totalCloud','WD','WV','airPressure','Transformation_3h',
    'pastWeather1','pastWeather2','rainfall_6h','lowCloudiness','lowCloudCover','lowCloudHigh','dewPoint','visibility','currentWeather','temperature',
    'midCloudiness','highCloudiness','flag1','flag2','temperatureChange_24h','transformer_24h']
    time = pd.read_csv(os.path.join(path,'Date.csv'))
    time = time.rename(columns={'Unnamed: 0':'time'})
    data[['time','year','month','day','hour']]=time[['time','year','month','day','hour']]
    data.to_csv(os.path.join(path_csv,'wsl_{}.csv').format(date_now))

    txt = np.loadtxt(os.path.join(path,'wuwei.txt'))
    data = pd.DataFrame(txt)
    data.columns = ['stationID','lon','lat','altitude','siteLevel','totalCloud','WD','WV','airPressure','Transformation_3h',
    'pastWeather1','pastWeather2','rainfall_6h','lowCloudiness','lowCloudCover','lowCloudHigh','dewPoint','visibility','currentWeather','temperature',
    'lowCloudiness','highCloudiness','flag1','flag2','temperatureChange_24h','transformer_24h']
    time = pd.read_csv(os.path.join(path,'Date.csv'))
    time = time.rename(columns={'Unnamed: 0':'time'})
    data[['time','year','month','day','hour']]=time[['time','year','month','day','hour']]
    data.to_csv(os.path.join(path_csv,'ww_{}.csv').format(date_now))

    txt = np.loadtxt(os.path.join(path,'yongchang.txt'))
    data = pd.DataFrame(txt)
    data.columns = ['stationID','lon','lat','altitude','siteLevel','totalCloud','WD','WV','airPressure','Transformation_3h',
    'pastWeather1','pastWeather2','rainfall_6h','lowCloudiness','lowCloudCover','lowCloudHigh','dewPoint','visibility','currentWeather','temperature',
    'lowCloudiness','highCloudiness','flag1','flag2','temperatureChange_24h','transformer_24h']
    time = pd.read_csv(os.path.join(path,'Date.csv'))
    time = time.rename(columns={'Unnamed: 0':'time'})
    data[['time','year','month','day','hour']]=time[['time','year','month','day','hour']]
    data.to_csv(os.path.join(path_csv,'yc_{}.csv').format(date_now))