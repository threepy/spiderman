# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class SpidermanPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='toor',
        db='spider', charset='utf8')
        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        if spider.name == 'dmoz':
            self.cursor.execute('delete from books')
            self.conn.commit()

    def process_item(self, item, spider):
        if spider.name == 'dmoz':
            if item['title']:
                if item['link']:
                    if item['desc']:
                        sql = 'insert into books VALUES (%s, %s, %s)'
                        param = (item['title'][0], item['link'][0], item['desc'][1])
                        self.cursor.execute(sql, param)
                        self.conn.commit()
                return item
        else:
            return item

    def close_spider(self, spider):
        self.conn.close()


class XinSpiderPipeline(SpidermanPipeline):
    def open_spider(self, spider):
        if spider.name == 'xin':
            self.cursor.execute('delete from forSaleTable')
            self.conn.commit()

    def process_item(self, item, spider):
        if spider.name == 'xin':
            sql = 'insert into forSaleTable(title, price, url, ImgUrl, registerTime, tableDisplayMileage, gearbox, saleCity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            param = (item['title'][0], item['price'][0], item['url'][0], item['image_urls'][0],
                     item['registerTime'][0], item['tableDisplayMileage'][0], item['gearbox'][0], item['saleCity'][0])
            self.cursor.execute(sql, param)
            self.conn.commit()
            return item
        else:
            return item

