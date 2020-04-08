import os
from tools.web_crawler import WebC
from tools.logger import Logger
from tools.multithread import ThreadPool
from tools.data_factory import Csv
from threading import Lock
from matplotlib import pyplot as plt, font_manager
import pandas as pd
from pandas import Series, DataFrame

lg = Logger()


@lg.log()
def get_data(start):
    _url = 'https://book.douban.com/top250?start={}'
    url = _url.format(start)
    wc = WebC(url)
    soup = wc.soup

    _book_name = soup.find_all('div', class_='pl2')
    book_name_list = [i.a.get('title') for i in _book_name]
    lg.info(book_name_list)

    _book_info = soup.find_all('p', class_='pl')

    book_publish_date_list = []
    book_price_list = []
    book_publisher_list = []
    for i in _book_info:
        text = i.text
        if len(text.split(' / ')) <= 3:
            break
        book_price_list.append(text.split(' / ')[-1])
        book_publish_date_list.append(text.split(' / ')[-2])
        book_publisher_list.append(text.split(' / ')[-3])

    _comment_score = soup.find_all('span', class_='rating_nums')
    comment_score_list = [i.text for i in _comment_score]

    lg.info(book_price_list)
    lg.info(book_publish_date_list)
    lg.info(book_publisher_list)
    lg.info(comment_score_list)

    _comment_num = soup.find_all('span', class_='pl')
    comment_num_list = [i.text.strip('(').strip(')').strip().strip('人评价') for i in _comment_num][:-1]
    lg.info(comment_num_list)

    _intro = soup.find_all('span', class_='inq')
    intro_list = [i.text for i in _intro]
    lg.info(intro_list)
    lock = Lock()
    lock.acquire()
    csv.write_body(book_name_list, book_publisher_list, book_publish_date_list, book_price_list, comment_score_list,
                   comment_num_list,
                   intro_list)
    lock.release()


try:
    if not os.path.exists('book.csv'):
        csv = Csv('book.csv')
        headline = ['bookName', 'bookPublisher', 'publishDate', 'bookPrice', 'commentScore', 'commentNum', 'intro']
        csv.write_line(headline)
        args = [i * 25 for i in range(10)]
        pool = ThreadPool(5)
        pool.add_task_list(get_data, args)
        pool.execute_task()

    font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Light.ttc')
    book_info = pd.read_csv('book.csv')
    bookName = [i for i in book_info["bookName"]]
    publisher = [i for i in book_info['bookPublisher']]
    publishDate = [i.split('-')[0].split('年')[0].split('.')[0] for i in book_info["publishDate"]]
    for i, d in enumerate(publishDate):
        if len(d) != 4:
            print(i)
    price = [i.strip('元') for i in book_info["bookPrice"]]
    commentScore = [float(i) * 10000 for i in book_info["commentScore"]]
    commentNum = [int(i) for i in book_info["commentNum"]]
    #
    data = {
        'Name': Series(bookName),
        'Publisher': Series(publisher),
        'PublishDate': Series(publishDate),
        'Price': Series(price),
        'CommentScore': Series(commentScore),
        'CommentNum': Series(commentNum)
    }
    df = pd.DataFrame(data)

    _year = df.groupby(by='PublishDate').count()["Name"]
    index = [i for i in _year.index]
    lg.sp(index)
    book_num = [i for i in _year]
    plt.figure(figsize=(14, 6), dpi=80)
    plt.plot(index, book_num, linestyle="-.", label="BookNum")
    plt.xlabel("Year")
    plt.ylabel("bookNum")
    plt.xticks(range(len(index)), font_properties=font, rotation=45)
    plt.title("doubantushu")
    plt.legend()  # 图例
    plt.savefig('PublishDate-BookNum')
    plt.show()

    _y = df.groupby(by='Publisher').count()["Name"]
    plt.figure(figsize=(14, 6), dpi=80)
    x_label = [i for i in _y.index]
    y_book_num = [i for i in _y]
    x = range(len(x_label))
    plt.bar(x, y_book_num, width=0.4, alpha=0.8, color='blue', label="BookNum")
    plt.xlabel("Publisher")
    plt.ylabel("BookNum")
    plt.xticks(x, x_label, font_properties=font, rotation=45)
    plt.title("Publisher-BookNum")
    plt.legend()
    plt.savefig('Publisher-BookNum')
    plt.show()

except:
    lg.error()
