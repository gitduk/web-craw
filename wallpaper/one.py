from tools.web_crawler import WebC
from tools.logger import Logger
from tools.multithread import ThreadPool
from tools.downloader import Downloader

logger = Logger()


def get_img(target, num):
    Url = 'https://api.zzzmh.cn/bz/getJson'
    Data = {'target': target, 'pageNum': num}
    Header = {
        'authority': 'api.zzzmh.cn',
        'method': 'POST',
        'path': '/bz/getJson',
        'scheme': 'https',
        'access': '684f2bed552c0fa5403ae9fd57424b4fc54ab6a56dbed0fc3867223caea36028',
        'content-length': '30',
        'content-type': 'application/json',
        'location': 'bz.zzzmh.cn',
        'origin': 'https://bz.zzzmh.cn',
        'referer': 'https://bz.zzzmh.cn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sign': '3fa2a92dbc8ae4ff36671782f4216729',
        'timestamp': '1583956089908',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    wc = WebC(Url, headers=Header)
    data = wc.get_payload_data(data=Data)
    fmt = 'https://w.wallhaven.cc/full/{}/wallhaven-{}.{}'
    url_list = []
    for i in data["result"]["records"]:
        if i["t"] == "p":
            url = fmt.format(i["i"][:2], i["i"], "png")
        else:
            url = fmt.format(i["i"][:2], i["i"], "jpg")
        url_list.append(url)
    save_img(num, url_list)
    return url_list


def save_img(page, img_list):
    for i, d in enumerate(img_list):
        dld = Downloader('Img/Page{}'.format(page), d, str(i), 'img')
        dld.run()


try:
    pool = ThreadPool(5, info=False)
    pool.add_task_list(get_img, [('Index', i) for i in range(10, 21)])
    pool.start()
except:
    logger.error()
finally:
    print('end')
