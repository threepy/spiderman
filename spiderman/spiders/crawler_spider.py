#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyCrawlerSpider(CrawlSpider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com']
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log('hi, this an item page. %s' % response.url)
        print 'hello'
        item = scrapy.Item()
        # item['id'] = response.xpah('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # return item