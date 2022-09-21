import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from datetime import datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_ap'
    hoje = datetime.now().strftime('%d-%m-%Y') 
    def start_requests(self):
        urls = ['https://diario.portal.ap.gov.br/ultimaedicao.php']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_url = 'https://diario.portal.ap.gov.br/ultimaedicao.php?pdf'
        # file_url = response.urljoin(file_url)
        filename = "DOAP_"+self.hoje + ".pdf"
        
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        with open(f'downFiles/downloads/Amapa/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()