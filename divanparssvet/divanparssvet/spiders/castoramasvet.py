import scrapy


class DivansvetSpider(scrapy.Spider):
    name = "divansvet"

    allowed_domains = ["https://www.castorama.ru"]
    start_urls = ["https://www.castorama.ru/lighting/interior-lighting/"]

    def parse(self, response):
        svet_page = response.css('li.product-card')
        for svet in svet_page:
            yield {
                'name': svet.css('a.product-card__name').attrib['title'],
                'price': svet.css('div.pY3d2 span::text')[3].get(),  # ценв в четвертом элементе
                'link': svet.css('a.product-card__name').attrib['href']
            }
