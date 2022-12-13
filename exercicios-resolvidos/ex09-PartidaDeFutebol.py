print('  ATLÉTICO x CRUZEIRO')
print('-----------------------')

golA = int(input('Quantos gols do ATLÉTICO? '))
golC = int(input('Quantos gols do CRUZEIRO? '))
dif = 0
stat = ''

if golA > golC:
    dif = golA - golC
else:
    dif = golC - golA

if dif == 0:
    stat = 'EMPATE'
elif dif > 0 and dif <= 3:
    stat = 'PARTIDA NORMAL'
else:
    stat = 'GOLEADA'


print('-----------------------')
print(f'DIFERENCA: {dif}')
print(f'STATUS: {stat}')
print('-----------------------')
