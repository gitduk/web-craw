import re
from urllib import request
import urllib3
import os
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

urllib3.disable_warnings()


class WebC(object):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    def __init__(self, url):
        from fake_useragent import UserAgent
        self.__ua = UserAgent()
        self.__headers = {
            'User-Agent': self.__ua.random
        }
        self.__url = url
        self.__save = True
        self.__char = 'utf-8'

    @property
    def save(self):
        return self.__save

    @save.setter
    def save(self, value):
        self.__save = value

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char):
        self.__char = char

    @property
    def html(self):
        time.sleep(0.2)
        rq = requests.get(self.__url, headers=self.__headers)
        time.sleep(0.5)
        rq.encoding = self.__char
        html = rq.text
        if self.save:
            with open('result.html', 'w') as f:
                f.write(html)
        return html

    @property
    def header(self):
        response = request.urlopen(self.__url)
        header = response.info()
        return header

    @property
    def soup(self):
        if os.path.exists('result.html'):
            soup = BeautifulSoup(open('result.html'), 'html.parser')
        else:
            soup = BeautifulSoup(self.html, 'html.parser')

        return soup


class SQL(object):
    def __init__(self, user, password, port, dbname, char, base):
        self.engine = create_engine(
            'mysql://{}:{}@localhost:{}/{}?charset={}'.format(user, password, port, dbname, char),
            echo=False)
        self.Base = base
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def write(self, msg):
        self.session.add(msg)
        self.session.commit()


def download_video(video_url, file_name):
    download_header = {
        "Accept-Encoding": "identity;q=1, *;q=0",
        "Range": None,
        "Referer": None,
        # "Connection": "Close",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.6.2"
    }
    proxy = {}
    path = os.path.dirname(file_name)
    if not os.path.exists(path):
        os.mkdir(path)

    content_offset = 0
    if os.path.exists(file_name):
        content_offset = os.path.getsize(file_name)

    content_length = 1024 * 1024 * 10
    total_length = None
    download_header["Referer"] = video_url
    with requests.session() as s:
        s.headers = download_header
        s.proxies = proxy
        s.stream = True
        while True:
            s.headers["Range"] = "bytes=%d-%d" % (content_offset, content_offset + content_length)
            resp = s.get(video_url, timeout=10)
            if not resp.ok:
                if resp.status_code == 416:
                    return
                continue
            resp_length = int(resp.headers["Content-Length"])
            resp_range = resp.headers["Content-Range"]
            if total_length is None:
                total_length = int(resp_range.split("/")[1])
            resp_offset = int(re.compile(r"bytes (\d+)-").findall(resp_range)[0])
            if resp_offset != content_offset:
                continue

            with open(file_name, 'ab') as file:
                file.write(resp.content)
                file.flush()

            content_offset += resp_length
            if content_offset >= total_length:
                break
