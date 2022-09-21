import scrapy
from urllib import request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem


class DoSalvadorSpider(CrawlSpider):
    name = 'do_salvador'
    allowed_domains = ['dom.salvador.ba.gov.br']
    start_urls = ['http://www.dom.salvador.ba.gov.br/']

    rules = (
        Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DOItem()
        # item['domain_id'] = response.css('div.info h4 a::attr(onclick)').extract()
        file_url = response.css('a.thumbsup-thumb img::attr(src)').getall() #.re(r'https.*assinado.pdf')
        item['file_urls'] = [response.urljoin(file_uri)+'.pdf' for file_uri in file_url] 
        item['save_folder'] = 'Salvador' # file_url.re(r'https.*.pdf').split('/')[-1]
        yield item

