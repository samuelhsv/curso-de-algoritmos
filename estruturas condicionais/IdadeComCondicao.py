ano = int(input('Que ano estamos? '))
nasc = int(input('Que ano nasci? '))
idade = ano - nasc

print(f'Em {ano} você terá {idade} anos', end='')

if idade >= 21:
    print(' e já terá atingido a maioridade') 