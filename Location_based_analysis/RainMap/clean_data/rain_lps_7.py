import pandas as pd 
import os


dir = "C:\\Users\\11016\\Desktop\\wind_7\\"
index = 0
filenames = os.listdir(dir)
temp_df =[]
for file in filenames:
    print(index)
    temp = pd.read_excel(os.path.join(dir,file))
    temp.drop_duplicates(inplace=True)
    temp = temp.groupby(['Date'])['WD','WV'].mean()
    temp.to_excel(os.path.join("C:\\Users\\11016\\Desktop\\wind_7\\",'{}_D.xlsx').format(file))
