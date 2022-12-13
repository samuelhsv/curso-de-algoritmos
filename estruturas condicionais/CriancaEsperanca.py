print('-------------------------')
print('    CRIANCA ESPERANCA')
print('-------------------------')
print('Muito obrigado por ajudar')
print('[1] para doar R$10')
print('[2] para doar R$25')
print('[3] para doar R$50')
print('[4] para doar outros valores')

choice = int(input('[5] para cancelar\n'))
valor = 0

if choice == 1:
    valor = 10
elif choice == 2:
    valor = 25
elif choice == 3:
    valor = 50
elif choice == 4:
    valor = input('Qual o valor da doacao? R$ ')
elif choice == 5:
    exit()

print('-------------------------')
print(f'SUA DOAÇÃO FOI DE R$ {valor}')
print('MUITO OBRIGADO!')
print('-------------------------')
