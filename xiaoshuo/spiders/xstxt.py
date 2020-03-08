# -*- coding: utf-8 -*-
import re
import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiaoshuo.items import XiaoshuoItem

#盗版小说网站抓取
class XstxtSpider(CrawlSpider):
    name = 'xstxt'
    allowed_domains = ['sbiquge.com']
    start_urls = ['https://www.sbiquge.com/biqukan/']

    rules = (
        Rule(LinkExtractor(allow="/\d+?_\d+?/", unique=True), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        chap_list = response.xpath(".//*[@class='listmain']/dl/dd")
        novel_name = response.xpath(".//div[@id='book']//div[@id='info']/h1/text()").get()
        for chapter in chap_list:
            c_name = chapter.xpath('./a/text()').get()
            c_url = chapter.xpath('./a/@href').get()
            if c_name:
                item = XiaoshuoItem(c_name=c_name, novel_name=novel_name)
                url = response.urljoin(c_url)
                request = scrapy.Request(url=url, callback=self.parse_content,dont_filter=True)
                request.meta['key'] = item
                yield request


    @staticmethod
    def parse_content(response):
        item = response.meta['key']
        print("<<<<<<<" + item['novel_name'] + '  '+
        item['c_name'] + "      爬取中<<<<<<<<<")
        content_list = response.xpath(".//*[@id='content']/text()").getall()  # 匹配到的是一个列表
        content = ''
        for content1 in content_list:
            content1.replace('\xa0','')
            content1.replace('\r', '')
            content = content + content1
        item['content'] = content
        yield item








