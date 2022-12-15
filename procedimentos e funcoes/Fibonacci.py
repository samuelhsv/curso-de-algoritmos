x = 0
y = 1

def fibonacci(t1, t2):
    s = t1 + t2
    print(s, end=' ')
    t1 = t2
    t2 = s
    return t1, t2 # Retorna o valor de t1 e t2

print(x, y, end=' ')
for i in range(8):
    x, y = fibonacci(x, y) # Sem o return, x e y ficam sem valor ja que nao foi retornado nenhum valor
    # apos os return, x, y valem os proximos numeros da sequencia e com esses valores
    # a proxima iteração é iniciada