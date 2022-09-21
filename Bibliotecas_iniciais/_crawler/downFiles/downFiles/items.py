# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DownfilesItem(scrapy.Item):
    file_urls = scrapy.Field()
    original_file_name = scrapy.Field()
    files = scrapy.Field()  

class DORecifeItem(scrapy.Item):
    file_urls = scrapy.Field()
    original_file_name = scrapy.Field()
    files = scrapy.Field()  
    
class DOItem(scrapy.Item):
    file_urls = scrapy.Field()
    
    original_file_name = scrapy.Field()
    save_folder = scrapy.Field()
    files = scrapy.Field()
    