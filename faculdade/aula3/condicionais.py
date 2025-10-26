#Condicional simples
#if(x>y): parênteses opcionais, mas dois pontos obrigatório

#Desenvolva um programa que leia dois valores numéricos inteiros e compare se o primeiro é maior que o segundo, utilizando uma condicional simples. Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado é maior do que o segundo

x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if (x > y):
    print('O primeiro valor é maior que o segundo') # O print só é feito caso seja verdadeiro, caso falso nada acontece

#E se quisermos indicar que o segundo valor é maior?
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if (x > y):
    print('O primeiro valor é maior que o segundo')

if(x < y):
    print('O segundo valor é maior que o primeiro')

#Condicional composta
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if (x > y):
    print('O primeiro valor é maior que o segundo')

else:
    print('O segundo valor é maior que o primeiro')

#Desenvolva um programa que leia um valor inteiro e descubra se ele é par ou ímpar

x = int(input('Digite um valor inteiro: '))
if (x % 2 == 0):
    print('O número é par!')

else:
    print('O número é ímpar!')