#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DoubanMovieItem

class MyCrawlerSpider(CrawlSpider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    rules = (
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')), callback='parse_item'),
    )

    def parse_item(self, response):
        item = DoubanMovieItem()
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score']=sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        item['director']=sel.xpath('//*[@id="info"]/span[1]/a/text()').extract()
        item['classification']= sel.xpath('//span[@property="v:genre"]/text()').extract()
        item['actor']= sel.xpath('//*[@id="info"]/span[3]/a[1]/text()').extract()
        return item