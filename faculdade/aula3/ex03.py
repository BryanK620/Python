#Escreva um programa que calcule o preco a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
#Calcule o preço de acordo com a tabela a seguir
#Residencial -> até 500 kWh -> 0,40 / Acima de 500 kWh -> 0,65
#Comercial  -> até 1000 kWh -> 0,55 / Acima de 1000 kWh -> 0,60
#Industrial  -> até 5000 kWh -> 0,55 / Acima de 5000 kWh -> 0,60


kwh = float(input('Quantos kWh?'))
tipo = input('Qual o tipo da instalação? (R, C ou I)')

if(tipo == 'R'):
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.40

    print(f'Total a pagar: {kwh*preco}')

elif(tipo == 'C'):
    if kwh >= 1000:
        preco = 0.55
    else:
        preco = 0.60

    print(f'Total a pagar: {kwh*preco}')


elif(tipo == 'I'):
    if kwh >= 5000:
        preco = 0.55
    else:
        preco = 0.60

    print(f'Total a pagar: {kwh*preco}')

else:
    print('Instalação Inválida. Encerrando...')