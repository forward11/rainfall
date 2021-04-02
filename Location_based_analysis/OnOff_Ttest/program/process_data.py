import pandas as pd
from file_reader import get_all_files

lps_path = "C:\\Users\\11016\\Desktop\\output_data\\lps\\new"
files = get_all_files(lps_path)
date = pd.date_range('2020-04-01', '2020-11-30')
columns = ['RG001', 'RG002', 'RG003', 'RG004', 'RG005', 'RG006', 'RG007', 'RG008']
result = pd.DataFrame(index=date, columns=columns)

for file in files[0:8]:
    print("hello")
    temp = pd.read_excel(file)
    temp.drop_duplicates(inplace=True)
    rain_sum = temp.groupby(['Date'])['rain_day'].sum()
    rain_count = temp.groupby(['Date'])['rain_day'].count()
    result[lambda df: df.columns[files.index(file)]] = rain_sum / rain_count * 1440

result.to_csv("C:\\Users\\11016\\Desktop\\output_data\\lps\\new\\RainGauge19_lps.csv")
