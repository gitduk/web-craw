import requests
import re
import urllib.request
import os
import time
from threading import Thread



def wallpaper_download(t, n, p):
    html = requests.get('http://desk.zol.com.cn/%s/good_%d.html' % (t, n))
    html.encoding = 'gb2312'
    data = html.text
    # print(data)
    # 获取页面壁纸集的链接地址，数量和名字
    url = re.findall('<a class="pic" href="(.*?)"', data)
    img_amount = re.findall('</em> \(\d+?张\)</span>', data)
    img_name = re.findall('<em>(.*?)</em>', data)
    # 去除正则表达式匹配的多余项
    # print(url)
    # print(len(url))
    # print(img_name)
    # print(len(img_name))
    # print(img_amount)
    # print(len(img_amount))

    url = url[:-1]
    img_name = img_name[2:-1]

    requests_url = []
    for i in url:
        requests_url.append('http://desk.zol.com.cn' + i)

    # print(requests_url)

    # 二次访问找到下载链接
    def download(d_url, name, t):
        d_html = requests.get(d_url)
        d_html.encoding = 'utf-8'
        data = d_html.text
        # 找到图片所在网址
        img_url = re.findall('id="1920x1080" href="(.*?)"', data)
        if not img_url:
            img_url = re.findall('id="1600x900" href="(.*?)"', data)
            if not img_url:
                img_url = re.findall('id="1440x900" href="(.*?)"', data)
                if not img_url:
                    img_url = re.findall('id="1366x768" href="(.*?)"', data)
                    if not img_url:
                        img_url = re.findall('id="1280x800" href="(.*?)"', data)
                        if not img_url:
                            img_url = re.findall('id="1024x768" href="(.*?)"', data)
                            if not img_url:
                                print('线程%d' % p + '此页图片无下载链接，跳过下载，开启下一页下载。')
                                return

        real_img_url = 'http://desk.zol.com.cn' + img_url[0]

        # 访问网址， 找到下载链接
        img_d_html = requests.get(real_img_url)
        img_d_url = re.findall('<img src="(.*?)">', img_d_html.text)
        print('线程%d: ' % p + '图片下载链接：', img_d_url[0])
        print('线程%d: ' % p + '图片下载中......')
        if not os.path.exists('/home/dongkai/Pictures/ZOLwallpaper/%s/' % name):
            os.mkdir('/home/dongkai/Pictures/ZOLwallpaper/%s/' % name)

        time.sleep(0.2)
        urllib.request.urlretrieve(img_d_url[0], '/home/dongkai/Pictures/ZOLwallpaper/%s/' % name + str(t) + '.jpg')
        print('线程%d: ' % p + '下载完成')
        next_url = re.findall('class="next" href="(.*?)"', data)
        real_next_url = 'http://desk.zol.com.cn' + next_url[0]
        if real_next_url != 'http://desk.zol.com.cnjavascript:;':
            print('线程%d: ' % p + '下一张图片地址：', real_next_url)
            print('线程%d: ' % p + '开始下载下一张图片')
            t += 1
            download(real_next_url, name, t)
        else:
            print('线程%d: ' % p + '已经下载完成当前分类壁纸')
            return

    x = 0
    for i in requests_url:
        try:
            download(i, img_name[x], 0)
        except IndexError:
            print('网页不规范，名称与链接数量不对应，停止下载。')
        x += 1

    print("====================线程%d结束====================" % p)

    # 统计结束的线程
    global p_num
    p_num += 1
    global page_num
    if p_num == page_num:
        print('=============================下载结束====================================')


# 多线程下载
class MyProcess(Thread):
    def __init__(self, type, page, n):
        super().__init__()
        self.page = page
        self.n = n
        self.type = type

    def run(self):
        wallpaper_download(self.type, self.page, self.n)



if __name__ == '__main__':

    p_num = 0

    p_list = []
    t = 0
    print("""可选类型：
    fengjing,
    dongman,
    meinv,
    chuangyi,
    katong,
    qiche,
    youxi,
    keai,
    mingxing,
    jianzhu,
    zhiwu,
    dongwu,
    jingwu,
    yingshi,
    chemo,
    tiyu,
    model,
    shouchaobao,
    meishi,
    xingzuo,
    jieri,
    pinpai,
    beijing,
    qita
    """)
    type = input('请输入下载壁纸类型：\n')
    page_num = input('请输入下载页数：\n')
    for i in range(int(page_num)):
        p = MyProcess(type, i, t)
        p_list.append(p)
        t += 1

    for i in p_list:
        i.start()

    for i in p_list:
        i.join()
