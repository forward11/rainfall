import os
import pandas as pd

path = "E:\\rainfall\\FullyConnectedPredRain\\wsl\\data\\yongchang\\2020"
files = os.listdir(path)
df_temp = []
for file in files:
    df = pd.read_csv(os.path.join(path,file))
    df_temp.append(df)
df_final = pd.concat(df_temp)
df_final.to_csv("E:\\rainfall\\FullyConnectedPredRain\\wsl\\data\\yongchang\\2020_yc.csv")
