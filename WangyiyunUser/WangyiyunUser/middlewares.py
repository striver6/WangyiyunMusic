# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import signals
import random
# 第三方框架，可以产生各种headers
from fake_useragent import UserAgent


class WangyiyunuserSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WangyiyunuserDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 添加消息头
class RandomUserAgent(object):
    def __init__(self):
        super(RandomUserAgent,self).__init__()
        #实例化方法
        self.ua=UserAgent()
    def process_request(self,request, spider):
        #这里的header是由框架产生的，也可以自己写
        random_type=self.ua.chrome
        request.headers.setdefault("User-Agent",random_type)
class ProxyMiddlleWare(object):
    def __init__(self):
        super(ProxyMiddlleWare,self).__init__()
    def process_request(self,request,spider):
        # 得到地址
        proxy=self.get_Random_Proxy()
        print(proxy+"**********")
        # 设置代理
        request.meta['proxy']=proxy
    #这个方法是从文档中读取id地址
    def get_Random_Proxy(self):
        with open(r"G:\1.txt",'r') as file:
            text=file.readlines()
        proxy = random.choice(text).strip()
        return proxy
    def process_response(self,request,response,spider):
        #如果该ip不能使用，更换下一个ip
        if response.status!=200:
            proxy = self.get_Random_Proxy()
            print('更换ip'+proxy)
            request.meta['proxy'] = proxy
            return request
        return response
