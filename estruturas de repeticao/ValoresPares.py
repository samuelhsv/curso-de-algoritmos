i = int(input('Digite um valor: '))
if i % 2 == 1:
    i -= 1
for j in range(i, -1, -2):
    print(j)
