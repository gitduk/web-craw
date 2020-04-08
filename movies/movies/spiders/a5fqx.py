# -*- coding: utf-8 -*-
import os

import scrapy

from ..items import MovieItem


class A5fqxSpider(scrapy.Spider):
    name = '5fqx'
    allowed_domains = ['5fqx.com/index.html']
    prefix = "https://5fnj.com/arc/west/list_4_{}.html"
    url_list = []
    for i in range(1, 111):
        url = prefix.format(i)
        url_list.append(url)
    start_urls = url_list

    # start_urls = ['https://5fqx.com/arc/mainland/list_1_1.html']

    def parse(self, response):
        movies = response.xpath("//div[@class='tc_nr']/ul/li")
        for i in movies:
            movie = MovieItem()
            movie["title"] = i.xpath("div[@class='w_z']/h3/a/text()").extract()
            movie["img_url"] = i.xpath("div[@class='t_p']/a/img/@data-original").extract()
            movie["video_html_url"] = i.xpath("div[@class='w_z']/h3/a/@href").extract()
            yield movie
