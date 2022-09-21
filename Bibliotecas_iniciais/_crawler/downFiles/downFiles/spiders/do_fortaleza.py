import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoFortalezaSpider(CrawlSpider):
    name = 'do_fortaleza'
    allowed_domains = ['diariooficial.fortaleza.ce.gov.br']
    start_urls = ['http://diariooficial.fortaleza.ce.gov.br/?num-diario=&content-diario=&ano-diario=2022&mes-diario=&captcha=t7gq2x&current=']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
