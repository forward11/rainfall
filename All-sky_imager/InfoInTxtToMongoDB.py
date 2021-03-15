import os
import time
from pymongo import MongoClient


base_dir = r'CloudData'

client = MongoClient('localhost', 27017)
db = client['Cloud_DB']
col = db['Cloud']

for file in os.listdir(base_dir):
    with open(os.path.join(base_dir, file)) as f:
        print(file)
        content = f.readlines()[2:]
        for line in content:
            line = line.split()
            result = dict()
            # 时间转换校准
            time_stamp = int(time.mktime(time.strptime(line[0]+line[1], "%Y%m%d%H%M%S"))) + 8 * 60 * 60
            time_local = time.localtime(time_stamp)

            result['date'] = time.strftime("%Y-%m-%d", time_local)
            result['time'] = time.strftime("%H:%M:%S", time_local)
            # 计算时使用的照片, '11'表示用了后缀11的一张照片计算, '1112'表示用了两张照片
            result['Ext'] = line[2]
            # BRGB算法计算的总云量
            result['BRBG'] = float(line[3])
            # CDOC算法计算的总云量
            result['CDOC'] = float(line[4])
            # 用CDOC算法计算的厚云的云量
            result['thick'] = float(line[5])
            # 用CDOC算法计算的薄云的云量
            result['thin'] = float(line[6])
            # 太阳可见度(0, 1, 3, 5, 8, 9)
            result['sun'] = int(line[7])
            #
            result['hcf'] = float(line[8])
            #
            result['BRmin'] = float(line[9])
            result['BRmid'] = float(line[10])
            result['Brmax'] = float(line[11])
            # 12列之后的值，应该是存的一些经纬度之类的设置信息，都是相同的
            # ['0', '0', '11', '12', '0', '37.19', '102.86', '0.8', '0.5', '5', '0.1', '2.5', '2.5', '0.9', '0.99',
            # '0.5', '0.1', '0.9', '15', '-9', '0.12', '79.5', '0.965', '1', '0', '1', '1', '1', '0', '0', '0']
            col.insert_one(result)
client.close()
