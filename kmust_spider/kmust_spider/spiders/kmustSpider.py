# -*- coding: utf-8 -*-
import scrapy
from kmust_spider.items import KmustSpiderItem
from pdb import set_trace

class KmustspiderSpider(scrapy.Spider):
    name = 'kmustSpider'
    allowed_domains = ['kmust.edu.cn']
    start_urls = ['http://www.kmust.edu.cn/html/xyxw/5.html']
    root_url = "http://www.kmust.edu.cn/"

    def parse(self, response):
        url_els = response.xpath("//div[@id='NewsListmain']/ul")
        # set_trace()
        for url_el in url_els:
            time_str = url_el.xpath(".//span[@class='Only_time']/text()").extract()[0]
            title = url_el.xpath(".//span[@class='Only_title']/text()").extract()[0]
            news_links_relUrl = url_el.xpath(".//span[@class='Only_title']/a/@href").extract()[0]
            request_url= self.root_url + news_links_relUrl

            # print(time_str,title,request_url)

            yield scrapy.Request(url = request_url, callback=self.parse_second, meta={"info":(title,time_str)})

        # find next page url
        next_page_relUrl = response.xpath("//div[@class='pageChange']/a[3]/@href")

        # crawl next page
        # yield scrapy.Request(url = self.root_url+next_page_relUrl,callback=self.parse)

    def parse_second(self, response):
        title,time_str = response.meta['info']
        content = response.xpath("//div[@class='HOPE_Content']/text()")
        item = KmustSpiderItem()
        item['title'] = title
        item['content'] = content
        item['time'] = time_str