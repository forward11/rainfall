import numpy as np

font_label = {'weight': 'normal',
              'size': 26,
              }
font_ticks = {'weight': 'normal',
              'size': 22,
              }
font2 = {'weight': 'normal',
         'size': 28,
         }
font3 = {'weight': 'normal',
         'size': 40,
         }
font4 = {'weight': 'normal',
         'size': 40,
         }
font5 = {'weight': 'normal',
         'size': 36,
         }


def config_lps(plt):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # plt.title('降雨量分布图', font5)
    plt.ylabel('Latitude', fontdict=font_label)
    plt.xlabel('Longitude', fontdict=font_label)
    plt.ylim(35.50, 35.95)
    plt.xlim(106.08, 106.30)
    # x_ticks = [106.10 + 0.02*i for i in range(8)]
    # x_ticks_str = [str(i) for i in x_ticks]
    # plt.xticks(x_ticks, x_ticks_str)
    y_ticks = [35.6, 35.7, 35.8, 35.9]
    plt.yticks(y_ticks)
    plt.tick_params(width=1.0, length=8, labelsize=22)


def config_wsl(plt):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # plt.title('降雨量分布图', font5)
    plt.ylabel('Latitude', fontdict=font_label)
    plt.xlabel('Longitude', fontdict=font_label)
    plt.ylim(37.15, 37.24)
    plt.xlim(102.87, 102.94)
    # x_ticks = [106.10 + 0.02*i for i in range(8)]
    # x_ticks_str = [str(i) for i in x_ticks]
    # plt.xticks(x_ticks, x_ticks_str)
    # y_ticks = [35.6, 35.7, 35.8, 35.9]
    # plt.yticks(y_ticks)
    plt.tick_params(width=1.0, length=8, labelsize=22)
