import datetime
import calendar
import pandas as pd
from pymongo import MongoClient


base_dir = r'CloudData'


def run():
    client = MongoClient('localhost', 27017)
    db = client['Cloud_DB']
    col = db['Cloud']

    data = {
        'month': [],
        'BRBG': [],
        'CDOC': [],
        'thick': [],
        'thin': []
    }
    # 从19年8月到21年2月, 19年7月和21年3月天数不够
    current_month = 7
    while current_month < 26:
        year = 2019 + current_month // 12
        month = current_month % 12 + 1

        days_in_this_month = calendar.monthrange(year, month)[1]

        BRBG, CDOC, thick, thin = 0, 0, 0, 0

        s_time = datetime.date(year, month, 1)
        month_str = s_time.strftime("%Y-%m")
        print(month_str)

        for d in range(1, days_in_this_month+1):
            s_time = datetime.date(year, month, d)
            date = s_time.strftime("%Y-%m-%d")
            result = col.find({'date': date})
            for line in result:
                BRBG += line['BRBG'] if line['BRBG'] > 0 else 0
                CDOC += line['CDOC'] if line['CDOC'] > 0 else 0
                thick += line['thick'] if line['thick'] > 0 else 0
                thin += line['thin'] if line['thin'] > 0 else 0

        data['month'].append(month_str)
        data['BRBG'].append(BRBG)
        data['CDOC'].append(CDOC)
        data['thick'].append(thick)
        data['thin'].append(thin)
        current_month += 1

    df = pd.DataFrame(data, columns=['month', 'BRBG', 'thick', 'thin'])
    print(df)
    df.to_csv('cloud_every_monthy.csv', index=False)
    client.close()


if __name__ == '__main__':
    run()
