import socks
import urllib3
from tfuc.logger import Logger
import requests
from bs4 import BeautifulSoup
from amazon.data_preparation import header, cookie, proxy_list, cookies
from amazon.get_data import save_review, get_title, get_star, get_price, get_rating, kill_img_code_page, get_proxy, \
    save_html, write_to_sqlite
from tfuc.multithread import ThreadPool
from amazon.save_date import conn
from lxml import etree

lg = Logger()


def amazon_request(url):
    try:
        resp = requests.get(url=url, headers=header, cookies=cookie, proxies=get_proxy(), timeout=30)
        lg.info(resp.url)
        status_code = resp.status_code
        # solve request error
        if status_code != 200:
            lg.warning("{}: {}".format(ASIN, status_code))
            lg.warning("{}: you have an {} error".format(ASIN, status_code))
            save_html("html/{}_{}.html".format(ASIN, status_code), resp)
            return None

        soup = BeautifulSoup(resp.text, 'lxml')

        # img code
        img_code_url_ = soup.find("div", class_="a-row a-text-center")

        while img_code_url_:
            lg.warning("{}: IMAGE CODE".format(ASIN))
            img_url = img_code_url_.img.get("src")
            resp, soup = kill_img_code_page(ASIN, url, soup, img_url)
            img_code_url_ = soup.find("div", class_="a-row a-text-center")
        return resp, soup

    except requests.exceptions.ReadTimeout:
        lg.warning("{} Read Time Out".format(url))
        resp, soup = amazon_request(url)
        return resp, soup

    except ConnectionRefusedError:
        return None
    except socks.ProxyConnectionError:
        return None
    except urllib3.exceptions.NewConnectionError:
        return None
    except urllib3.exceptions.MaxRetryError:
        return None
    except requests.exceptions.ConnectionError:
        return None


def amazon_craw(ASIN):
    url = "https://www.amazon.com/dp/{}/".format(
        ASIN)
    lg.info(url)

    try:
        resp, soup = amazon_request(url)
    except TypeError:
        return

    try:
        # ASIN, title, star, price, rating
        if soup:
            data = (ASIN, get_title(ASIN, soup), get_star(ASIN, soup), get_price(ASIN, soup), get_rating(ASIN, soup))
            write_to_sqlite(conn, "TopSellers", "ASIN", data)
        else:
            lg.warning(resp.status_code)

    except:
        lg.error("{}:Parsing Error".format(ASIN))

    try:
        save_review(ASIN)
    except:
        lg.error("{}: Get Review Data Error".format(ASIN))


if __name__ == '__main__':

    pool = ThreadPool(10)
    with open("asin_uniq.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            ASIN = line.strip()
            pool.add_task(amazon_craw, ASIN)
        pool.start()

    print("end")
    # amazon_craw("B00002N8CX")
