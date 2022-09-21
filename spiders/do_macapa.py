import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem


class DoRecifeSpider(CrawlSpider):
    name = 'do_es'
    allowed_domains = ['ioes.dio.es.gov.br']
    start_urls = ['https://ioes.dio.es.gov.br/portal/login']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    # def parse_item(self, response):
    #     item = DOItem()
    #     # item['domain_id'] = response.css('div.info h4 a::attr(onclick)').extract()
    #     file_url = response.css('a.diary-btn::attr(href)').extract().re(r'https.*pdf')
    #     item['file_urls'] = file_url
    #     item['save_folder'] = 'Macapa' # file_url.re(r'https.*.pdf').split('/')[-1]
    #     yield item

