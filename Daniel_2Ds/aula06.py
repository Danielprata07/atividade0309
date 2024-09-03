#aula06
lista = [1,25,23,12,11,6,8,4,34,19,14]

'''print[0]
print[0:5]'''

lista.sort()
lista.sort(reverse=True)
print(f'Lista ordena {lista}')

lista.remove(12)
lista.pop(5)
del lista[2:5] 

nome='Daniel'
lista.append(nome)
print(lista)

lista.insert(2, 'Prata')
print(lista)

#substituir
lista[2] = 'tiago'
print(lista)

print('Daniel' in lista)

'''if condicao: verdadeiro  
    resultado
else: falso
    resultado do if '''

if 'Daniel' in lista: 
    print('sim, o Daniel esta na lista')
else:
    print('Não, o Daniel não esta na lista')

'''print(15*'-',' DANIEL LINDO ', 15*'-')''' 

# len conta quantidades de elementos dentro da lista
# sum irá soma as quantidades de elementos dentro da lista


