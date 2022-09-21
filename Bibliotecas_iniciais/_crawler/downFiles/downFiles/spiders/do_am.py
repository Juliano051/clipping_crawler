# hardcode hardcoded
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from datetime import datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_am'    
    hoje = datetime.now().strftime('%Y%m%d') 
    def start_requests(self):
        urls = ['https://imprensaoficial.al.gov.br/diario-oficial']
        for url in urls:
            yield scrapy.Request(url="https://imprensaoficial.al.gov.br/diario-oficial", callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_url =  response.css('a.text-light::attr(href)').get()
        file_url = response.urljoin(file_url)
        file_url = "https://diario.imprensaoficial.am.gov.br/portal/edicoes/download/16915"
        filename = "DOAL-"+response.css('h1.fs-base.mb-0::text').extract()[1].strip()+".pdf"
        
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        with open(f'downFiles/downloads/Amazonas/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()