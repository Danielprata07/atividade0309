print(20*'-' ,'Questão 1 - Lista 1', 20*'-')

lista = [5,8,2,9,1] #resposta letra a

lista.sort() #resposta letra b
lista.sort(reverse=True)

lista.append(7) #resposta letra c
lista.insert(2,3)

lista[1] = 10 #resposta letra d
lista.remove(9)

del lista[2:4]#resposta letra e

print(f'Lista editada será:{lista}')

