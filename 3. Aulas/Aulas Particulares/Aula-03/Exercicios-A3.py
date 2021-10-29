def tabuada():
  print('''
  ===============================================
                   TABUADA
  ===============================================
  ''')

  num = int(input('Qual tabuada você deseja aprender hoje?'))

  for contador in range(11):
    prod = contador * num
    print('%d x %d = %d' %(num,contador,prod))

def investimento():

  print('''
  ===============================================
           CALCULADORA DE INVESTIMENTOS
  ===============================================
  ''')

  deposito_inicial = float(input('Qual o valor do depósito?'))
  taxa_juros = float(input('Qual o valor da taxa de juros(%)?'))
  
  #no momento 0, o saldo é igual ao deposito inicial
  saldo = deposito_inicial

  mes = 0

  while mes < 24:
    saldo = saldo * (1 + (taxa_juros/100))
    print('O valor no mês %d é: %.2f'%(mes+1,saldo))
    mes += 1

  print('Os juros totais foram de %.2f reais'%(saldo-deposito_inicial))

def calcula_troco():

  print('''
  ===============================================
                 TROCO MAROTO
  ===============================================
  ''')

  cedulas = [200,100,50,20,10,5,2]
  troco = float(input('Digite o valor do troco:'))

  for cedula in cedulas:

    if troco in cedulas:
      print("O valor do seu troco é:", troco)
      break
    
    elif troco>2:

      qtd_notas = int(troco // cedula)

      if qtd_notas == 0:
        pass
      else:
        print("Estou te entregando {0} nota(s) de {1}".format(qtd_notas,cedula))
        troco = troco - (qtd_notas*cedula)

      if troco <=2:
        print("Não tenho moedas para dar o seu troco. \nObrigado por comprar aqui!")

def crescimento_populacional():

  #População dos países A e B
  pop_a = 80000
  pop_b = 200000

  #Crescimento anual dos países A e B
  cresc_a = 1.03
  cresc_b = 1.015
  
  ano = 0

  while pop_b > pop_a:
      
    pop_a = pop_a*cresc_a
    pop_b = pop_b*cresc_b
    ano += 1

  print("O número necessário de anos para a população \ndo país A ultrapassar a do país B é: {0} anos".format(ano))

def lanchonete():

  print('''
  ===============================================1
     LANCHONETE DO CIDÃO - SISTEMA DE PEDIDOS
  ===============================================
  ''')

  escolha_01 = int(input("Bem-vindo à lanchonete do Cidão!\nDeseja fazer um pedido? \n1 - Sim, 0 - Sair\n"))

  if escolha_01 == 1:
    print("Ótimo! Aqui está o cardápio:")
    print('''
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00  
    ''')

    codigos = [100,101,102,103,104,105]
    dic_precos = {100:1.20, 101:1.30, 102:1.50, 103:1.20,104:1.30,105:1.00}
    
    print('Para fazer o pedido, digite o código e a quantidade desejadas. Para pedir a conta, digite 200')

    totalAPagar = 0

    while True:

      codigo_produto = int(input('Digite o código do item:'))

      if codigo_produto == 200:
        print("Você nos deve R$%.2f"%totalAPagar)
        print()
        print("Obrigado e volte sempre!=]")
        break

      quantidade_produto = int(input('Digite a quantidade que deseja pedir:'))

      if codigo_produto in codigos:
        if quantidade_produto>0:
          print('Anotando o pedido')
          totalAPagar = totalAPagar + quantidade_produto*dic_precos[codigo_produto]
        else:
          print('Quantidade inválida')
      else:
        print('Código inválido')
    
  elif escolha_01 == 0:
    print("Obrigado pela visita à lanchonete!")
  
  else:
    print("Te dei duas opções e você não escolheu nenhuma?\nDê o fora daqui Ò.Ó !!!")



      



