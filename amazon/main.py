import os
from tfuc.logger import Logger
import requests
from bs4 import BeautifulSoup
from amazon.data_preparation import header, cookie
from amazon.get_reviews import get_review_data, get_review_num
from tfuc.multithread import ThreadPool
from amazon.save_date import conn

lg = Logger()

def amazon_craw(ASIN):
    lg.warning(ASIN)
    url = "https://www.amazon.com/Garmin-Instinct-Features-Monitoring-Graphite/dp/{}/ref=sr_1_17?dchild=1&qid=1598922312&sr=8-17&srs=17938598011&th=1".format(
        ASIN)
    lg.info(url)

    resp = requests.get(url=url, headers=header, cookies=cookie, timeout=5)
    status_code = resp.status_code

    if status_code != 200:
        lg.warning("you have an {} error".format(status_code))
        return
    lg.info("REQUEST SUCESS")

    # save html
    file_path = "html/{}.html".format(id)
    if not os.path.exists(file_path):
        with open(file_path, "w+") as f:
            f.write(resp.text)

    soup = BeautifulSoup(resp.text, 'html.parser')

    # title
    title = soup.find("span", id="productTitle").text.strip()
    lg.info("Title:{}".format(title))

    # stars
    star = float(soup.find("span", class_="a-icon-alt").text.split(" ")[0])
    lg.info("Stars:{}".format(star))

    # price
    price_ = soup.find("span", id="newBuyBoxPrice")
    if price_:
        price = price_.text.strip().replace("$", "")
        lg.info("Price:{}".format(price))
    elif soup.find("span", class_="a-color-price"):
        price = soup.find("span", class_="a-color-price").text.strip().replace("$", "")
        lg.info("Price:{}".format(price))
    elif soup.find("span", id="price"):
        price = soup.find("span", id="price").text.strip().replace("$", "")
        lg.info("Price:{}".format(price))
    else:
        lg.warning("NO price")
        exit()

    # ratings
    ratings = int(soup.find("span", id="acrCustomerReviewText").text.split(" ")[0].replace(",", ""))
    lg.info("ratings:{}".format(ratings))

    # num of answered questions
    # answered_questions = soup.find("a", id="askATFLink")
    # lg.info("Answered Questions:{}".format(answered_questions.text.strip()))

    # write to sqlite3
    try:
        values = (ASIN, title, float(price), star, ratings)
        cur = conn.cursor()
        if not cur.execute("SELECT ASIN FROM TopSellers WHERE ASIN == ?", (ASIN,)):
            cur.execute("INSERT INTO TopSellers VALUES (?, ?, ?, ?, ?)", values)
    except:
        lg.error("Repeat insert")

    # get reviews links
    all_review_url = soup.find("a", class_="a-link-emphasis a-text-bold").get("href")
    name = soup.find("a", class_="a-link-emphasis a-text-bold").get("href").split("/")[1]
    page_url = "https://www.amazon.com/{}".format(all_review_url)

    lg.info("Page url:{}".format(page_url))
    num_str = get_review_num(page_url)
    num = int(num_str.split(" ")[3].replace(",", ""))
    page_num = (num // 10) + 1
    review_page_list = []
    # for i in range(1, page_num + 1):
    for i in range(1, 2):
        review_page_list.append(
            "https://www.amazon.com/{}/product-reviews/{}/ref=cm_cr_arp_d_paging_btm_next_{}?ie=UTF8&reviewerType=all_reviews&pageNumber={}".format(
                name, ASIN, i, i))

    # get reviews data
    pool = ThreadPool(50, info=True)
    for url in review_page_list:
        pool.add_task(get_review_data, (ASIN, conn, url))
    pool.start()


with open("asin_uniq.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        ASIN = line.strip()
        amazon_craw(ASIN)
# amazon_craw(1631363867)


