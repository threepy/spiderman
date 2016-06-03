# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class SpidermanPipeline(object):
    def __init__(self):
        dbargs = settings.get('DB_CONNECT')
        db_server = settings.get('DB_SERVER')
        dbpool = adbapi.ConnectionPool(db_server, **dbargs)
        self.dbpool = dbpool

    def __del__(self):
        try:
            self.dbpool.close()
        except Exception:
            pass

    def open_spider(self, spider):
        if spider.name == 'dmoz':
            delSQL = 'delete from books'
            self.dbpool.runOperation(delSQL)

    def process_item(self, item, spider):
        if spider.name == 'dmoz':
            if item['title']:
                if item['link']:
                    if item['desc']:
                        sql = 'insert into books VALUES (%s, %s, %s)'
                        param = (item['title'][0], item['link'][0], item['desc'][1])
                        self.dbpool.runOperation(sql, param)
                return item
        else:
            return item

class XinSpiderPipeline(SpidermanPipeline):
    def open_spider(self, spider):
        if spider.name == 'xin':
            self.dbpool.runOperation('delete from forsaletable')

    def process_item(self, item, spider):
        if spider.name == 'xin':
            sql = 'insert into forSaleTable(title, price, url, ImgUrl, registerTime, tableDisplayMileage, gearbox, saleCity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            param = (item['title'][0], item['price'][0], item['url'][0], item['image_urls'][0],
                     item['registerTime'][0], item['tableDisplayMileage'][0], item['gearbox'][0], item['saleCity'][0])
            self.dbpool.runOperation(sql, param)
            return item
        else:
            return item

class DoubanMoviePipeline(SpidermanPipeline):
    def open_spider(self, spider):
        if spider.name == 'doubanmovie':
            self.dbpool.runOperation('delete from doubanmovie')
            
    def process_item(self, item, spider):
        if spider.name == 'doubanmovie':
            sql = 'insert into doubanmovie (id, name, year, score, director, classification, actor, introd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            param = (int(item['id'][0].split(".")[1]), item['name'][0], item['year'][0], item['score'][0], item['director'][0],item['classification'][0], ' '.join(item['actor']), item['introd'][0])
            self.dbpool.runOperation(sql, param)
            return item
        else:
             return item
             