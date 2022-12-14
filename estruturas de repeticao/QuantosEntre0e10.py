cont = 0
soma = 0
for i in range(6):
    num = int(input('Digite um valor: '))
    if num >= 0 and num <= 10:
        cont += 1
        if num % 2 == 1:
            soma = soma + num

# Fora do intervalo
#   if num % 2 == 1:
#       soma = soma + num

print(f'Ao todo, foram {cont} numeros entre 0 e 10')
print(f'Nesse intervalo, a soma de impares foi {soma}')

