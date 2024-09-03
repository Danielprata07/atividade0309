# PROGRAMA PARA IDENTIFICAÇÃO DE NÚMEROS 

num1 = input('Digite o 1° número: ')
num2 = input('Digite o 2° número: ')
num3 = input('Digite o 3° número: ')
num4 = input('Digite o 4° número: ')

lista = [num1, num2, num3, num4]

lista.sort()
print(f'o maior número é: {lista[3]}')
print(f'o menor número é: {lista[0]}')