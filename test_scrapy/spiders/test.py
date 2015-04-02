# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = "test" # spider's id
    allowed_domains = ["tuotuozyx.com"]
    start_urls = (
        'http://www.tuotuozyx.com/',
    )

    def parse(self, response):
   	    pass