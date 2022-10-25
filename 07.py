#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = str(input("Sua frase preferida: "))

espacoEmBranco = frase.count(" ")

fraseNova = frase.lower()
a = fraseNova.count("a")
e = fraseNova.count("e")
i = fraseNova.count("i")
o = fraseNova.count("o")
u = fraseNova.count("u")

print("a->", a, "\ne->", e, "\ni->", i, "\no->", o, "\nu->", u)
print("espaço em branco->", espacoEmBranco)