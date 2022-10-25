#escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
import math
contador1 = ['um','dois','três','quatro','cinco','seis','seis','sete','oito',
'nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove']
contadorDezenas = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']

numero = int(input("Numero: "))

dezena = math.trunc(numero/10)
unidade = numero%10

if numero <= 19:
  print(contador1[int(numero)])
else:
  print(contadorDezenas[int(dezena)-2], "e", contador1[int(unidade)-1])