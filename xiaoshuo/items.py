# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    c_name = scrapy.Field()
    novel_name = scrapy.Field()
    content = scrapy.Field()

