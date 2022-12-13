n = int(input('Quer a tabuada de qual numero? '))
r = 0
i = 1
while True:
    r = n * i
    print(f'{n} x {i} = {r}')
    i += 1
    if i == 11:
        break
