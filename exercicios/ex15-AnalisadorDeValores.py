soma = 0
media = 0
div5 = 0
nulo = 0
somaPar = 0

for i in range(5):
    n = int(input(f'Digite o {i + 1}° valor: '))
    soma += n
    media = n + media
    if i == 4:
        media = media / 5
    if n % 5 == 0:
        div5 += 1
    if n == 0:
        nulo += 1
    if n % 2 == 0:
        somaPar += n


print(f'A soma entre os valores é {soma}')
print(f'A media entre os valores é {media}')
print(f'Valores divisiveis por 5: {div5}')
print(f'Valores nulos: {nulo}')
print(f'A soma dos valores pares é {somaPar}')
