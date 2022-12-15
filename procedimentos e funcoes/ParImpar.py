def ParOuImpar(v):
    if v % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR' # return retorna um valor pra onde ele foi chamado

n = int(input('Digite um numero: '))
r = ParOuImpar(n) # 'r' Só pode receber um valor se tiver o return que retorna um valor para a variavel
print(f'O numero {n} é um valor {r}')