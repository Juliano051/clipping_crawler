import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from datetime import datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from downFiles.items import DOItem

class DoCeSpider(scrapy.Spider):
    name = 'do_manaus'    
    hoje = datetime.now().strftime('%Y%m%d') 
    def start_requests(self):
        urls = ['http://dom.manaus.am.gov.br/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        

## deve usar o xpath pra selecionar o dt que contem a data de hoje, em seguida o link 
#contido no following-sibling 
 
    def parse(self, response):
        base = response.xpath('//span[contains(text(), "06/07/2022")]')
        page = response.url.split("/")[-2]
        file_url =  response.css('a.text-light::attr(href)').get()
        file_url = response.urljoin(file_url)
        filename = "DOAL-"+response.css('h1.fs-base.mb-0::text').extract()[1].strip()+".pdf"
        
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
    def down(self, response, filename):
        with open(f'downFiles/downloads/Alagoas/{filename}', 'wb') as f:
            f.write(response.body)
            f.close()