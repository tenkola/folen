import csv

import requests
from pyquery import PyQuery as pq
import pymysql
import pymongo

client = pymongo.MongoClient(host='192.168.0.102', port=27017)
db = pymysql.connect(host='192.168.0.102', user='root', password='123456', port=3306, db='spider_db')


def start_request(page):
    url = 'https://www.phb123.com/renwu/fuhao/shishi_{}.html'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    return response


# 解析
def parse_detail(response):
    doc = pq(response.text)

    items = doc('tbody tr:gt(0)')  # 点代表属性，  ＃好代表ID
    for item in items.items():
        data = dict()
        data['ranking'] = item(' td:eq(0)').text()
        data['name'] = item('td:eq(1)').text()
        data['wealth'] = item('td:eq(2)').text()
        data['company'] = item('td:eq(3)').text()
        data['country'] = item('td:eq(4)').text()
        yield data


def sink():
    pass


# 存储
def write_csv(result):
    path = 'nongyao.csv'
    with open(path, 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(result.values())


def write_mysql(result):
    cursor = db.cursor()
    keys = ','.join(result.keys())
    values = ','.join(['%s'] * len(result))
    sql = 'insert into {table} ({keys}) values ({values})'.format(table='nongyao', keys=keys, values=values)
    cursor.execute(sql, tuple(result.values()))
    db.commit()
    cursor.close()


def write_mongodb(result, table):
    db = client['spider']

    collection = db[table]
    collection.insert_one(result)


def main():
    for i in range(1, 16):
        response = start_request(i)
        results = parse_detail(response)
        for result in results:
            print(result)
            write_mongodb(result, 'news')
            # write_mysql(result)


if __name__ == '__main__':
    main()
