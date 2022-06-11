import requests


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.0 .0Safari / 537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'https://movie.douban.com/top250?start=25&filter='
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-

"""
@author: tenkola
@time: 2022/6/1 15:19
"""
#请求
import csv

import requests
from pyquery import PyQuery as pq
import pymysql

db = pymysql.connect(host='192.168.0.102', user='root', password='123456', port=3306, db='spider_db')


def start_request(page):
    url = 'https://www.icama.cn/BasicdataSystem/pesticideRegistration/queryselect.do'
    data = {
        'pageNo': page,
        'pageSize': 30,
        'djzh': '',
        'nymc': '',
        'cjmc': '',
        'sf': '',
        'nylb': '',
        'zhl': '',
        'jx': '',
        'zwmc': '',
        'fzdx': '',
        'syff': '',
        'dx': '',
        'yxcf': '',
        'yxcf_en': '',
        'yxcfhl': '',
        'yxcf2': '',
        'yxcf2_en': '',
        'yxcf2hl': '',
        'yxcf3': '',
        'yxcf3_en': '',
        'yxcf3hl': '',
        'yxqs_start': '',
        'yxqs_end': '',
        'yxjz_start': '',
        'yxjz_end': '',

    }
    response = requests.post(url=url, data=data)

    return response

#解析
def parse_detail(response):
    doc = pq(response.text)

    items = doc('#tab tr:gt(0)')
    for item in items.items():
        data = dict()

        data['id'] = item('td:eq(0)').text()
        data['name'] = item('td:eq(1)').text()
        data['type'] = item('td:eq(2)').text()
        data['size'] = item('td:eq(3)').text()
        data['total'] = item('td:eq(4)').text()
        data['endtime'] = item('td:eq(5)').text()
        data['company'] = item('td:eq(6)').text()
        yield (data)


def sink():
    pass

#存储
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
    for i in range(1, 1497):
        response = start_request(i)
        results = parse_detail(response)
        for result in results:
            write_mysql(result)


if __name__ == '__main__':
    main()
