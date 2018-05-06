# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class QuotesJSSpider(scrapy.Spider):
    name = "jsquotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/js/',
        ]
        for urlx in urls:
            yield SplashRequest(url=urlx, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{

                'text':quote.css('span.text::text').extract_first(),
                'author':quote.css('small.author::text').extract_first(),
                'tags':quote.css('div.tags > a.tag::text').extract_first(),

            }
