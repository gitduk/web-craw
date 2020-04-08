# -*- coding: utf-8 -*-
import scrapy
from ..items import QianchengwuyouItem


class WuyouSpider(scrapy.Spider):
    name = 'wuyou'
    allowed_domains = ['xy.51job.com/default-xs.php']
    prefix = 'https://search.51job.com/list/000000,000000,0600,00,3,99,%2B,2,{}.html?lang=c&stype=1&postchannel=100000&workyear=01&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    urls = []
    for i in range(1, 85):
        urls.append(prefix.format(str(i)))

    start_urls = urls

    def parse(self, response):
        items = response.xpath("//div[@class='el']")
        print(items)
        for i in items:
            print('-' * 100)
            wyou = QianchengwuyouItem()
            wyou['position'] = i.xpath("p/span/a/@title").extract()
            wyou['company_name'] = i.xpath("span[@class='t2']/a/@title").extract()
            wyou['location'] = i.xpath("span[@class='t3']/text()").extract()
            wyou['money'] = i.xpath("span[@class='t4']/text()").extract()
            wyou['date'] = i.xpath("span[@class='t5']/text()").extract()
            wyou['link'] = i.xpath("p/span/a/@href").extract()
            print('\n')
            yield wyou
