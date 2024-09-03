#Solicitei 5 notas para saber a media do aluno, caso ele tire menor que 7 ele esta reprovado, se ele tirar mais de 7, aprovado.
notas=[]

numero_usuario1=int(input('Digite uma nota: '))
notas.append(numero_usuario1)
numero_usuario2=int(input('Digite uma nota: '))
notas.append(numero_usuario2)
numero_usuario3=int(input('Digite uma nota: '))
notas.append(numero_usuario3)
numero_usuario4=int(input('Digite uma nota: ')) 
notas.append(numero_usuario4)
numero_usuario5=int(input('Digite uma nota: '))
notas.append(numero_usuario5)
quantidade_notas=len(notas)
soma=sum(notas)
media = soma/quantidade_notas

print(f'As notas são: {notas}')
print(f'A quantidade de notas são: {quantidade_notas}')
print(f'A soma das notas são: {soma}')
print(f'A media das notas são: {media}')

if media > 7: 
    print(f'Aprovado')
else:
    print('reprovado')




