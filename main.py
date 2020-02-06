import os
import time
from getvd import *
from tfunc import WebC, video_downloader
from threading import Thread


def dld_html(car, num):
    if num == 1:
        url = 'https://my6b.com/{}/index.html'.format(car)
        # url = 'https://maya01.com/s/{}/#m'.format(car)
    else:
        url = 'https://my6b.com/{}/index_{}.html'.format(car, num)
        # url = 'https://maya01.com/s/{}/index_{}.html'.format(car, num)
    html = WebC(url).data()
    return html


def deal_with_url(html):
    lst = get_video_url(html)
    L = []
    for i in lst[0]:
        d_url = get_download_url(i)
        L.append(d_url)
    # writedown the url and name
    for i, l in enumerate(L):
        with open('url_list.txt', 'a+') as f:
            f.write(l + 'name:' + lst[1][i] + '\n')
    return L, lst[1]  # L:a list of video download url


# 多线程下载
class MyProcess(Thread):
    def __init__(self, url, name, page_num):
        super().__init__()
        self.url = url
        self.name = name
        self.page_num = page_num

    def run(self):
        video_downloader(self.url, self.name, self.page_num)


def downloading(lst, page_num):
    p_list = []
    for i, l in enumerate(lst[0]):
        p = MyProcess(l, lst[1][i], page_num)
        p_list.append(p)

    for i in p_list:
        time.sleep(0.5)
        print('开始下载:%s' % i.name)
        # i.setDaemon(True)
        i.start()

    for i in p_list:
        print(i.name)
        print('===========线程结束============')
        i.join()


def down_shell(category, page_num):
    html = dld_html(category, page_num)
    v_html_list = deal_with_url(html)
    print(v_html_list[0])
    print(v_html_list[1])
    downloading(v_html_list, page_num)


if __name__ == '__main__':
    for i in range(1, 10):
        print('开始下载第{}页'.format(i))
        down_shell('all', i)
