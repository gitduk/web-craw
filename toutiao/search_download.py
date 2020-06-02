from tools.web_crawler import WebC
from tools.logger import Logger
from tools.downloader import Downloader, ThreadPool
import time
import os

lg = Logger()


@lg.log()
def get_data(key, offset):
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword={}&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1586376202445&_signature=.hK4TAAgEBAlwgA2mqd8TP4T-VAAKCmAgnwBvnsyka.PuY.Cgcld81w3HjFjKnP0gUCSAznM6ShXczfxiLKVPBooqbSZ65QY1FhEcNXWXzLYdjCFhO24Yczx78oMzRcSVRO'.format(
        offset, key)
    cookies = 'tt_webid=6802935200747734535; SLARDAR_WEB_ID=78a23d69-712b-4b35-9c92-45006ddbb9ac; WEATHER_CITY=%E5%8C%97%E4%BA%AC; ttcid=4c817e85eab94bac8a63ffee1550859d29; tt_webid=6802935200747734535; csrftoken=1400e70a8b3c5424c87a84b64b171c73; sso_uid_tt=cbf93c6c11f172e2a70dd54dc64b5a9f; sso_uid_tt_ss=cbf93c6c11f172e2a70dd54dc64b5a9f; toutiao_sso_user=c895c5d6ff236bf93af261bb77f535ee; toutiao_sso_user_ss=c895c5d6ff236bf93af261bb77f535ee; sid_guard=37b30f0a23472c29d3e8e0014440607e%7C1586363340%7C5184000%7CSun%2C+07-Jun-2020+16%3A29%3A00+GMT; uid_tt=bf60b914f9ce34b45b39240a897737fb; uid_tt_ss=bf60b914f9ce34b45b39240a897737fb; sid_tt=37b30f0a23472c29d3e8e0014440607e; sessionid=37b30f0a23472c29d3e8e0014440607e; sessionid_ss=37b30f0a23472c29d3e8e0014440607e; __utma=24953151.2079936350.1586366655.1586366655.1586366655.1; __utmz=24953151.1586366655.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cp=5E8EC19EDC1EDE1; s_v_web_id=k8rqpjsr_ECPPYe12_6o5u_4Uv4_BNwJ_LaJFoTZgpytG; tt_scid=6IokNZX3yr.j1U5DoeiJlvWU9EKeSX2O32xXKHd.RqGBNr2oaLgKPjwlhuwTAXqx6d35; __tasessionId=afxci8cqt1586376945350'

    wc = WebC(url, cookies=cookies, ip=True)
    data = wc.get_json_dict()
    _image_url = 'http://{}-tt.byteimg.com/large/pgc-image/{}'

    try:
        title_list = []
        image_list = []
        if not data['data']:
            lg.warning('No data')
            return
        for i in data['data']:
            if 'image_list' in i.keys() and 'emphasized' in i.keys():
                title_list.append(i['emphasized']['title'].replace('<em>', '').replace('</em>', ''))
                image_url_list = []
                for j in i['image_list']:
                    p = j['url'].split('-')[0].split('//')[-1]
                    id = j['url'].split('/')[-1]
                    image_url = _image_url.format(p, id)
                    image_url_list.append(image_url)
                image_list.append(image_url_list)
        print(title_list)
        return title_list, image_list
    except:
        lg.error()


def downloader(key, offset, title_list, image_list):
    for i in zip(title_list, image_list):
        dir_path = 'images/{}/{}/{}'.format(key, offset, i[0])
        os.makedirs(dir_path, exist_ok=1)
        for j, url in enumerate(i[1]):
            dldr = Downloader(dir_path, url, str(j), 'jpg')
            dldr.run()


def task(key, offset):
    try:
        title_list, image_list = get_data(key, offset)
    except TypeError:
        return
    downloader(key, offset, title_list, image_list)


key = input('Key:')
task_list = []
args = [(key, i * 20) for i in range(10)]
pl = ThreadPool(max_workers=1)
pl.add_task_list(task, args)
pl.start()
