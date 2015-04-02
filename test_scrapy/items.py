# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
<<<<<<< HEAD
=======
from scrapy.item import Item,Field
>>>>>>> 00be01d4e754ce37da0222504c8707ade39c1db3


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
<<<<<<< HEAD
    pass
=======
    title = Field()
    author = Field()
>>>>>>> 00be01d4e754ce37da0222504c8707ade39c1db3
