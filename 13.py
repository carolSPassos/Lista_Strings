#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada 
# com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, 
# informando se o usuário ganhou ou perdeu o jogo.
import random

biblioteca = ["branco","amarelo","vermelho","preto","roxo","verde","laranja"]

txt_aleatoria = random.choice(biblioteca)
txt_embaralhada = ''.join(random.sample(txt_aleatoria, len(txt_aleatoria)))

tentativa = 0

while tentativa != 3:
  print(txt_embaralhada)
  resposta = input("qual é a palavra? ")
  if resposta == txt_aleatoria:
    print("Acertou!")
    break
  else:
    tentativa += 1
else:
  print("Acabou a chance")
  