import scrapy
import json
import unicodedata
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DOItem

class DoNatalSpider(scrapy.Spider):
    name = 'do_natal'
    allowed_domains = ['natal.rn.gov.br']
    def start_requests(self):
        urls = ['https://natal.rn.gov.br/api/dom/data/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_url = re.search(r'https.*.pdf', response.json()['data'][-1][0]).group(0)
        filename = re.sub('<[^<]+?>', '', response.json()['data'][-1][0])
        yield scrapy.Request(url=file_url, callback=self.down, cb_kwargs={'filename':filename})
        
        
    def down(self, response, filename):
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
        filename = re.sub(r'[^\w\s-]', '', filename.upper())
        filename = re.sub(r'[-\s]+', '-', filename).strip('-_')
        with open(f'downFiles/downloads/Natal/DOM-Natal-{filename}.pdf', 'wb') as f:
            f.write(response.body)
            f.close()
            
    

    # def parse_item(self, response):
        
    #     # # json_response = json.loads(response.text)
    #     # self.log('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    #     item = DOItem()
    #     file_url = re.search(r'https.*.pdf', response.json()['data'][0][0]).group(0)
    #     item['file_urls'] = file_url
    #     # # item['original_file_name'] = re.sub('<[^<]+?>', '', response.json()['data'][0][0])
    #     item['save_folder'] = 'Natal'
    #     self.log(">>>>>>>>>>>>>>>)")
    #     yield item
    