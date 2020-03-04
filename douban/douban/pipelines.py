# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from .tfunc import SQL

Base = declarative_base()


class Douban(Base):
    __tablename__ = 'DB'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer)
    title = Column(String(10))
    link = Column(String(50))
    rating = Column(Integer)


class DoubanPipeline(object):
    def process_item(self, item, spider):
        sql = SQL(user='root', password='123456', port='3306', dbname='homework', char='utf8', base=Base)
        douban_movie = Douban(rank=item["rank"], title=item["title"][0], link=item["link"], rating=item["rating"])
        sql.write(douban_movie)
        print('-' * 100)
        return item
