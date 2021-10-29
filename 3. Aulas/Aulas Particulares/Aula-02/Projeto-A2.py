#cabeçalho
print('------------------------------------------')
print('Classificação Etária de Games - ESRB')
print('------------------------------------------')
print()

#mensagem Inicial
print('Olá! Quer saber quais jogos você pode jogar de acordo com a ESRB? \ns-sim, n-não')

#resposta
answer = input()

#aqui podemos adicionar uma lista para permitir mais de uma resposta possível.

if answer == 's':
  print('\nUhuul! Vamos lá:\n')
  
  print('Por favor, digite a sua idade:')
  user_age = int(input())
  
  print("\nVocê pode jogar jogos com os seguintes selos: \n")

  if ((user_age >= 2) and (user_age <= 6)):
    print('eC - Early ChildHood')
  
  if user_age >= 6:
    print('E - Everyone')

  if user_age >= 10:
    print('E10+ - Everyone 10+')

  if user_age>=14:
    print('T - Teen')

  if user_age >= 17:
    print('M - Mature')

  if user_age >= 18:
    print('A - Adults Only')
  
  print('\nObrigado por usar o nosso programa!')

elif answer == 'n':
  print('Ahh, que pena! =[')
  print()
  print('PROGRAMA ENCERRADO')

else:
  print('Desculpe, não entendi o que você falou...')
  print()
  print('PROGRAMA ENCERRADO')

#melhorar a usabilidade com a função sleep da biblioteca time