valor = float(input("Qual o valor do empréstimo? R$ "))
juros = valor + valor * 0.2
parcelas = int(input("Quantas parcelas? "))
total = juros / parcelas
print(f'Vou pagar {parcelas} parcelas de R$ {total:.2f}')
