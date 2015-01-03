#!/bin/bash
export mip=`ifconfig eth0|grep inet|sed -n '1p'|awk '{print $2}'|awk -F ':' '{print $2}'`
echo $mip 
#modify redis.conf 
sed  -i "/^bind/{s/$/ $mip/}"  /etc/redis/redis.conf
#modify crawler settings
var=$(printf 'REDIS_URL = 'redis://%s:6379/0'' $mip)
echo $var >> ../crawler/xysites/settings.py
redis-server /etc/redis/redis.conf
apt-get install python-pip redis-server
pip install -r requirements.txt
cd ../crawler && scrapy crawl xysites