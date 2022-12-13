kg = float(input('Massa (Kg): '))
m = float(input('Altura (m): '))
imc = kg / (m ** 2)

print(f'IMC: {imc:.2f}')

if imc < 17:
    print('Muito abaixo do Peso')
elif imc >= 17 and imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print('Obesidade')
elif imc >= 35 and imc < 40:
    print('Obesidade Mevera')
else:
    print('Obesidade Morbida')
