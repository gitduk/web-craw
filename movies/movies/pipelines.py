# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
from threading import Thread

import requests

from .settings import VIDEO_PATH
import logging
from .spiders.tfunc import WebC


class MoviesPipeline(object):
    def process_item(self, item, spider):
        file_name = item["title"][0] + '.mp4'
        try:
            file_path = os.path.join(VIDEO_PATH, file_name)
            file_path = os.path.abspath(file_path)

            retry_count = 0
            while retry_count < 3:
                try:
                    print('-' * 100)
                    url = item["video_html_url"][0]
                    logging.info(
                        "[开始下载] \n retry: %d \n path: %s \n url: %s" % (
                            retry_count, file_path, url))
                    video_url = self.get_video_url(url)
                    # p = Thread(target=self.download_video, args=(video_url, file_path,))
                    # p.start()
                    break
                except Exception as EX:
                    print('-' * 100)
                    logging.warning(
                        "[下载异常] \n url: %s \n EX: %s" % (item["video_html_url"][0], str(EX)))
                    retry_count += 1

            if retry_count == 3:
                spider.start_urls.append(item["video_html_url"][0])
                print('-' * 100)
                logging.warning("[下载失败] \n Name: %s" % file_name)
            else:
                print('-' * 100)
                logging.info("[下载完成] \n Name: %s" % file_name)
        except:
            print('-' * 100)
            logging.exception("[下载失败] \n Name: %s" % file_name)
        return item

    def get_video_url(self, url):
        url_prefix = 'https://5fqx.com'
        url = url_prefix + url
        print('+' * 100)
        print(url)
        wc = WebC(url)
        soup = wc.soup
        div = soup.find_all('div', class_='l_m')
        for i in div:
            print(i)
        return div

    def download_video(self, video_url, file_name):
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
