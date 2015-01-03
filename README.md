## Redis-based Scrapy Spider ##

This project attempts to use scrapy and redis to get images from a website.

###Features:###

Distributed crawling/scraping
You can start multiple spider instances that share a single redis queue. Best suitable for broad multi-domain crawls.

Distributed post-processing
Scraped items gets pushed into a redis queued meaning that you can start as many as needed post-processing processes sharing the items queue.

###Requirements:###
* scrapy==0.24.4
* requests==2.2.1
* service_identity==14.0.0
* scrapy_redis==0.5.2

###Usage:###

first

    git clone git://github.com/jsntxzx/xysites.git

To run this on one machine:
   

    cd xysites/master
    ./master_init.sh
    cd ../crawler
    scrapy crawl xysites
    

To run this on multiple machines:

master machine : run above code

slave machine : 

    cd xysites/slave
    ./slave_init.sh
    cd ../crawler
    scrapy crawl xysites
	
	



	