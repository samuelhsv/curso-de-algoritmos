n = 0
s = 0
maior = 0
menor = 0

for i in range(5):

    n = int(input(f'Digite o {i + 1}° valor: '))
    s = s + n
    if n > maior:
        maior = n

    if i == 0:
        menor = maior

    if n < menor:
        menor = n

print(f'A soma de todos o valores foi {s}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
