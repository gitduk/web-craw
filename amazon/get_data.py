import json
import random
import requests
from bs4 import BeautifulSoup
from amazon.data_preparation import header, cookie, proxy_list, cookies
from amazon.save_date import conn
from tfuc.logger import Logger
import time
import threading
import re

from tfuc.multithread import ThreadPool

lock = threading.Lock()

lg = Logger()


def get_proxy():
    random_proxy = proxy_list[random.randint(0, len(proxy_list) - 1)]
    # proxy = {"https": random_proxy["type"] + "://" + random_proxy["addr"]}
    proxy = {"https": "socks5h://" + random_proxy["addr"]}
    lg.info("Proxy: {}".format(proxy))
    return proxy


def save_html(path, resp):
    with open(path, "w") as f:
        f.write(resp.text)


def write_to_sqlite(conn, table_name, p_key, datas):
    cur = conn.cursor()
    cur.execute("SELECT ASIN FROM TopSellers WHERE ASIN = 'B00000JGWY'")
    str_ = "SELECT %s FROM %s WHERE %s = '%s'" % (p_key, table_name, p_key, datas[0])
    cur.execute(str_)
    if not cur.fetchone():
        values = '(' + ','.join(['? '] * len(datas)) + ')'
        cur.execute("INSERT INTO {} VALUES {}".format(table_name, values), datas)
    conn.commit()


def kill_img_code_page(ASIN, url, soup, img_url):
    parms_ = soup.find_all("input")
    if parms_:
        parms_list = [p.get("value") for p in parms_]
    else:
        lg.warning("can not get parms data")

    lg.warning(img_url)
    f = requests.get(img_url).content
    files = {'img': f}
    code_resp = requests.post('http://192.168.0.222:8008/amz/v1', files=files)
    code_dict = json.loads(code_resp.text)
    code_status = code_dict["status_code"]
    if code_status == 200:
        result = code_dict["result"]
        data = {'amzn': parms_list[0], 'amzn-r': '/', 'field-keywords': result}
        lg.warning(data)

        vali_url = "https://www.amazon.com/errors/validateCaptcha"
        vali_resp = requests.get(vali_url, params=data, allow_redirects=False)
        head = vali_resp.headers
        set_cookie = head["set-cookie"]
        resp2 = requests.get(url=url, headers=header, cookies=cookies(set_cookie), proxies=get_proxy(), timeout=30)
        soup2 = BeautifulSoup(resp2.text, 'html.parser')
        return resp2, soup2
    else:
        lg.warning("can not get image code [{}]".format(code_status))
        return None, None


def get_title(ASIN, soup):
    title_ = soup.find("span", id="productTitle")
    if title_:
        title = title_.text.strip()
        lg.info("{}: Title:{}".format(ASIN, title))
        return title
    else:
        lg.warning("{}: No title".format(ASIN))
        return None


def get_star(ASIN, soup):
    star_ = soup.find("span", class_="a-icon-alt")
    if star_:
        star = float(star_.text.split(" ")[0])
        lg.info("{}: Stars:{}".format(ASIN, star))
        return star
    else:
        lg.warning("{}: NO star".format(ASIN))
        return None


def get_price(ASIN, soup):
    price_ = soup.find("div", id=lambda x: x in ["buyNew_noncbb", "priceblock_ourprice"])
    if price_:
        price = price_.text.replace("$", "").replace(" ", "").replace("Price:", "").strip()
        lg.info("{}: Price:{}".format(ASIN, price))
        return price
    elif soup.find("span",
                   id=lambda x: x in ["priceblock_ourprice", "price", "newBuyBoxPrice", "price_inside_buybox",
                                      "a-size-base a-color-price"]):
        price = soup.find("span",
                          id=lambda x: x in ["priceblock_ourprice", "price", "newBuyBoxPrice",
                                             "price_inside_buybox"]).text.replace("$",
                                                                                  "").replace(
            " ",
            "").replace(
            "Price:", "").strip()
        lg.info("{}: Price:{}".format(ASIN, price))
        return price
    elif soup.find("span", class_=lambda x: x in ["a-color-price"]):
        price = soup.find("span", class_=lambda x: x in ["a-color-price"]).text.replace("$", "").replace(" ",
                                                                                                         "").replace(
            "Price:", "").strip()
        lg.info("{}: Price:{}".format(ASIN, price))
        return price
    else:
        lg.warning("{}: NO price".format(ASIN))
        return None


def get_rating(ASIN, soup):
    rating_ = soup.find("span", id="acrCustomerReviewText")
    if rating_:
        rating = int(rating_.text.split(" ")[0].replace(",", ""))
        lg.info("{}: ratings:{}".format(ASIN, rating))
        return rating
    else:
        lg.warning("{}: NO ratings".format(ASIN))
        return None


def save_review(ASIN):
    page_url = "https://www.amazon.com/product-reviews/{}/".format(ASIN)
    lg.info("{}: Page url:{}".format(ASIN, page_url))
    num = get_review_num(ASIN, page_url)
    if num:
        lg.info("{}: Reviews:{}".format(ASIN, num))
        page_num = (num // 10) + 1
        lg.info("{}: Pages:{}".format(ASIN, page_num))
        review_page_list = []
        for i in range(1, page_num + 1):
            # for i in range(1, 2):
            review_page_list.append(
                "https://www.amazon.com/product-reviews/{}/ref=cm_cr_arp_d_paging_btm_next_{}?pageNumber={}".format(
                    ASIN, i, i))

        # get reviews data
        pool = ThreadPool(10, info=False)
        for url in review_page_list:
            pool.add_task(get_review_data, (ASIN, conn, url))
        pool.start()
    else:
        lg.warning("can not get review url")


def get_review_num(ASIN, url):
    random_proxy = proxy_list[random.randint(0, len(proxy_list) - 1)]
    proxy = {random_proxy["type"]: random_proxy["addr"]}
    resp = requests.get(url=url, headers=header, cookies=cookie, proxies=proxy, timeout=30)
    time.sleep(0.1)
    soup = BeautifulSoup(resp.text, 'lxml')

    img_code_url_ = soup.find("div", class_="a-row a-text-center")

    if img_code_url_:
        lg.warning("{}: IMAGE CODE".format(ASIN))
        img_url = img_code_url_.img.get("src")
        resp, soup = kill_img_code_page(ASIN, url, soup, img_url)

    num_str_ = soup.find("div", class_="a-row a-spacing-base a-size-base")
    if num_str_:
        num_str = num_str_.span.text
        num = re.search("\| (.*?) global", num_str.strip(), re.S)
        return int(num.group(1).replace(",", ""))
    else:
        return None


def get_review_data(asin, conn, url):
    random_proxy = proxy_list[random.randint(0, len(proxy_list) - 1)]
    proxy = {random_proxy["type"]: random_proxy["addr"]}
    resp = requests.get(url=url, headers=header, cookies=cookie, proxies=proxy, timeout=30)
    time.sleep(0.1)
    soup = BeautifulSoup(resp.text, 'lxml')
    reviews = soup.find_all("div", class_="a-section review aok-relative")

    if reviews:
        for review in reviews:
            lg.info("===================================================")
            lg.info(url)
            review_id = review.get("id")
            cons_id_ = review.find("a", class_="a-profile")
            if cons_id_:
                cons_id = cons_id_.get("href").split("account.")[1].split("/")[0]
            else:
                continue

            cons_name = review.find("span", class_="a-profile-name").text
            star = float(review.find("span", class_="a-icon-alt").text.split(" ")[0])
            date = review.find("span", class_="a-size-base a-color-secondary review-date").text
            review_title = review.find("div", class_="a-row").find_all("span")[3].text
            review_text_ = review.find("span", class_="a-size-base review-text review-text-content")
            img_url_ = review.find_all("img", class_="review-image-tile")
            if review_text_.span and img_url_:
                review_text = review_text_.span.text.strip()
                img_url = "|".join([i.get("src") for i in img_url_])
                data = (review_id, cons_id, cons_name, asin, star, date, review_title, review_text, img_url)
            elif review_text_.span:
                review_text = review_text_.span.text.strip()
                data = (review_id, cons_id, cons_name, asin, star, date, review_title, review_text, None)
            elif img_url_:
                img_url = "|".join([i.get("src") for i in img_url_])
                data = (review_id, cons_id, cons_name, asin, star, date, review_title, None, img_url)

            cur = conn.cursor()

            lock.acquire()
            write_to_sqlite(conn, "Reviews", "review_id", data)

            lg.info("ReviewID :{}".format(review_id))
            lg.info("Cus ID:{}".format(cons_id))
            lg.info("Cus Name:{}".format(cons_name))
            lg.info("ASIN :{}".format(asin))
            lg.info("Star:{}".format(star))
            lg.info("Date:{}".format(date))
            lg.info("review Title: {}".format(review_title))
            lg.info("Txt:{}".format(review_text))
            lock.release()
