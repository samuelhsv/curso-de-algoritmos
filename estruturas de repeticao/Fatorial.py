import os

while True:    
    os.system('cls')

    num = int(input('Digite um número: '))
    cont = num
    fat = 1
    r = ''
    while True: 
        fat = fat * cont # 1° iteração: fat recebe o valor inicial do fatorial
                         # agora fat vale num e os proximos valores são abaixo de num 
        cont -= 1        # depois da subtração que o fatorial é calculado e cont vale -1 corrente
        if cont == 0:
            break
    print(f'O valor do fatorial de {num} é igual a {fat}')
    r = input('Quer continuar? [S/N] ')
    if r == 'N':
        break
