# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time

class TaobaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from selenium import webdriver
from scrapy.http import HtmlResponse
class JSPageMiddleware(object):
    def  process_request(self, request, spider):
        if spider.name == 'Shop_goods':
            brower = webdriver.PhantomJS()
            # brower = webdriver.Firefox()

            # brower.implicitly_wait(60)
            brower.get(request.url)
            # time.sleep(5)
            # js
            # brower.execute_script("var h=window.innerHeight"
            #                       "document.write(h)"
            #                       "window.scrollBy(0,h/2)")

            brower.execute_script("window.scrollBy(0,3000)")


            time.sleep(5)
            print ("fangwen, (0)".format(request.url))
            time.sleep(1)
            brower.execute_script("window.scrollBy(0,5000)")
            time.sleep(1)

            return HtmlResponse(url=brower.current_url, body=brower.page_source, encoding="utf-8", request=request)
