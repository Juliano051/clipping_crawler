
from urllib import request
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from downFiles.items import DownfilesItem



class DOPernambucoSpider(CrawlSpider):
    # headers = {
    #     "authority": "ssl.doas.state.ga.us",
    #     "pragma": "no-cache",
    #     "cache-control": "no-cache",
    #     "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
    #     "accept": "application/json, text/javascript, */*; q=0.01",
    #     "x-requested-with": "XMLHttpRequest",
    #     "sec-ch-ua-mobile": "?0",
    #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    #     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "origin": "https://ssl.doas.state.ga.us",
    #     "sec-fetch-site": "same-origin",
    #     "sec-fetch-mode": "cors",
    #     "sec-fetch-dest": "empty",
    #     "referer": "https://ssl.doas.state.ga.us/gpr/",
    #     "accept-language": "en-US,en;q=0.9"
    # }
    name = 'do_ba_'
    allowed_domains = ['dool.egba.ba.gov.br']
    start_urls = ['https://dool.egba.ba.gov.br/apifront/portal/edicoes/pdf_diario/']

    rules = (
        Rule(LinkExtractor(allow=r'edicoes/'), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):

        link = self.start_urls
        self.save_pdf(link)

    def save_pdf(self, link):
        
        response = request.urlopen(link)    
        print("chegou aqui")
        # print(response.read())
        file = open("./downfiles/downloads/Pernambuco/"+filename , 'wb')
        print(file)
        print(f"salvo em {filename}.pdf")
        file.write(response.read())
        file.close()