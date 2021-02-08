import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from set_plt import config_wsl

rain = pd.read_csv('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\RainGauge_wsl.csv', index_col=0)  
info = pd.read_excel('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\wsl\\StationInfo.xlsx')
wind = pd.read_excel('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\wsl\\wind.xlsx', index_col=0)
data = rain.copy(deep=False)
data = data[1:] * 5
info = info[1:].reset_index()
station, lon, lat = info['台站号'], info['经度'], info['纬度']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#A9A9A9']

for i in range(len(data)):
    plt.figure(figsize=(6.4 * 3, 4.8 * 3))
    # 设置横纵坐标轴
    config_wsl(plt)
    temp = data[i:i+1].values.tolist()[0]

    for j in range(8):
        if temp[j] < 5.0:
            plt.plot(lon[j], lat[j], 'o', c=colors[j], markersize=10, label=station[j])
        else:
            plt.plot(lon[j], lat[j], 'o', c=colors[j], markersize=temp[j]*1.05, label=station[j])
        if temp[j] == 0.0:
            plt.text(lon[j], lat[j]+0.001, '0', ha='center', va='bottom', fontsize=26)
        elif 0 < temp[j]/5 < 25:
            plt.text(lon[j], lat[j]+0.003*(temp[j]/40), str(round(temp[j]/5, 2)), ha='center', va='bottom', fontsize=26)
        else:
            plt.text(lon[j], lat[j], str(round(temp[j]/5, 2)), ha='center', va='center', fontsize=26, fontweight='bold')

    # plt.plot(lon[7], lat[7], 'v', c='b', label=station[7], markersize=30)
    # plt.plot(lon[8], lat[8], 'v', c='g', label=station[8], markersize=30)
    # plt.plot(lon[6], lat[6], 'v', c='r', label=station[6], markersize=30)

    plt.plot(lon[10], lat[10], '*', c='k', label=station[10], markersize=40)
    plt.plot(lon[11], lat[11], '*', c='k', label=station[11], markersize=40)
    plt.plot(lon[9], lat[9], '*', c='k', label=station[9], markersize=40)

    index = data[i:i + 1].index.values.tolist()[0]
    plt.savefig('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\wsl\\rain\\' + index + '.png', dpi=150)
    # plt.show()
    plt.close()

    wind_ = wind[wind.index == index]
    ax = WindroseAxes.from_ax()
    wd = wind_['WD'].values.tolist()
    wv = wind_['WV'].values.tolist()
    if not len(wd) or not len(wv):
        continue
    
    ax.bar(wd, wv, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.savefig('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\wsl\\wind\\' + index + '.png')
    plt.close()
