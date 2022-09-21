import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import unicodedata
import re
# from datetime import datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_maceio'    
    hoje = datetime.now().strftime('%Y%m%d') 
    def start_requests(self):
        urls = ['https://www.diariomunicipal.com.br/maceio/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_url =  response.css('a#downloadPdf::attr(href)').get()
        # file_url = response.urljoin(file_url)
        filename = "DOM_Maceio_"+response.css('aside#info-diarios span::text').get()
        
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        # filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
        filename = re.sub(r'[^\w\s-]', '-', filename)+".pdf"
        # filename = re.sub(r'[-\s]+', '-', filename).strip('-_')+".pdf"
        with open(f'downFiles/downloads/Maceio/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()