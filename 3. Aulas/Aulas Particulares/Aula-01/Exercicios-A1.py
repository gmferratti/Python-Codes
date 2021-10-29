def media_anual():
  n1 = float(input("Digite a nota do bimestre 1:"))
  n2 = float(input("Digite a nota do bimestre 2:"))
  n3 = float(input("Digite a nota do bimestre 3:"))
  n4 = float(input("Digite a nota do bimestre 4:"))
  media = (n1+n2+n3+n4)/4
  print("O valor da média anual é:",media)

def calcula_aumento():
  salario = float(input('Qual é o valor do seu salário hoje?'))
  aumento_p = float(input('O seu aumento percentual será de quanto?'))
  salario_novo = ((aumento_p/100)+1)*salario
  aumento_real = salario_novo - salario
  print('O seu novo salário será {0} reais e o seu aumento total será de {1} reais'.format(salario_novo,aumento_real))

def aluguel_carro():

  dias = float(input("Por quantos dias você alugou o carro?"))
  km = float(input("Quantos kms você percorreu com o carro alugado?"))

  valor_total = 60*dias + 0.15*km

  print("O valor total a ser pago pelo aluguel do veículo é de {0} reais".format(valor_total))

#media_anual()
#calcula_aumento()
aluguel_carro()