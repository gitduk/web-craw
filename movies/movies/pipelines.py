# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from selenium.webdriver.common.by import By

from tools.web_crawler import WebC
from .settings import VIDEO_PATH
import logging


class MoviesPipeline(object):
    def process_item(self, item, spider):
        file_name = item["title"][0] + '.mp4'
        try:
            file_path = os.path.join(VIDEO_PATH, file_name)
            file_path = os.path.abspath(file_path)

            retry_count = 0
            while retry_count < 2:
                try:
                    print('-' * 100)
                    url = item["video_html_url"][0]
                    logging.info(
                        "[开始下载] \n retry: %d \n path: %s \n url: %s" % (
                            retry_count, file_path, url))
                    video_url = self.get_video_url(url, file_name)
                    # p = Thread(target=download_video, args=(video_url, file_path,))
                    # p.start()
                    break
                except Exception as EX:
                    print('-' * 100)
                    logging.warning(
                        "[下载异常] \n url: %s \n EX: %s" % (item["video_html_url"][0], str(EX)))
                    retry_count += 1

            if retry_count == 2:
                spider.start_urls.append(item["video_html_url"][0])
                print('-' * 100)
                logging.warning("[下载失败] \n Name: %s" % file_name)
            else:
                print('-' * 100)
                logging.info("[下载完成] \n Name: %s" % file_name)
        except:
            print('-' * 100)
            logging.exception("[下载失败] \n Name: %s" % file_name)

    def get_video_url(self, url, name):
        url_prefix = 'https://5fqx.com'
        url = url_prefix + url
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.implicitly_wait(10)
        wc = WebC(url)
        driver = wc.selenium_driver
        a = driver.find_element(By.XPATH, "//div[@class='l_m']/a[2]")
        video_url = a.get_attribute('href')
        with open('video_url.txt', 'a+') as f:
            f.write(video_url + "|{}\n".format(name))
        return video_url
