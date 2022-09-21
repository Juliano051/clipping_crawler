import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from datetime import datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_teresina'    
    hoje = datetime.now().strftime('%Y%m%d') 
    def start_requests(self):
        urls = ['http://dom.pmt.pi.gov.br/lista_diario.php']
        for url in urls:
            yield scrapy.Request(url="http://dom.pmt.pi.gov.br/lista_diario.php", callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        # file_url =  response.css('a.text-light::attr(href)').get()
        file_url =  response.css('a::attr(href)').get()
        filename = response.css('a::text').get()+".pdf"
        
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        with open(f'downFiles/downloads/Teresina/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()