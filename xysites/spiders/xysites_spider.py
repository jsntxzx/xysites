#!/usr/bin/env python
# encoding: utf-8
# Author: xiang

from scrapy.spider import Spider
from scrapy.http import Request
from xysites.items import XysitesItem

class NinemouthSpider(Spider):
    name = "xysites"
    allowed_domains = ["34yu.com"]
    start_urls = [
#                  u'http://34yu.com/tupian/xiyangnvsaomei/', 
#                  u'http://34yu.com/tupian/dongfangnvjizhongying/', 
                   u'http://34yu.com/tupian/wangyouzipaitietuqu/' ,
#                  u'http://34yu.com/tupian/katongtietuqu/',
#                  u'http://34yu.com/tupian/gaogenmeizusiwazhuanqu/',
                  ]
    base_url = u'http://34yu.com'
    imgbase_url = u'http://pictureimg.info/imgdat/'

    def parse(self, response):
        nextpage_url = response.xpath('//div[@class="wp-pagenavi"]/a[@id="nextpagelink"]/@href').extract()
        content_urls = response.xpath('//div[@class="project-desc"]/p/b/a/@href').extract()
        if len(nextpage_url) == 1 :
            next_link = self.base_url + nextpage_url[0]
            yield Request(url=next_link, callback=self.parse)

        for content_url in content_urls:
            content_link = self.base_url + content_url 
            yield Request(url=content_link, callback=self.parse_content)

    def parse_content(self , response):
        
        folder = response.xpath('//div[@class="title"]/text()').extract()[0]
        mystring = response.xpath('//div[@class="singleinfo"]/text()').extract()[0].strip('\r\n').split(',')
        prefix = mystring[0]
        for substr in mystring[1:]:
            item = XysitesItem()
            item['folderName'] = folder
            item['imageUrl'] = self.imgbase_url + prefix + '/' + substr
            yield item