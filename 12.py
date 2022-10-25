#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número 
# no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
# O usuário pode informar o número com ou sem o traço separador

numeroDeTelefone = input("telefone: ")

tel = numeroDeTelefone.replace("-", "")

if(tel.isdigit()):
  if len(tel) == 7:
    print("3" + tel)
  elif len(tel) == 8:
    print(tel)
  else:
    print("invalido")
else:
  print("não é numero")