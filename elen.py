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
