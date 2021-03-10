import pandas as pd
from file_reader import get_all_files

wsl_path = "C:\\Users\\11016\\Desktop\\output_data\\wsl_19\\data"
files = get_all_files(wsl_path)
date = pd.date_range('2019-05-01', '2020-06-30')
columns = ['R0001', 'R0002', 'R0003', 'R0004', 'R0005', 'R0006', 'R0007', 'R0008']
result = pd.DataFrame(index=date, columns=columns)

for file in files[0:8]:
    print("hello")
    temp = pd.read_excel(file)
    temp.drop_duplicates(inplace=True)
    rain_sum = temp.groupby(['Date'])['rain_day'].sum()
    rain_count = temp.groupby(['Date'])['rain_day'].count()
    result[lambda df: df.columns[files.index(file)]] = rain_sum / rain_count * 1440

result.to_csv("C:\\Users\\11016\\Desktop\\output_data\\wsl_19\\data\\RainGauge19_wsl.csv")
