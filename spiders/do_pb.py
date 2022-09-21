import scrapy
import locale
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem
from downFiles.pipelines import DOPipeline

class DoPbSpider(CrawlSpider):
    name = 'do_pb'
    locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')
    hoje = datetime.now().strftime('%d/%m/%Y')
    ano_mes = datetime.strptime(hoje, '%d/%m/%Y').strftime('%Y/%B')
    allowed_domains = ['auniao.pb.gov.br']
    start_urls = [f'http://auniao.pb.gov.br/servicos/doe/{ano_mes}']

    rules = (
        Rule(LinkExtractor(allow=r'junho/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DOItem()
        file_url = response.css('a.contenttype-file::attr(href)').re(r'https.*.pdf') #.strip('/view')
        item['file_urls'] = file_url
        item['save_folder'] = 'Paraiba'
        yield item