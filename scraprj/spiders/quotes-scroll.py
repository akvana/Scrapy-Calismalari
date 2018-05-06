# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesScrollSpider(scrapy.Spider):
    name = "quotesscroll"
    api_url='http://quotes.toscrape.com/api/quotes?page={}'
    urls = [
        api_url.format(1)
    ]
    def start_requests(self):


        for urlx in self.urls:
            yield scrapy.Request(url=urlx, callback=self.parse)


    def parse(self, response):
        data = json.loads(response.text)
        for quotes in data['quotes']:
            item= {
            'author_name':quotes['author']['name'],
            'text':quotes['text'],
            'tags':quotes['tags'],
            }
            yield item
        if data['has_next']:
            next_url=data['page']+1
            yield scrapy.Request(url=self.api_url.format(next_url),callback=self.parse)
