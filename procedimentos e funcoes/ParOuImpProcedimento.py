def ParOuImpar(v):
    if v % 2 == 0:
        print(f'O numero {v} é PAR')
    else:
        print(f'O numero {v} é IMPAR')

n = int(input('Digite um numero: '))
ParOuImpar(n)
