
import json
import base64
import scrapy
from scrapy_splash import SplashRequest
from urllib.request import urlretrieve
from scrapy.selector import Selector
class MySpider(scrapy.Spider):
    name='ppm2'
    def start_requests(self):
        splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 0,
        }
        yield SplashRequest(url='https://pythonprogramming.net/parsememcparseface/', callback=self.parse_result)

    # ...
    def parse_result(self, response):
        #imageUrl = xhtml.xpath('/html/body/div[2]/div/div/div/img/@src')
        imageUrl =Selector(text=response.body).xpath('/html/body/div[2]/div/div/div/img/@src').extract_first()
        urlretrieve(imageUrl, "yaptinnnlen.jpg")

        """filename = 'some_image.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)"""
