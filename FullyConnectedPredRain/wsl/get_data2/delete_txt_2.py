import pandas as pd 
import numpy as np 
import os

dir = "C:\\Users\\11016\\Desktop\\data_0508\\2018-2020\\2019\\"
months = ['1','2','4','5','6','7','8','9','10','11','12']
for month in months:
    files = os.listdir(dir+month)
    for file in files:
        file1 = dir+month+"\\"+file
        with open(file1,"r") as f:
            lines = f.readlines()
        with open(file1,"w") as f1:
            new_lines = lines[2:]
            for line in new_lines:
                f1.write(line)