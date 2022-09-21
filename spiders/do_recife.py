import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem


class DoRecifeSpider(CrawlSpider):
    name = 'do_recife'
    allowed_domains = ['dome.recife.pe.gov.br']
    start_urls = ['https://dome.recife.pe.gov.br/dome/buscar.php']

    rules = (
        Rule(LinkExtractor(allow=r'dome/buscar.php'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DOItem()
        # item['domain_id'] = response.css('div.info h4 a::attr(onclick)').extract()
        file_url = response.css('div.info h4 a::attr(onclick)').re(r'https.*assinado.pdf')
        item['file_urls'] = file_url
        item['save_folder'] = 'Recife' # file_url.re(r'https.*.pdf').split('/')[-1]
        yield item

