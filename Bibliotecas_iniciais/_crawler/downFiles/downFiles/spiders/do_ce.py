import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_ce'    
    hoje = datetime.now().strftime('%Y%m%d') 
    def start_requests(self):
        urls = [
            f'http://pesquisa.doe.seplag.ce.gov.br/doepesquisa/sead.do?page=ultimasDetalhe&cmd=10&action=Cadernos&data={hoje}',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_url = response.css('div.LinkPreto a::attr(href)').getall() #re(r'http.*.pdf')
        for url in file_url:
            filename = url.split('/')[-1]
            yield scrapy.Request(url=url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        with open(f'downFiles/downloads/Ceara/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()