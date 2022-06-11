# -*- coding: utf-8 -*-

"""
@author: tenkola
@time: 2022/6/9 20:15
"""

import csv

import requests
from pyquery import PyQuery as pq
import pymysql

db = pymysql.connect(host='192.168.0.102', user='root', password='123456', port=3306, db='spider_db')


def start_request(page):
    url = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    params = {
        'start': 25 * (page - 1),
        'filter': ''
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response


# 解析
def parse_detail(response):
    doc = pq(response.text)

    items = doc('.grid_view li')  # 点代表属性，  ＃好代表ID
    for item in items.items():
        data = dict()

        data['name'] = item('.hd span:eq(0)').text()
        data['fraction'] = item('.star span:eq(1)').text()
        data['num'] = item('.star span:eq(3)').text()

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


def main():
    for i in range(1, 250):
        response = start_request(i)
        results = parse_detail(response)
        for result in results:
            print(result)
        # write_mysql(result)


if __name__ == '__main__':
    main()
