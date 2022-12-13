nome = input('Qual o nome do funcionario? ')
sal = int(input('Qual o salario do funcionario? R$ '))
dep = int(input('Qual a quantidade de dependentes? '))
nsal = 0

if dep == 0:
    nsal = sal + (sal * 0.05)
elif dep >= 1 and dep <= 3:
    nsal = sal + (sal * 0.10)
elif dep >= 4 and dep <= 6:
    nsal = sal + (sal * 0.15)
else:
    nsal = sal + (sal * 0.18)

print(f'O novo salario de {nome} sera de R${nsal:.2f}')




