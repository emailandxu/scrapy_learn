# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KmustSpiderCrawlSpider(CrawlSpider):
    name = 'kmust_spider_crawl'
    allowed_domains = ['kmust.edu.cn']
    start_urls = ['http://www.kmust.edu.cn/html/xyxw/5.html']

    # 这里不太一样
    # follw 是不是需要跟进到下一页
    rules = (
        Rule(LinkExtractor(allow=r'.+html/xyxw/\d\.html'), follow=True),
        Rule(LinkExtractor(allow=r'.+html/xyxw/\d{4}/\d{2}/\d{2}/.+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print("访问",response.url)
