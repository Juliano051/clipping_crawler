import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from datetime import datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_ac'    
    hoje = datetime.now().strftime('%Y%m%d') 
    def start_requests(self):
        urls = ['http://www.diario.ac.gov.br/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_url =  response.css('a.edhoje::attr(href)').get()
        file_url = response.urljoin(file_url)
        filename = ''.join(response.css('span.txt-hj-pequeno::text').getall())+".pdf"
        
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        with open(f'downFiles/downloads/Acre/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()