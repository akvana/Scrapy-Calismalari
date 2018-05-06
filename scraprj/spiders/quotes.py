# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/',
        ]
        for urlx in urls:
            yield scrapy.Request(url=urlx, callback=self.parse)




    def detail_parse(self,response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        item={'author_name': response.css('.author-title::text').extract_first(),
                'texts': response.css('.author-description::text').extract_first(),
                }
            #print('BASLIK',item['tags'][0])
        yield(item)




    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        for quote in response.css('div.quote'):
            item={'author_name': quote.css('.author::text').extract_first(),
                    'texts': quote.css('.text::text').extract_first(),
                    'tags': quote.css('.tag::text').extract(),
                    }
            #print('BASLIK',item['tags'][0])
            #yield(item)
        next_detail_url= response.css('div.quote >  span > a ::attr(href)').extract()
        for url in next_detail_url:
            if next_detail_url:
                next_detail_url=response.urljoin(url)
                print('#####################################', next_detail_url,'#####################################')
                yield scrapy.Request(url=next_detail_url,callback=self.detail_parse)

        next_page_url= response.css('li.next > a ::attr(href)').extract_first()
        if next_page_url:
            next_page_url=response.urljoin(next_page_url)
            print('#####################################', next_page_url,'#####################################')
            yield scrapy.Request(url=next_page_url,callback=self.parse)
