# -*- coding: UTF-8 -*-
import re
import scrapy
import requests
from scrapy.http import Request
# from taobao.items import TaobaoItem
import redis
import time

class Shop_goods(scrapy.Spider):
    name = 'Shop_goods'

    def start_requests(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        shop_list = r.llen('shop_num')
        for index in xrange(shop_list):
            shop_name = r.lindex('shop_num', index)
            print shop_name
            yield Request("https:"+shop_name.strip('"')+"/search.htm", self.parse)

    def parse(self, response):
        page = re.search('<span class="page-info">1/(.*?)</span', response.text)
        if page:
            print page.group(1)

        page_goods_num = re.findall(r'id=5\d{11}', response.text)
        for goods in page_goods_num:
            print goods


