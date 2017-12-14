# -*- coding: UTF-8 -*-
import re
import scrapy
import requests
from scrapy.http import Request
# from taobao.items import TaobaoItem
import redis
import time

class Shop_imformation_spider(scrapy.Spider):
    name = 'shop_infromation'

    def start_requests(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        shop_introduce = r.llen('shop_introduce')
        for index in xrange(shop_introduce):
            shop_introduce = r.lindex("shop_introduce", index)
            print shop_introduce
            yield Request("https:"+shop_introduce, callback=self.parse)

    def parse(self, response):
        # print response.text
        shop_name = re.search(r'data-goldlog-id="/tbwmdd\.1\.044">(.*?)<i id="J_TEnterShop', response.text)
        shop_zhuying = re.search(r'<li>当前主营：<a href=".*?target="_blank">&nbsp;(.*?)</a></li>', response.text)
        shop_home = re.search(r'<li>所在地区：(.*?)</li>', response.text)
        if shop_home:
            print shop_home.group()

        if shop_name:
            print shop_name.group(1)
        if shop_zhuying:
            print shop_zhuying.group(1)