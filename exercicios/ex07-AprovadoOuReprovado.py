print('-----------------------\nESCOLA JAVALI CANSADO\n-----------------------')

nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2

print('-----------------------')
print(f'MEDIA: {media:.1f}')


if media >= 7:
    print('ALUNO APROVADO')
else:
    print('ALUNO REPROVADO')

print('-----------------------')