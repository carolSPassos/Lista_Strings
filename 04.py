#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
nome = str(input("alguma palavra: "))

for i in range(0, len(nome) + 1):
  print(nome[:i])