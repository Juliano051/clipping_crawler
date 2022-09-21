## 
# Busca uma lista de palavras-chave, inicialmente contidas no documento keywords.txt, mas que deverá ser obtida da 
# base de dados do sistema. De posse dessa lista de dados, o script varre todos os documentos PDF e busca todas as palavras-chave 
# naquele documento. Identificando, o script salva o nome do documento associado aos termos encontrados e suas respectativas páginas.
# nesse primeiro momento, o resultado da busca é salvo em um arquivo (keyword_dataset.tsv) mas deverá ser enviado para o sistema
# através de uma integração preferencialmente através de API.
##

import fitz
import os
import glob

# for pdf_files in glob.glob('../scrapy/downFiles/downFiles/downloads/*.pdf'):
for pdf_files in glob.glob('*.pdf'):
    #abrir pdf usando módulo fitz
    document = fitz.open(pdf_files)
    print("docs")
    #conta o númeor de paginas
    num_pages = document.pageCount
    
    input = open("./keywords.txt", 'r')
    keywords_list = input.read()
    keywords_separate = keywords_list.split(',')
    keys = {}
    for keywords in keywords_separate:
        c = 0
        for page in range(0, num_pages):
            content = document[page]
            keyword_pattern = keywords.strip()
            keyword_search = content.search_for(keyword_pattern)
            for key in keyword_search:
                c+=1
            if c>=1:
                keys[keywords]= c
    if len(keys)>0:
        print(pdf_files, '->', keys)
        output = open('keyword dataset.tsv', 'a')
        output.write(pdf_files + '\t'+ str(keys) + '\n')
    else:
        print(pdf_files, '->', keys)
        output = open('keyword dataset.tsv', 'a')
        output.write(pdf_files + '\t Palavras-chave não identificadas no documento \n')
