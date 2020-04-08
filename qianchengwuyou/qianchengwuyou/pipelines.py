# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from openpyxl import Workbook
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from .spiders.tfunc import SQL

Base = declarative_base()


class Wuyou(Base):
    __tablename__ = 'wuyou'
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String(50))
    company_name = Column(String(50))
    location = Column(String(50))
    link = Column(String(100))
    money = Column(String(10))
    date = Column(String(10))


class QianchengwuyouPipeline(object):
    def process_item(self, item, spider):
        data_list = []
        for i in item:
            data_list.extend(item[i])

        if len(data_list) == 6:
            print(data_list)
            sql = SQL('root', '123456', '3306', 'homework', 'utf8', Base)
            w = Wuyou(position=data_list[0], company_name=data_list[1], location=data_list[2], money=data_list[3],
                      date=data_list[4], link=data_list[5])
            sql.write(w)

        return item
