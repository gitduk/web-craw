import requests
from bs4 import BeautifulSoup
from amazon.data_preparation import header, cookie
from tfuc.logger import Logger
import time
import threading

lock = threading.Lock()

lg = Logger()


def get_review_num(url):
    resp = requests.get(url=url, headers=header, cookies=cookie, timeout=5)
    time.sleep(0.1)
    soup = BeautifulSoup(resp.text, 'html.parser')
    num_str = soup.find("div", id="filter-info-section").span.text
    return num_str


def get_review_data(id, conn, url):
    resp = requests.get(url=url, headers=header, cookies=cookie, timeout=5)
    time.sleep(0.1)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.find_all("div", class_="a-section review aok-relative")

    for review in reviews:
        lg.info("===================================================")
        cuns_name = review.find("span", class_="a-profile-name").text
        star = float(review.find("span", class_="a-icon-alt").text.split(" ")[0])
        date = review.find("span", class_="a-size-base a-color-secondary review-date").text
        txt = review.find("span", class_="a-size-base review-text review-text-content").span.text

        values = (id, cuns_name, star, date, txt)
        cur = conn.cursor()

        lock.acquire()
        cur.execute("INSERT INTO Reviews (commodity_id, consumer, star, date, review) VALUES (?, ?, ?, ?, ?)", values)
        lg.info("ID :{}".format(id))
        lg.info("Cus Name:{}".format(cuns_name))
        lg.info("Star:{}".format(star))
        lg.info("Date:{}".format(date))
        lg.info("Txt:{}".format(txt))
        lock.release()
