# -*- coding: utf-8 -*-

# Scrapy settings for xysites project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'xysites'

SPIDER_MODULES = ['xysites.spiders']
NEWSPIDER_MODULE = 'xysites.spiders'

ITEM_PIPELINES = {'xysites.pipelines.XysitesPipeline':1,}

DOWNLOADER_MIDDLEWARES = {
       'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
       'xysites.rotate_useragent.RotateUserAgentMiddleware': 400,
	   }


DOWNLOAD_DELAY = 0.25
COOKIES_ENABLED = False