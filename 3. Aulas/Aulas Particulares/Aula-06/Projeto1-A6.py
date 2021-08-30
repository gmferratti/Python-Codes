import getpass

#Solicitando a palavra secreta ao usuário por meio da biblioteca getpass para que ela não seja revelada
palavra_sec = getpass.getpass("Digite a palavra secreta:")

#Padronizando a palavra em caixa-baixa
palavra_sec = palavra_sec.lower()

#Removendo espaços vazios
palavra_sec = palavra_sec.strip()

#Contando o número de caracteres da palavra
n_sec = len(palavra_sec)

#Criando uma lista de caracteres da palavra secreta
letras_sec = list(palavra_sec)

#Iniciando uma lista vazia para as letras descobertas
letras_desc = []

#Setando o estado inicial de "letras_desc" para somente tracinhos
for i in range(0,n_sec):
  letras_desc.append("_")

#Iniciando flag para caso a palavra seja advinhada
acertou = False

#imprimindo o cabeçalho do jogo

print("\n=================================================")
print("==================JOGO DA FORCA==================")
print("=================================================\n")

#Imprimindo orientação inicial
print("Tente adivinhar a palavra secreta. Boa sorte =]")

#Imprimindo a quantidade de tracinhos da palavra secreta
print(*letras_desc,"\n",sep=" ")

n_vidas = 6

#Loop principal do jogo que solicita letras ao usuário até que ele acerte a palavra secreta e o status da flag "acertou" passe de False para True
while acertou == False:
  
  if n_vidas == 0:
    print("G A M E    O V E R")
    break

  #solicitando que o usuário digite uma letra
  u_letra = input("Digite uma letra: ").lower().strip()

  #verificando se o usuário digitou somente uma letra mesmo
  if len(u_letra) > 1:
    print("Eu disse uma letra, espertinho =P")

  #atualizando a lista de letras descobertas com base no input do usuário
  for i in range(0, n_sec):
    if u_letra == letras_sec[i]:
      letras_desc[i] = u_letra
      print("Acertou! \o/")
  
  if u_letra not in letras_sec:
    n_vidas -= 1
    print("Tente novamente. Vidas restantes:", n_vidas)

  print(*letras_desc,"\n",sep=" ")

  if letras_desc == letras_sec:
    acertou = True
    print("P A R A B É N S!\n Você completou o desafio ¯\_( ͡° ͜ʖ ͡°)_/¯")
