# -*- coding: UTF-8 -*-
import re
import scrapy
import requests
from scrapy.http import Request
# from taobao.items import TaobaoItem
import redis
import time


class Myspider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ["taobao.com"]
    start_url = 'https://www.taobao.com'


    # def start_requests(self):
    #     html = requests.get('https://www.taobao.com')
    #     r = redis.Redis(host='localhost', port=6379, db=0)
    #     list = re.findall(r'<a href="(.*?)" data-cid="1" data-dataid="', html.text)
    #
    #
    #     print list.__len__()
    #     for i in list:
    #         r.rpush("foo_list5", i)
    #         # print i
    #         if i.startswith('https'):
    #             yield Request(i, self.parse)
    #         else:
    #             yield Request("https:"+i, self.parse)
    #     # yield Request("https://www.taobao.com/markets/nanzhuang/2017new", self.parse)
    #
    #
    # def parse(self, response):
    #     # print(response.text)
    #     r = redis.Redis(host='localhost', port=6379, db=0)
    #     goods_lsit = re.findall(r'<a href="(.*?)" target="_blank"', response.text)
    #     for b in goods_lsit:
    #         # print b
    #         goods_num = re.search(r'id=(\d){12}', b)
    #         if goods_num:
    #             print goods_num.group(0)
    #             r.rpush("goods_list", goods_num.group(0))
    # #             yield Request("https://item.taobao.com/item.htm?"+goods_num.group(0), callback=self.goods)
    # #
    # #
    # #
    # # def goods(self, response):
    # #     r = redis.Redis(host='localhost', port=6379, db=0)
    # #     shop_num = re.search(r'//[^w][0-9a-zA-Z]{0,20}\.taobao\.com', response.text)
    # #     if shop_num:
    # #         print shop_num.group()
    # #         r.rpush("shop_num", shop_num.group())


#
    # def start_requests(self):
    #     r = redis.Redis(host='localhost', port=6379, db=0)
    #     goods_list = r.llen('goods_list')
    #     for index in xrange(goods_list):
    #         goods_name = r.lindex("goods_list", index)
    #         print goods_name
    #         time.sleep(2)
    #         yield Request("https://item.taobao.com/item.htm?" + goods_name, self.parse)
    #
    # def parse(self, response):
    #     r = redis.Redis(host='localhost', port=6379, db=0)
    #     shop_num = re.search(r'"//[^w][0-9a-zA-Z]{0,20}\.taobao\.com"', response.text)
    #     if shop_num:
    #         print shop_num.group()
    #         r.rpush("shop_num", shop_num.group())


#
    def start_requests(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        shop_list = r.llen('shop_num')
        for index in xrange(shop_list):
            shop_name = r.lindex('shop_num', index)
            print shop_name
            time.sleep(2)
            yield Request("https:"+shop_name.strip('"'),self.parse)
        # yield Request("https://shop105514755.taobao.com/", self.parse)
    def parse(self, response):
        r = redis.Redis(host='localhost', port=6379, db=0)
        shop_information = re.search(r'target="_blank" href="(.*?)" id="miniDSR"', response.text)
        if shop_information:
            print shop_information.group(1)
            r.rpush('shop_introduce',shop_information.group(1))


            # yield Request("https:"+shop_information.group(1), callback=self.loading_shop)

    # def loading_shop(self, response):
    #     shop_name = re.search(r'class="J_TGoldlog" data-goldlog-id="/tbwmdd.1.044">(.*?)<i id="J_TEnterShop', response.text)
    #     shop_zhuying = re.search(r'<li>当前主营：<a href=".*?target="_blank">&nbsp;(.*?)</a></li>', response.text)
    #     shop_home = re.search(r'<li>所在地区：(.*?)</li>', response.text)
    #     if shop_home:
    #         print shop_home.group()
    #     if shop_name:
    #         print shop_name.group(1)
    #     if shop_zhuying:
    #         print shop_zhuying.group(1)










