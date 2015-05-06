# -*- coding: utf-8 -*-
import scrapy


class testspider(scrapy.spider):
    name = "test" # spider's id
    allowed_domains = ["tuotuozyx.com"]
    start_urls = (
        'http://www.tuotuozyx.com/',
    )

    def parse(self, response):
        pass

