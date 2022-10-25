# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e 
# indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
cpf = str(input("cpf: "))

if len(cpf) == 14:
  if cpf[3] == '.' and cpf[7] == '.':
    if cpf[11] == '-':
      primeiraParte = cpf[0:3].isdigit()
      segundaParte = cpf[4:7].isdigit()
      terceiraParte = cpf[8:11].isdigit()
      quartaParte = cpf[12:14].isdigit()

      if primeiraParte == False:
        print("cpf inválido")
      elif segundaParte == False:
        print("cpf inválido")
      elif terceiraParte == False:
        print("cpf inválido")
      elif quartaParte == False:
        print("cpf inválido")
      else:
        print("cpf validado!")
        print("FINALMENTE!!!")
    else:
      print("cpf inválido no -")  
  else:
    print("cpf inválido no .")
else:
    print("cpf inválido na quantidade de caracteres")

