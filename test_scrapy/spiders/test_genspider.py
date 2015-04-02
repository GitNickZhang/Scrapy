# -*- coding: utf-8 -*-
import scrapy


class TestGenspiderSpider(scrapy.Spider):
    name = "test_genspider"
    allowed_domains = ["tuotuozyx.com"]
    start_urls = (
        'http://www.tuotuozyx.com/',
    )

    def parse(self, response):
        pass
