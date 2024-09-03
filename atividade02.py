print(20*'-' ,'Questão 1 - Lista 1', 20*'-')

#resposta letra a 
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril','Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro','Novembro' ,'Dezembro']

if 'Junho' in meses: 
    print('Junho está na lista')
else:
    print('Item não encontrado')

meses[2]='Abril' #resposta letra c
meses[5]='Dezembro'

#resposta letra d
meses.remove('Novembro')

print(20*'-' ,'Questão 1 - Lista 1', 20*'-')

print(f'A lista final será: {meses}')