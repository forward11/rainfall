import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from set_plt import config_lps

rain = pd.read_csv('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\lps\\lps_last.csv', index_col=0)  
info = pd.read_excel('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\lps\\StationInfo.xlsx')
wind = pd.read_excel('E:\\rainfall\\Location_based_analysis\\RainMap\\data\\lps\\WG006_7_10.xlsx', index_col=0)
data = rain.copy(deep=False)
data = data[:] * 5
info = info[:].reset_index()
station, lon, lat = info['台站号'], info['经度'], info['纬度']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#A9A9A9']

for i in range(len(data)):
    plt.figure(figsize=(6.4 * 3, 4.8 * 3))
    # 设置横纵坐标轴
    config_lps(plt)
    temp = data[i:i+1].values.tolist()[0]

    for j in range(7):
        if temp[j] < 2.0:
            plt.plot(lon[j], lat[j], 'o', c=colors[j], markersize=2, label=station[j])
        else:
            plt.plot(lon[j], lat[j], 'o', c=colors[j], markersize=temp[j]*0.5, label=station[j])
        if temp[j] == 0.0:
            plt.text(lon[j], lat[j]+0.005, '0', ha='center', va='bottom', fontsize=26)
        elif 0 < temp[j]/5 < 25:
            plt.text(lon[j], lat[j]+0.003*(temp[j]/20), str(round(temp[j]/5, 2)), ha='center', va='bottom', fontsize=26)
        else:
            plt.text(lon[j], lat[j], str(round(temp[j]/5, 2)), ha='center', va='center', fontsize=26, fontweight='bold')


    plt.plot(lon[10], lat[10], '*', c='k', label=station[10], markersize=40)
    plt.plot(lon[11], lat[11], '*', c='k', label=station[11], markersize=40)
    plt.plot(lon[12], lat[12], '*', c='k', label=station[9], markersize=40)

    index = data[i:i + 1].index.values.tolist()[0]
    plt.savefig('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\lps\\rain\\' + index + '.png', dpi=150)
    plt.close()

    wind_ = wind[wind.index == index]
    ax = WindroseAxes.from_ax()
    wd = wind_['WD'].values.tolist()
    wv = wind_['WV'].values.tolist()
    if not len(wd) or not len(wv):
        continue
    
    ax.bar(wd, wv, normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.savefig('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\lps\\wind\\' + index + '.png',dpi=300)
    plt.close()
