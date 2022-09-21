import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem

class DoRnSpider(CrawlSpider):
    name = 'do_rn'
    allowed_domains = ['diariooficial.rn.gov.br']
    start_urls = ['http://diariooficial.rn.gov.br/dei/dorn3/']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DOItem()
        file_url = response.css('a::attr(href)').re(r'http.*.pdf')
        item['file_urls'] = file_url
        item['save_folder'] = 'Rio_G_do_Norte'
        yield item
