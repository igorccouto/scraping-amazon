# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['https://amazon.com']
    start_urls = ['http://https://amazon.com/']

    def parse(self, response):
        pass
