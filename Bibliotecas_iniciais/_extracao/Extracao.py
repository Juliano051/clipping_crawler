import re
from array import array
import nltk
from nltk.corpus import stopwords

class Extracao:
    
    paragrafo = ''
    termos = ''
    ## A classe extração recebe como parâmetros o parágrafo em que irá fazer a busca e os termos que irá buscar
    def __init__(self, paragrafo, termos) -> None:
        self.paragrafo = paragrafo
        self.termos = termos
    

    def extrair(self) -> array:

        result =  re.search(self.monta_regex(self.termos), self.paragrafo)

        if result:
                ## Imprime as 10 primeiras palavras do parágrafo + 10 palavras anteriores ao trecho encontrado, + 10 palavras
                ## após o trecho encontrado + as 10 últimas palavras do parágrafo
                arr_palavras_iniciais = self.paragrafo [: int(result.span()[0])].split()[:-2]
                
                if len(arr_palavras_iniciais) > 10:
                        palavras_iniciais = ' '.join(arr_palavras_iniciais[:10]) + " (...)"
                else:
                        palavras_iniciais = ' '.join(arr_palavras_iniciais[:9]) + " (...)"

                # print(result.span())
                trecho_palavra_chave = self.paragrafo[int(result.span()[0]- 24): (result.span()[1]+37)]
                # print(trecho_palavra_chave)
                arr_palavras_finais = self.paragrafo [-200:].split()[1:]
                palavras_finais = '(...) '+' '.join(arr_palavras_finais[1:])
                
                return palavras_iniciais + trecho_palavra_chave + palavras_finais
    
    def monta_regex(self, termos):
        ''' termos: termos a serem buscados, termos_n: termos negativos, que invalidam a busca,
        ou seja, a presença de um  termo negativo'''
        result = []
        for termo in termos:
            result.append(f'({termo})')
        return '(' + '|'.join(result) + ').*(' + '|'.join(result) + ')' 
    def get_values(self):
        print(self.termos, self.paragrafo)