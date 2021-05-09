import os
import pandas as pd

places = ['wsl','wuwei','yongchang']
for place in places:
    dirs = ['test','val','train']
    for dir in dirs:
        path = "E:\\rainfall\\FullyConnectedPredRain\\wsl\\data\\"+ place+ "\\" +dir
        files = os.listdir(path)
        df_temp = []
        for file in files:
            df = pd.read_csv(os.path.join(path,file))
            df_temp.append(df)
        df_final = pd.concat(df_temp)
        df_final.to_csv("E:\\rainfall\\FullyConnectedPredRain\\wsl\\data\\"+ place + "\\"+dir+"_"+place+".csv",index=False)
