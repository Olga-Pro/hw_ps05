import scrapy


class DivansvetSpider(scrapy.Spider):
    name = "divansvet"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        pass
