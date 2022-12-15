import os
n = ''
maiN = ''
p = 0
maiP = 0

def topo():
    os.system('cls')
    print('-------------------------------------')
    print( 'D E T E C T O R   D E   P E S A D O')
    print(f' Maior Peso ate agora: {maiP} Kg')
    print('-------------------------------------')

topo()
for i in range(5):
    n = input('Digite o nome: ')
    p = int(input(f'Digite o peso de {n}: '))
    if p > maiP:
        maiP = p
        maiN = n
    topo()
print(f'A pessoa mais pesada foi {maiN} com {maiP} Kg')
