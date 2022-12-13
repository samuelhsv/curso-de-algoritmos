print('-----------------------\nESCOLA SANTA PACIENCIA\n-----------------------')

nAlun = int(input('Quantos alunos a turma tem? '))
meAlun = ''
maiNota = 0

for i in range(nAlun):
    print('--------------------')
    print(f'ALUNO {i + 1}')
    nome = input('Nome do aluno: ')
    nota = float(input(f'Nota de {nome}: '))
    
    if nota > maiNota:
        maiNota = nota
        meAlun = nome

print('-----------------------')
print(f'O maior aproveitamento foi de {meAlun} com a nota {maiNota:.2f}')








