from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from tfunc import WebC

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}


# get the video url and name
def get_video_url(html):
    head = 'https://my6b.com'
    soup = BeautifulSoup(html, 'html.parser')
    _url = soup.find_all('h2')
    url = [head+i.a.get('href') for i in _url]
    name = [i.get_text() for i in _url]
    return url, name


def get_download_url(url):
    html = WebC(url).data()
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('a', 'btn btn-secondary').get('href')
    if url:
        return url
    else:
        print('没有获取到下载链接')





