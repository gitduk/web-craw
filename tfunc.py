import re
import sys
import urllib
from contextlib import closing
from urllib import request

import chardet
import urllib3
import os
import time
import tqdm
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

urllib3.disable_warnings()

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}


def match_url(url):
    return re.match(r'^https?:/{2}\w.+$', url)


def video_downloader(video_url, video_name, page_num):
    time.sleep(0.5)
    response = requests.get(video_url, stream=True, headers=headers)
    file_size = int(response.headers['content-length'])
    if os.path.exists(video_name):
        first_byte = os.path.getsize(video_name)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    header = {"Range": f"bytes={first_byte}-{file_size}"}

    time.sleep(0.5)
    with closing(requests.get(video_url, stream=True, verify=False, headers=header)) as response:
        file_size = int(response.headers['content-length'])
        path = '/home/dongkai/Videos/v/'
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            with(open('/home/dongkai/Videos/v/{}{}{}{}'.format(page_num, ':', video_name, '.mp4'), 'wb')) as f:
                i = 0
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        i = i + 1
                        f.write(chunk)
                        fmt = '第{page}页:{name} : [{detail}{char}]'
                        downloaded = round(((i * 102400) / file_size), 2)
                        print(fmt.format(page=page_num, name=video_name, detail=downloaded, char='%'))
    return file_size


class WebC(object):
    def __init__(self, url):
        from fake_useragent import UserAgent
        self.ua = UserAgent()
        self.headers = {
            'User-Agent': self.ua.random
        }
        self.url = url
        self.save = False
        self.charset = 'utf-8'

    def data(self):
        time.sleep(0.2)
        rq = requests.get(self.url, headers=self.headers)
        rq.encoding = self.charset
        data = rq.text
        if self.save:
            with open('result.html', 'w') as f:
                f.write(data)
        return data

    def info(self):
        response = request.urlopen(self.url)
        headers = response.info()
        if self.save:
            data = response.read()  # bytes
            with open('result.html', 'wb') as f:
                f.write(data)
        data = response.read().decode(self.charset)  # str
        return headers, data

    def get_pic(self):
        data = self.info()[1]
        url = re.findall('<a href="(.*?\.jpg)"', data)
        print(url)


if __name__ == '__main__':
    wc = WebC('http://www.netbian.com/desk/112.htm')
    wc.charset = 'gbk'
    # wc.save = True
    print(wc.info()[1])
    wc.get_pic()
