import datetime
import pandas as pd
from pymongo import MongoClient


base_dir = r'CloudData'


def run():
    client = MongoClient('localhost', 27017)
    db = client['Cloud_DB']
    col = db['Cloud']

    data = {
        'date': [],
        'BRBG': [],
        'CDOC': [],
        'thick': [],
        'thin': []
    }
    s_time = datetime.date(2019, 9, 17)
    e_time = datetime.date(2021, 3, 11)
    while s_time < e_time:
        date = s_time.strftime("%Y-%m-%d")
        result = col.find({'date': date})
        BRBG, CDOC, thick, thin = 0, 0, 0, 0

        for line in result:
            BRBG += line['BRBG'] if line['BRBG'] > 0 else 0
            CDOC += line['CDOC'] if line['CDOC'] > 0 else 0
            thick += line['thick'] if line['thick'] > 0 else 0
            thin += line['thin'] if line['thin'] > 0 else 0

        print(date)
        data['date'].append(date)
        data['BRBG'].append(BRBG)
        data['CDOC'].append(CDOC)
        data['thick'].append(thick)
        data['thin'].append(thin)

        s_time = s_time + datetime.timedelta(days=1)
    df = pd.DataFrame(data, columns=['date', 'BRBG', 'thick', 'thin'])
    print(df)
    df.to_csv('cloud_every_day.csv', index=False)
    client.close()


if __name__ == '__main__':
    run()
