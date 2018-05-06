# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = "login"
    login_url='http://quotes.toscrape.com/login'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/login',
        ]
        for urlx in urls:
            yield scrapy.Request(url=urlx, callback=self.parse)
    def parse(self, response):
        token= response.css('input[name="csrf_token"]::attr(value)').extract_first()
        print(token)
        data={
        'csrf_token':token,
        'username':'abc',
        'password':'abc',
        }
        yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.parse_quotes)

    def parse_quotes(self, response):
        for q in response.css('div.quote'):
            yield{
            'author_url':q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()

            }
