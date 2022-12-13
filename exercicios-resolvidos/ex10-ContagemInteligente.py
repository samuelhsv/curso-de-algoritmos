print('CONTAGEM INTELIGENTE\n--------------------')

ini = int(input('Inicio: '))
fim = int(input('Fim: '))

print('----------------\nC O N T A N D O\n----------------')

if ini < fim:
    for i in range(ini, fim+1):
        print(f'{i}...  ', end='')
else:
    for i in range(ini, fim-1, -1):
        print(f'{i}...  ', end='')    

