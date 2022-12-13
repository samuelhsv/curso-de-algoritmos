print('-----------------------\nESCOLA JAVALI CANSADO\n-----------------------')

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
aprov = ''

if media >= 9:
    aprov = 'A'
elif media >= 8 and media <= 8.9:
    aprov = 'B'
elif media >= 7 and media <= 7.9:
    aprov = 'C'
elif media >= 6 and media <= 6.9:
    aprov = 'D'
elif media >= 5 and media <= 5.9:
    aprov = 'E'
else:
    aprov = 'F'

print('-----------------------')
print(f'MEDIA: {media:.1f}')
print(f'APROVEITAMENTO: {aprov}')
print('-----------------------')




