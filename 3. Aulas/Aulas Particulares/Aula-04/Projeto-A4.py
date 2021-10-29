#Só para fazer graça
import time
print('''
===========================================================
             ASSISTENTE VIRTUAL - SUBWAY                     
===========================================================                                                    
''')


#LISTAS DE INGREDIENTES

grupos_ingredientes = ['pão', 'recheio', 'queijo', 'salada', 'tempero', 'molho']

pães = ['italiano branco', 'três queijos', 'parmesão e orégano', 'granola salgada', 'nove grãos', 'manteiga temperada']
recheios = ['frango teriyaky', 'frango defumado com cream cheese', 'frango ranch', 'BMT italiano', 'steak churrasco', 'carne supreme', 'vegetariano']
queijos = ['cheddar', 'prato', 'suíço', 'mussarela ralada']
saladas = ['azeitona', 'picles', 'pepino', 'pimentão', 'alface','cebola roxa', 'tomate','rúcula', 'cenoura', 'vinagrete']
temperos = ['sal', 'azeite', 'vinagre', 'pimenta do reino', 'nenhum']
molhos = ['cebola agridoce', 'chipotle', 'barbecue', 'parmesão', 'maionese temperada', 'maionese', 'mostarda e mel', 'supreme', 'nenhum']

#Lista de listas com todos os ingredientes disponíveis
ingredientes = [pães, recheios, queijos, saladas, temperos, molhos]

#MONTANDO UM DICIONÀRIO PARA ORGANIZAR TUDO
dicionario_ingredientes = dict(zip(grupos_ingredientes, ingredientes))

#LISTA DE RESPOSTAS POSSÍVEIS DO USUÁRIO
positivo = ['sim', 's', 'y', 'yes', 'claro', 'pode', 'pode sim']
negativo = ['não', 'n', 'no', 'nein', 'neh', 'não pode', 'não pode não']

#Nossa única variável global que entrará nas funções. A lista de escolhas do usuário.
escolha = []

#Função de boas-vindas que direciona o atendimento.
def welcome():
  print('Bem vindo ao Subway! Posso anotar o seu pedido?')
  while True:
    resposta = input().lower().strip()
    if resposta in positivo:
      anota_pedido()
      confere_pedido()
      break
    elif resposta in negativo:
      print('Sem problemas. Mais tarde eu pergunto de novo ;)')
      time.sleep(2)
      print('...')
      time.sleep(2)
      welcome()
    else:
      print('Não entendi =/ Poderia reformular?')

#Função que mostra o menu e anota o pedido
def anota_pedido():
  print('\nOk, vamos lá \o/')
  contador = 0
  global escolha
  
  #Limpando as escolhas anteriores, 
  #caso o pedido esteja sendo reanotado
  escolha.clear()

  for chave, valor in dicionario_ingredientes.items():
    
    #Mostra as opções
    print("\nEscolha o tipo de {0}:".format(chave))
    for v in valor:
      print(contador, '- ', v)
      contador += 1
    
    #reseta contador
    contador = 0
    #calcula as opções válidas
    opcoes_validas = range(0,len(valor)+1,1)
    
    #Enquanto eu não tiver todas as 6 respostas
    while len(escolha) < 6:
      #Armazena a resposta do USUÁRIO
      resposta = int(input().strip())
      if resposta in opcoes_validas:
        #Se a resposta for válida, armazena e vai pra próxima
        escolha.append(resposta)
        break
      else:
        print("Opção inválida! Escolha uma das opções acima")


#Função que confere o pedido e dá oportunidade para o usuário alterá-lo.
def confere_pedido():
  contador = 0
  print("\nCONFIRMAÇÃO DO PEDIDO \n")

  for grupo in grupos_ingredientes:
    #Este acesso está treta... Mas não consegui fazer de outro jeito
    ing_escolhido = dicionario_ingredientes[grupo][escolha[contador]]
    print("{0}: {1}".format(grupo, ing_escolhido))
    
    contador += 1
  
  resposta = input('\nTudo certo?\n')
  
  while True:
    if resposta in positivo:
      print('O pedido está sendo preparado!\nObrigado por escolher o subway =]')
      break
    elif resposta in negativo:
      print('Sem problemas! \nVamos anotar o seu pedido novamente\n')
      anota_pedido()
      confere_pedido()
      break
    else:
      print("Desculpa, não entendi =/ Poderia reformular?")

welcome()