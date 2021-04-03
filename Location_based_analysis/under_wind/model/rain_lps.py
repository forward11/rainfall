import pandas as pd
import matplotlib.pyplot as plt
from set_plt import config_lps

#encoding="ISO-8859-1"
data=pd.read_csv(r"E:\rainfall\Location_based_analysis\under_wind\lps_rain_process.csv",index_col=0,encoding="ISO-8859-1")
info = pd.read_excel(r"E:\rainfall\Location_based_analysis\under_wind\data\lps\StationInfo_lps.xlsx")
station, lon, lat = info['台站号'], info['经度'], info['纬度']
wv5_x,wv5_y = data['WV5_x'],data['WV5_y']
wv6_x,wv6_y = data['WV6_x'],data['WV6_y']
wv7_x,wv7_y = data['WV7_x'],data['WV7_y']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2','#A9A9A9']
data = data[:] * 5

for i in range(len(data)):
    plt.figure(figsize=(6.4 * 3, 4.8 * 3))
    # 设置横纵坐标轴
    config_lps(plt)
    temp = data[i:i+1].values.tolist()[0]

    for j in range(7):
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

    plt.plot(lon[10], lat[10], '*', c='k', label=station[10], markersize=60)    #单电极
    plt.plot(lon[11], lat[11], '*', c='k', label=station[11], markersize=60)
    plt.plot(lon[12], lat[12], '*', c='k', label=station[12], markersize=60)

    plt.plot(lon[7], lat[7], 'D', c='red', label=station[7], markersize=40)
    plt.arrow(lon[7], lat[7],-wv5_x[i]/30,-wv5_y[i]/30)
    plt.arrow(lon[7], lat[7]+0.005,-wv5_x[i]/30,-wv5_y[i]/30)
    plt.arrow(lon[7], lat[7]-0.005,-wv5_x[i]/30,-wv5_y[i]/30)

    plt.plot(lon[8], lat[8], '^', c='red', label=station[8], markersize=40)
    plt.arrow(lon[8], lat[8],-wv6_x[i]/30,-wv6_y[i]/30)
    plt.arrow(lon[8], lat[8]+0.005,-wv6_x[i]/30,-wv6_y[i]/30)
    plt.arrow(lon[8], lat[8]-0.005,-wv6_x[i]/30,-wv6_y[i]/30)

    plt.plot(lon[9], lat[9], 'h', c='red', label=station[9], markersize=40)
    plt.arrow(lon[9], lat[9],-wv7_x[i]/300,-wv7_y[i]/300)
    plt.arrow(lon[9], lat[9]+0.005,-wv7_x[i]/300,-wv7_y[i]/300)
    plt.arrow(lon[9], lat[9]-0.005,-wv7_x[i]/300,-wv7_y[i]/300)

    plt.legend(loc=2, markerscale=0.3,fontsize=15)

    index = data[i:i + 1].index.values.tolist()[0]
    plt.savefig('E:\\rainfall\\Location_based_analysis\\under_wind\\plot\\lps_rain_process\\' + index + '.png', dpi=150)
    plt.close()
