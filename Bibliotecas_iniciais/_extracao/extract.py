### Usando regex para extração de recortes
import re
from xml.etree.ElementInclude import include
import nltk
from nltk.corpus import stopwords
from Extracao import Extracao

# print(stopwords.words('portuguese'))

paragrafo = '''Tendo em vista que as tentativas de notificação pessoal através de aviso de recebimento restaram frustradas, notificamos o(a) Sr(a).
João Victor Cavalcanti de Carvalho do débito existente no valor de R$ 2.690,19 (dois mil, seiscentos e noventa reais e dezenove
centavos), atualizado até 17/10/2019, referente ao recebimento indevido de vencimentos nos exercícios financeiros de 2018 e 2019,
sem a respectiva contraprestação laboral (Desconto previdenciário sobre o valor do proporcional de 13º salário, referente a 01/12 avos,
correspondente ao período de 01/01/2019 a 28/02/2019; Desconto do valor do vencimento recebido no mês de fevereiro de 2019, tendo
em vista o contido no ofício 163/19 da EM Engenho do Meio, que informa o dia da última presença ao trabalho como sendo a data
28/12/2018; Desconto do valor da gratificação de exercício da profissão recebido no mês de fevereiro de 2019, tendo em vista o contido
no ofício 163/19 da EM Engenho do Meio, que informa o dia da última presença ao trabalho como sendo a data 28/12/2018; Desconto
do proporcional de férias, correspondente a 08/12 avos, tendo em vista o período aquisitivo de 2018/2019, não completado; Desconto
de 38 vales, sendo 20 para o mês de fevereiro de 2018, recebido antecipadamente no mês de janeiro de 2019 e 18 para o mês de março
de 2018, recebido antecipadamente no mês de fevereiro de 2019; Desconto do vale transporte recebido para o mês de março de 2019;
e Desconto de 01 falta, referente ao dia 21/12/2018), na matrícula nº. 109.994-9, para PAGAMENTO ou, ainda, para apresentar defesa,
restando assegurados os princípios da ampla defesa e contraditório, na forma do artigo 5º, LV, da CF/88, no prazo de 30 (trinta) dias,
contados a partir da data da publicação.'''

virgulas = paragrafo.split(',')

# print(virgulas[0]+" (...)")
termos = ['João', 'Victor', 'Cavalcanti', 'Carvalho']
ext = Extracao(paragrafo, termos)
print(ext.extrair())

