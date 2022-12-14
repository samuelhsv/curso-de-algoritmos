n = 0
s = 0
iniMenor = 0
maior = 0
menor = 0

while True:
    n = int(input(f'Digite um valor: '))
    s = s + n
    if n > maior:
        maior = n

    if iniMenor == 0:
        menor = maior

    if n < menor:
        menor = n

    iniMenor =+ 1

    resp = input('Quer continuar? [S/N] ')
    if resp == 'N' or resp == 'n':
        break

print(f'A soma de todos o valores foi {s}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
