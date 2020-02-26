# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import json

class AsosSpider(Spider):
    name = 'asos'
    allowed_domains = ['asos.com']
    start_urls = ['https://www.asos.com/men/shoes-boots-trainers/boots/cat/?cid=5774'
                  '&nlid=mw%7Cshoes%7Cshop%20by%20product&page=1']

    def parse(self, response):
        products = response.xpath('//article[@data-auto-id="productTile"]/a/@href').extract()
        for product in products:
            yield Request(product,
                          callback=self.parse_shoe)

        next_page = response.xpath('//a[text()="Load more"]/@href').extract_first()
        if next_page:
            yield Request(next_page,
                          callback=self.parse)

    def parse_shoe(self, response):
        product_name = response.xpath('//h1/text()').extract_first()
        product_id = response.url.split('/prd/')[1].split('?')[0]
        price_api_url = 'https://www.asos.com/api/product/catalogue/v3/stockprice?productIds=' \
                        + product_id + '&store=ROE&currency=EUR'

        yield Request(price_api_url,
                      meta={'product_name': product_name},
                      callback=self.parse_shoe_price)

    def parse_shoe_price(self, response):
        json_resp = json.loads(response.body.decode('utf-8'))
        price = json_resp[0]['productPrice']['current']['text']

        yield {'product_name': response.meta['product_name'],
               'price': price, }