#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spiderman.items import DoubanMovieItem

class MyCrawlerSpider(CrawlSpider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    rules = (
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+&filter='))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+[/]')), callback='parse_item'),
    )

    def parse_item(self, response):
        item = DoubanMovieItem()
        item['id'] = response.xpath('//div[@id="content"]/div/span[@class="top250-no"]/text()').extract()
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = response.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['classification'] = response.xpath('//span[@property="v:genre"]/text()').extract()
        item['actor'] = response.xpath('//span/a[@rel="v:starring"]/text()').extract()
        item['introd'] = response.xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div//span[@property="v:summary"]/text()').extract()
        return item
        