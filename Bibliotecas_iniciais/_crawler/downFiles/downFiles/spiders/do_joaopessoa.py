import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem


class DoJoaopessoaSpider(CrawlSpider):
    USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    headers = {'User-Agent': USER_AGENT}
    name = 'do_joaopessoa'
    allowed_domains = ['joaopessoa.pb.gov.br']
    start_urls = ['https://www.joaopessoa.pb.gov.br/doe-jp/']
    handle_httpstatus_list = [304]

    rules = (
        Rule(LinkExtractor(allow=r'doe-jp'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DOItem()
        # item['domain_id'] = response.css('div.info h4 a::attr(onclick)').extract()
        file_url = response.css('a.btn.btn-danger::attr(href)').re(r'https.*.pdf')
        item['file_urls'] = file_url
        item['save_folder'] = 'Joao_Pessoa' # file_url.re(r'https.*.pdf').split('/')[-1]
        yield item
        # print(response)
