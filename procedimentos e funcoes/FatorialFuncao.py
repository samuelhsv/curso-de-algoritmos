def fatorial(n):
    mult = 1
    for i in range(1, n+1):
        mult = mult * i
    return mult

n = int(input('Digite um número: '))
f = fatorial(n)
print(f'O valor de {n}! é {f}')
