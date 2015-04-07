# -*- coding: utf-8 -*-

import scrapy
from test_scrapy.items import TestScrapyItem
from bs4 import BeautifulSoup
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class LofterSpider(scrapy.Spider):
	name = 'wooyun'
	allow_domains = ['drops.wooyun.org']
	start_urls = ['http://drops.wooyun.org/']

	def parse(self, response):
		# filename = 'test.html'
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)

		soup = BeautifulSoup(response.body)
		post_divs = soup.find_all('div', class_='post')
		items = []
		for post_div in post_divs:
			title = post_div.find('h2').get_text()
			item = TestScrapyItem()
			item['title'] = title
			items.append(item)	
		# for content_div in content_divs:
		# 	content = content_div.get_text()
		# 	item = TestScrapyItem()
		# 	item['content'] = content
		# 	items.append(item)
		# 	print content

		return items