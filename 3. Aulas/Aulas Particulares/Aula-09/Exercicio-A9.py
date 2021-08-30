#Vamos processar o texto de uma notícia usando o que aprendemos.

#Primeiro, o site da notícia:
#https://g1.globo.com/planeta-bizarro/noticia/2019/08/15/guaxinim-assaltante-fica-preso-em-maquina-de-venda-de-lanches-nos-eua.ghtml

#Vamos transformar o texto da notícia em uma lista de palavras

texto = """
Guaxinim 'assaltante' fica preso em máquina de venda de lanches nos EUA

Incidente curioso ocorreu na quarta-feira (14) na Flórida.

Um guaxinim "ladrão" ficou preso em uma máquina de venda de lanches no estado americano da Flórida. O caso ocorreu no condado de Volusia na quarta-feira (14). A polícia postou fotos do "assaltante" pego em flagrante.

"Este senhor foi apreendido hoje quando cometia um furto em uma máquina de venda de comida na escola Pine Ridge", disse a polícia.

O guaxinim foi resgatado pelas autoridades de controle animal e solto no mato."

"""
texto_otimizado = texto.lower()
texto_otimizado = texto.replace('.', '')
texto_otimizado = texto.replace('\"', '')
lista_texto = texto_otimizado.split()
print(lista_texto)

#Vamos verificar o vocabulário da notícia utilizando um set
vocabulario = set(lista_texto)
print(vocabulario)

#Vamos criar um dicionário para contar a frequência de palavras
pal_freq = dict()

def conta_palavras(frase):
  dic_pal = dict()
  for caracter in frase:
    #Se a chave ainda não tiver no dicionário, adiciona
    if caracter not in dic_pal:
      dic_pal[caracter] = 1
    #Se já estiver, só incrementa o valor
    else:
      dic_pal[caracter] += 1
    
  return dic_pal

pal_freq = conta_palavras(lista_texto)
pal_freq_ord = {k: v for k, v in sorted(pal_freq.items(), key=lambda item: item[1])}
print(pal_freq_ord)

import matplotlib.pyplot as plt

plt.bar(pal_freq_ord.keys(),pal_freq_ord.values(), color = 'red')
plt.show()