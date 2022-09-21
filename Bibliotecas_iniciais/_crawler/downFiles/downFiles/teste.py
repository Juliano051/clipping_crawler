
# import requests
# link = "https://www.mppe.mp.br/mppe/cidadao/diario-oficial-link-cidadao/category/766-diario-oficial-2022?download=11277:diario-oficial-eletronico-mppe"
# pdf = requests.get(link) 
# print(pdf)
# def save_pdf(self, pdf, file_name):
#         path = file_name
#         with open(path, 'wb') as f:
#             f.write(pdf)
           
import urllib.request
pdf_path = ""
def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()
pdf_path = "https://www.mppe.mp.br/mppe/cidadao/diario-oficial-link-cidadao/category/766-diario-oficial-2022?download=11277:diario-oficial-eletronico-mppe"
download_file(pdf_path, "Test")