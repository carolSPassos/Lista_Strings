# Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador poderá errar 6 vezes antes de ser enforcado.
import random
palavras = ["carta", "anzol","cidade","azuleijo","perna"]

palavraAleatoria = random.choice(palavras)

tentativas = 0
print(palavraAleatoria)
print("A palavra tem ", len(palavraAleatoria), "letras")

while tentativas != 3:  
  
    letraEscolhida = str(input("escolha uma letra: ")).lower()

    if letraEscolhida in palavraAleatoria:
        print("temos essa letra")  
        tentativas = str(input("tenta uma palavra: "))
        if tentativas == palavraAleatoria:
          print("parabens")
          break
    else:
      print("não tem esse letra!")    
else:
  print("Acabou as chances")




    



