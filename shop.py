import re
import scrapy
import requests
from scrapy.http import Request
# from taobao.items import TaobaoItem
import redis
import time

class shop_Myspider(scrapy.Spider):
    name = 'shop'
    # allowed_domains = ["taobao.com"]
    # start_url = 'https://www.taobao.com'

    def start_requests(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        goods_list = r.llen('goods_list')
        for index in xrange(goods_list):
            goods_name = r.lindex("goods_list", index)
            print goods_name
            time.sleep(2)
            yield Request("https://item.taobao.com/item.htm?" + goods_name, self.parse)

    def parse(self, response):
        r = redis.Redis(host='localhost', port=6379, db=0)
        shop_num = re.search(r'"//[^w][0-9a-zA-Z]{0,20}\.taobao\.com"', response.text)
        if shop_num:
            print shop_num.group()
            # r.rpush("shop_num", shop_num.group())