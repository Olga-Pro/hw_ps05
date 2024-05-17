import scrapy


class DivansvetSpider(scrapy.Spider):
    name = "divansvet"
    # allowed_domains = ["https://divan.ru"]
    # start_urls = ["https://www.divan.ru/category/svet"]

    allowed_domains = ["https://leroymerlin.ru"]
    start_urls = ["https://leroymerlin.ru/catalogue/osveshchenie/"]

    def parse(self, response):
        svet_page = response.css('div.lsooF')
        for svet in svet_page:
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'link': svet.css('a').attrib['href']
            }
