conv = int(input('Quantas conversoes voce fará? ')) 

for i in range(conv):    
    reais = int(input("Qual o valor? R$ "))
    dolar = reais / 2.20
    print(f'O valor convertido e U${dolar:.2f}')