#Simplifica o uso de múltiplas condicionais em um programa, utilizando o elif

#Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana. Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algortimo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela. Considere que maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana R$ 1,85

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual sua escolha? '))
qtd = int (input('Quantas unidades? '))

if (produto == 1 ): #maçã #Primeiro teste sempre com if, todos os outros elif
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total à pagar: {pagar}')

elif (produto == 2): #laranja
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total à pagar: {pagar}')

elif (produto ==3): #banana
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. Total à paga{pagar}')
else:   
    print('Produto inexistente!')



