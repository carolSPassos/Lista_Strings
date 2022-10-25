# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

palavra1 = str(input("Palavra 1: "))
palavra2 = str(input("Palavra 2: "))

print("Palavra 1: ", palavra1, "contém", len(palavra1), "caracteres")
print("Palavra 2: ", palavra2, "contém", len(palavra2), "caracteres")

if len(palavra1) == len(palavra2):
  print("as duas são do mesmo tamanho")
else:
  print("não tem mesmo comprimento")

palavra1 = palavra1.lower()
palavra2 = palavra2.lower()

if palavra1 == palavra2:
  print("elas tem o mesmo conteúdo")
else:
  print("elas tem conteúdo diferentes!")
