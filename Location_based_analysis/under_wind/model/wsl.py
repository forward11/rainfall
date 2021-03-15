import pandas as pd
import matplotlib.pyplot as plt
from set_plt import config_wsl

data=pd.read_csv(r"E:\rainfall\Location_based_analysis\under_wind\wsl.csv",encoding="ISO-8859-1",index_col=0)
info = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\wsl\StationInfo.xlsx")
station, lon, lat = info['台站号'], info['经度'], info['纬度']
wd_x,wd_y = data['WD_x'],data['WD_y']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#A9A9A9']

for i in range(len(data)):
    plt.figure(figsize=(6.4 * 3, 4.8 * 3))
    # 设置横纵坐标轴
    config_wsl(plt)
    temp = data[i:i+1].values.tolist()[0]

    for j in range(8):
        if temp[j] < 0.5:
            plt.plot(lon[j], lat[j], 'o', c=colors[j], markersize=5, label=station[j])
        else:
            plt.plot(lon[j], lat[j], 'o', c=colors[j], markersize=temp[j]*12, label=station[j])
        if temp[j] == 0.0:
            plt.text(lon[j], lat[j]+0.001, '0', ha='center', va='bottom', fontsize=26)
        elif 0 < temp[j]/5 < 25:
            plt.text(lon[j], lat[j]+0.003*(temp[j]/40), str(round(temp[j]/5, 2)), ha='center', va='bottom', fontsize=26)
        else:
            plt.text(lon[j], lat[j], str(round(temp[j]/5, 2)), ha='center', va='center', fontsize=26, fontweight='bold')


    plt.plot(lon[12], lat[12], '*', c='k', label=station[12], markersize=40)
    plt.arrow(lon[12], lat[12],wd_x[i]*0.001,wd_y[i]*0.001)
    plt.arrow(lon[12], lat[12]+0.005,wd_x[i]*0.001,wd_y[i]*0.001)
    plt.arrow(lon[12], lat[12]-0.005,wd_x[i]*0.001,wd_y[i]*0.001)

    plt.plot(lon[10], lat[10], '*', c='red', label=station[10], markersize=40)
    plt.arrow(lon[10], lat[10],wd_x[i]*0.001,wd_y[i]*0.001)
    plt.arrow(lon[10], lat[10]+0.005,wd_x[i]*0.001,wd_y[i]*0.001)
    plt.arrow(lon[10], lat[10]-0.005,wd_x[i]*0.001,wd_y[i]*0.001)

    index = data[i:i + 1].index.values.tolist()[0]
    plt.savefig('E:\\rainfall\\Location_based_analysis\\under_wind\\plot\\wsl\\' + index + '.png', dpi=150)
    plt.close()
