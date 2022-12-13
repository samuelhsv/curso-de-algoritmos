i = 1
cont = 0
n = int(input("Digite um numero: "))

while True:
    if n % i == 0:
        cont += 1
    i += 1
    if i > n:
        break

print(f'Ao todo, existem {cont} valores divisiveis ', end='')
if cont == 2:
    print(f'e o numero {n} é primo')
else:
    print(f'e o numero {n} não é primo')

