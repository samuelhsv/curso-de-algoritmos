n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'A media do aluno foi {m:.2f}')

if m >= 7:
    print('Aluno APROVADO')
elif m >=5 and m < 7:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')
