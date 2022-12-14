cont = 0
i = 0

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        cont += 1
    i += 1
    if i == 5:
        break

print(f'Foram digitados {cont} numeros negativos.')
