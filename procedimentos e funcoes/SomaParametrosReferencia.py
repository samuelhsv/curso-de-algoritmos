def soma(a, b):
    a += 1
    b += 2
    print(f'Valor de A: {a}\nValor de B: {b}')
    print(f'Soma: {a + b}')
    return a, b

x = 4
y = 8

x, y = soma(x, y)
print(f'Valor de x: {x}\nValor de y: {y}')
