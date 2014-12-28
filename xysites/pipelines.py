# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xysites.items import XysitesItem
import os
import requests

class XysitesPipeline(object):
    def process_item(self, item, spider):
        base = 'images/'
        category = item['folderName']
        url = item['imageUrl']
        if not os.path.exists(base + category) :
            os.makedirs(base + category)
        name = base+category+'/'+ url.split('/')[-1]
        if not os.path.exists(name) :
            self.download(url , name)
        return item

    def download(self, url, name):
        with open(name ,'wb') as h :
            response = requests.get(url,stream = True)
            for block in response.iter_content(1024):
                if not block:
                    break;
                h.write(block)
