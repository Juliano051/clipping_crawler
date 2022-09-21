# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
from datetime import datetime
from scrapy.pipelines.files import FilesPipeline

hoje = datetime.now().strftime('%d-%m-%Y')
class DownfilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        original_file_name = item.get('original_file_name')
        media_guid = hashlib.sha1( str.encode(request.url)).hexdigest()
        return f'full/{media_guid}-{original_file_name}'

class DORecifePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # original_file_name = request.url.split('/')[-1]
        original_file_name = item.get('original_file_name')
        media_guid = hashlib.sha1( str.encode(request.url)).hexdigest()
        return f'full/Recife/{media_guid}-{original_file_name}'

class DOPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        save_folder = item['save_folder']
        original_file_name = request.url.split('/')[-1] #item.get('original_file_name')
        media_guid = hashlib.sha1( str.encode(request.url)).hexdigest()
        return f'{save_folder}/{media_guid}-##-{original_file_name}'
    
# class DOParaibaPipeline(FilesPipeline):
#     def file_path(self, request, response=None, info=None, *, item=None):
#         original_file_name = request.url.split('/')[-1] #item.get('original_file_name')
#         media_guid = hashlib.sha1( str.encode(request.url)).hexdigest()
#         return f'full/Paraiba/{media_guid}-{original_file_name}'