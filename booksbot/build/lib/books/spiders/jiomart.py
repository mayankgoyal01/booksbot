# # -*- coding: utf-8 -*-
# import scrapy


# class Jiomart(scrapy.Spider):
#     name = "jiomart"
#     start_urls = [
#         'https://www.jiomart.com/c/groceries/personal-care/91',
#     ]

#     def parse(self, response):
#         for quote in response.xpath('//div[@class="cat-item"]'):
#             yield {
#                 # 'image': quote.xpath('./span[@class="cat-img"]/img[@class="product-image-photo"]/@src').extract_first(),
#                 'text': quote.xpath('./a[@class="cat-img"]/span[@class="clsgetname"]/text()').extract_first(),
#                 # 'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
#             }

#         # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
#         # if next_page_url is not None:
#             # yield scrapy.Request(response.urljoin(next_page_url))
#         print(response)
