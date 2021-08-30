def exercicio_01():

  print('''
  =====================================
           Calculadora Básica          
  =====================================
  ''')

  print('Digite qual operação você deseja fazer:')
  print('+ soma \n- subtração \nx multiplicação \n/ divisão')
  op = input()

  a = float(input('Digite o primeiro número:'))
  b = float(input('Digite o segundo número:'))

  result = 0.0

  if op == '+':
    result = a + b
  elif op == '-':
    result = a - b
  elif op == 'x':
    result = a * b
  elif op == '/':
    result = a / b
  else:
    result = 'Operação inválida'

  print('O resultado da operação é:', result)

  #Desafio: como alterar o programa para só solicitar os números caso a operação não seja inválida?

def exercicio_02():

  print('''
  =====================================
       Calculadora de Empréstimo          
  =====================================
  ''')


  salario = float(input('Digite o valor do salário: '))
  valorImovel = float(input('Digite o valor do imóvel: '))
  anosFin = int(input('Digite a quantidade de anos do financiamento: '))

  prestacao = valorImovel/(anosFin*12)

  if prestacao > 0.30*salario:
    print('Empréstimo indisponível para o cliente. \nValor da prestação acima da capacidade de pagamento.')

  else:

    print('Capacidade de pagamento aprovada!\nO valor base da prestação é:', prestacao)
  
  #Desafio: como tornar esse programa mais seguro para que as pessoas não façam simulações de empréstimo proibidas usando valores negativos para o imóvel?

def exercicio_03():

  print('''
  =====================================
     Calculadora de Tarifa de Energia          
  =====================================
  ''')

  kWh = float(input('Digite quantos KWh você consumiu este mês: '))
  print('Digite o tipo de tarifa energética:')
  print('R - Residencial, C - Comercial, I - Industrial')
  tipoTarifa = input()

  tarifa = 0.0

  if tipoTarifa == 'R':

    if kWh <= 500:
      tarifa = 0.40 * kWh
    else:
      tarifa = 0.65 * kWh
  
  elif tipoTarifa == 'C':

    if kWh <= 1000:
      tarifa = 0.55 * kWh
    else:
      tarifa = 0.70 * kWh

  elif tipoTarifa == 'I':
    
    if kWh <= 5000:
      tarifa = 0.60 * kWh
    else:
      tarifa = 0.75 * kWh

  else:

    tarifa = 'Operação Inválida!'

  print('O valor a ser pago da tarifa é:', tarifa)

  #Desafio: Que tal fazer uma calculadora para a tarifa energética real?