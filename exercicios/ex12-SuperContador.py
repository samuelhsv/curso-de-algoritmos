while True:
    print('\n==================\n|      MENU      |\n==================')
    print('|  [1] De 1 a 10 |')
    print('|  [2] De 10 a 1 |')
    print('|  [3] Sair      |')
    print('==================')
    opc = int(input(''))
    if opc == 1:
        for i in range(10):
            print(f'{i + 1}.. ', end='')
    elif opc == 2:
        for j in range(10, 0, -1):
            print(f'{j}.. ', end='')
    elif opc == 3:
        break
    else:
        print('Opcao Invalida')
        continue
