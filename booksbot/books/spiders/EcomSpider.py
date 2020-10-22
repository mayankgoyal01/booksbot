import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest


# class Allproductsurl(scrapy.Item):
#     item_name = scrapy.Field()
#     all_product_url = scrapy.Field()

class Product(scrapy.Item):
    product_url = scrapy.Field()
    MRP = scrapy.Field()
    SP = scrapy.Field()
    description = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    cat_url = scrapy.Field()
    page_url = scrapy.Field()


class EcomSpider(scrapy.Spider):
    name = 'EcomSpider'
    start_urls = ['https://www.jiomart.com/c/groceries/personal-care/91']
    headers = {
        'X-Crawlera-Cookies': 'disable',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    # start_urls = ['https://www.jiomart.com/p/groceries/lux-soft-touch-bar-soap-150-g-pack-of-3/490915877']

    # def parse(self, response):

        # url = 'https://www.jiomart.com/c/groceries/personal-care/91'
        # formdata = {'rel_pincode': '301001'}
        # yield SplashFormRequest.from_response(
        #     response,
        #     url=url,
        #     formdata=formdata,
        #     callback=self.parse_links,
        #     args={'wait': 3}
        # )

    def parse(self, response):
        for each_cat in response.css("li.o-menu > ul > li > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(each_cat), callback=self.parse_catpage, headers={'referer_url': response.urljoin(each_cat)})
 
    def parse_catpage(self, response):
        for product_url in response.css("div.cat-item > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.parse_product_page, headers={
                'referer_url': response.request.headers.get('referer_url'),
                'referer2_url': response.url
                })
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse_catpage, headers={
                })


    def parse_product_page(self, response):


        item = Product()
        item['product_url'] = response.url
        item['MRP'] = response.xpath("//div[@class='price-box']/span[@class='price']/strike/text()").get()
        item['description'] = response.xpath("//div[@class='feat_detail']/div[@class='content_txt']/p/text()").get()
        item['SP'] = response.xpath("//div[@class='price-box']/span[@class='final-price']/span/text()").get()
        item['title'] = response.xpath("//div[@class='title-section']/h1/text()").get()
        item['img_url'] = response.xpath("//div[@class='swiper-wrapper']//img/@src").get(0)
        item['cat_url'] = response.request.headers.get('referer_url')
        item['page_url'] = response.request.headers.get('referer2_url')
        return item

