# -*- coding: utf-8 -*-
import scrapy

from ..items import DoubanItem


class MovieSpiderSpider(scrapy.Spider):
    name = 'movie-spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        items = response.xpath("//div[@class='item']")
        for i in items:
            movie = DoubanItem()
            movie["rank"] = i.xpath("div[1]/em/text()").extract()
            movie["title"] = i.xpath("div[2]/div[@class='hd']/a/span[@class='title']/text()").extract()
            movie["link"] = i.xpath("div[2]/div[@class='hd']/a/@href").extract()
            movie["rating"] = i.xpath("div[2]/div[2]/div/span[2]/text()").extract()
            yield movie
