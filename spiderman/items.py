# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermanItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class XinItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    registerTime = scrapy.Field()
    tableDisplayMileage = scrapy.Field()
    gearbox = scrapy.Field()
    saleCity = scrapy.Field()
    
    
class DoubanMovieItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    classification = scrapy.Field()
    actor = scrapy.Field()
    introd = scrapy.Field()
