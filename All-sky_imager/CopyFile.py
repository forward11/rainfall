import os
import shutil


base_dir = r'D:\SKY\asi16_data\asi_16107'
target_dir = r'D:\FindCloudData'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for i in os.listdir(base_dir):
    if os.path.isdir(os.path.join(base_dir, i)):
        txt_file = os.path.join(base_dir, i, 'evaluations', 'cloudiness_{}.txt'.format(i))
        if os.path.exists(txt_file):
            shutil.copy2(txt_file, target_dir)
        else:
            print(txt_file)
