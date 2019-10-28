# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company=scrapy.Field()
    job=scrapy.Field()
    address=scrapy.Field()
    others=scrapy.Field()
    url_detail=scrapy.Field()

