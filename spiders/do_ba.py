import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

####################################################################################
####################################################################################
####################################################################################
## Este crawler nao pode ser feito uasndo scrapy e foi resolvido usando Selenium. ##
####################################################################################
####################################################################################
####################################################################################
##
# from scrapy_splash import SplashRequest


# from downFiles.items import DOItem


# class DoBaSpider(CrawlSpider):
#     handle_httpstatus_list = [302]
#     name = 'do_bahia'
#     allowed_domains = ['dool.egba.ba.gov.br']
#     start_urls = ['https://dool.egba.ba.gov.br/']
#     custom_settings = {'REDIRECT_ENABLED': False}
#     handle_httpstatus_list = [302]

#     rules = (
#         Rule(LinkExtractor(allow=r'download/'), callback='parse_item', follow=True),
#     )

#     def start_requests(self):
#         for url in self.start_urls:
#             yield SplashRequest(url, self.parse, args={'wait': 2.5})
    
#     # def parse_item(self, response):
#     #     item = DOItem()
#     #     file_urls = response.css('a[id="baixar-diario-completo"]::attr(href)').getall()
#     #     item['file_urls'] = [response.urljoin(file_url) for file_url in file_urls]
#     #     item['save_folder'] = 'Bahia' # file_url.re(r'https.*.pdf').split('/')[-1]
#     #     yield item
    
#     def parse(self, response):
#         scrapy.view(response)