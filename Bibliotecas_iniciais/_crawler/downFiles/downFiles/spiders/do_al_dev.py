import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem


class DoAlSpider(CrawlSpider):
    name = 'do_al_dev'
    allowed_domains = ['imprensaoficial.al.gov.br']
    start_urls = ['https://imprensaoficial.al.gov.br/diario-oficial/']

    
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DOItem()
        # item['domain_id'] = response.css('div.info h4 a::attr(onclick)').extract()
        file_url =  response.css('a.text-light::attr(href)').get()
        item['file_urls'] = response.urljoin(file_url)
        item['original_file_name'] = "DOAL - " #+ response.css('h1.fs-base.mb-0::text').get()
        item['save_folder'] = 'Alagoas' # file_url.re(r'https.*.pdf').split('/')[-1]
        yield item


