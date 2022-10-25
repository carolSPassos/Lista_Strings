#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

dataNascimento = str(input("data de nascimento no formato dd/mm/aaaa: "))

dia, mes, ano = dataNascimento.split('/')

meses = ['janeiro', 'fevereiro','março','abril','maio','junho','julho','agosto',
'setembro','outubro','novembro', 'dezembro']

print("Você nasceu em: ", dia,"de", meses[int(mes)-1],"de", ano )