import os

h18cas = 0
m2530loi = 0

while True:

    os.system('cls')

    print('==========================\n    SELETOR DE PESSOAS     \n==========================')
    sexo = input('Qual o Sexo? [M/F] ')
    idade = int(input('Qual a idade? '))
    print('Qual a cor do Cabelo? ')
    print('------------------------')
    print('[1] Preto\n[2] Castanho\n[3] Loiro\n[4] Ruivo')
    cor = int(input(''))
    if sexo == 'M' and idade >= 18 and cor == 2:
        h18cas += 1
    elif sexo == 'F' and idade >= 25 and idade <= 30 and cor == 3:
        m2530loi += 1

    cont = input('Quer continuar? [S/N]')
    if cont == 'N':
        break

os.system('cls')

print('==========================\n     RESULTADO FINAL     \n==========================')

print(f'Total de homens com mais de 18 e cabelos castanhos é {h18cas}')
print(f'Total de mulheres com entre 25 e 30 e cabelos loiros é {m2530loi}')
