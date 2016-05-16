#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from spiderman.items import XinItem
class XinSpider(scrapy.Spider):
    name = 'xin'
    allowed_domains = ['xin.com']
    start_urls = []
    baseurl = 'http://www.xin.com/nanjing/s/a16o2i'
    for i in range(1, 51):
        url = baseurl + str(i) + "v1?channel=bdsem"
        start_urls.append(url)

    def parse(self, response):
        for sel in response.xpath('/html/body/div[3]/div[2]/div[2]/div'):
            item = XinItem()
            item['title'] = sel.xpath('div/p/a/text()').extract()
            item['price'] = sel.xpath('div[3]/em/text()').extract()
            item['url'] = sel.xpath('div/p/a/@href').extract()
            item['image_urls'] = response.css('div.vtc-img a img.lazy::attr(data-original)').extract()
            item['registerTime'] = sel.xpath('div[2]/div[1]/ul/li[1]/text()').extract()
            item['tableDisplayMileage'] = sel.xpath('div[2]/div[1]/ul/li[2]/text()').extract()
            item['gearbox'] = sel.xpath('div[2]/div[1]/ul/li[3]/text()').extract()
            item['saleCity'] = sel.xpath('div[2]/div[1]/ul/li[4]/text()').extract()
            yield item
