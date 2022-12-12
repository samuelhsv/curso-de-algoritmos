kg = float(input('Massa (Kg): '))
m = float(input('Altura (m): '))
imc = kg / (m ** 2)

if imc >= 18.5 and imc <= 25:
    print(f'Parabéns! Você esta no seu peso ideal.')
else:
    print(f'Você nao esta na faixa de peso ideal.')
