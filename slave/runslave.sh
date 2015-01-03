#!/bin/bash

apt-get install python-pip redis-tools
pip install -r requirements.txt
cd ../crawler && scrapy crawl xysites