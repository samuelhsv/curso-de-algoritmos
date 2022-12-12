print('-----------------------\nDEPARTAMENTO DE TRANSITO\n-----------------------')
atual = int(input('Ano Atual (yyyy): '))
nasc = int(input('Ano de Nascimento (xxxx): '))
idade = atual - nasc

print('-----------STATUS-----------')
print(f'IDADE: {idade} ANOS')

if idade >= 18:
        print('APTO A TIRAR CARTEIRA')
else:
        print('INAPTO A TIRAR CARTEIRA')

print('----------------------------')
