#Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
palavra = str(input("será que é um palíndromo? "))

palavra = palavra.upper()

palavraSemEspaco = palavra.replace(" ", "")
palavraReversa = palavraSemEspaco[::-1]

print("palavra de trás pra frente: ", palavraReversa)

if(palavraReversa == palavraSemEspaco):
  print("É um palíndromo!!")
else:
  print("Não é um palíndromo!")