#Condicional Simples

#Escreva as seguintes expressões booleanas em linguagem Python
#a)O somatório de 2 com 2 é menor que 4
if (2 + 2 < 4):
    print('Verdadeiro!')

#b)O valor 7//3 é igual a 1 + 1
if(7//3 == 1+1):
    print('Verdadeiro!')   
#c)A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
if(3**2 + 4**2 == 25):
    print('Verdadeiro!')
#d)A soma de 2,4 e 6 é maior que 12
if(2 + 4 + 6 > 12):
    print('Verdadeiro!')
#e)1387 é divisível por 19
if(1387 % 19 == 0):
    print('Verdadeiro!')
#f)31 é par
if(31 % 2 == 0):
    print('Verdadeiro!')
#g)O menor valor entre: 34,29 e 31 é menor que 30
if(min (34, 29, 31) <30 ):
    print('Verdadeiro!')

#Traduza as afirmações a seguir para condicionais em Python
#a)Se idade é maior que 60, escreva:'Você tem direitos aos benefícios'
idade = 62
if (idade > 60):
    print('Você tem direito aos benefícios!')

#b)Se fano é maior que 10 e escudo é igual a 0,escreva: 'Você está morto!'
dano = 13
escudo = 0
if(dano > 10 and escudo == 0): # foi usando o and, pois é preciso que ambos os requisitos sejam atendidos para dar a mensagem
    print('Você está morto!')

#c)Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: 'Você escapou!'
norte = True
sul = False
leste = False
oeste = False

if (norte == True or sul == True or leste == True or oeste == True): #Foi usado o or, pois é preciso que apenas um seja true para da a mensagem
    print('Você escapou!')

    #Condicional composta

#Traduza as afirmações a seguir para condicionais em Python

#a) Se ano é divisível por 4, escreva: 'Pode ser um ano bissexto'. Caso contrário, escreva: 'Definitivamente não é um ano bissexto.'
ano = 1993

if(ano % 4 == 0):
    print('Ano pode ser bissexto!')

else:
    print('Definitivamente não é um ano bissexto!')

#b)Se ambas as variáveis booleanas cima e baixo forem True, escreva: 'Decida-se, caso contrário, escreva: 'Você escolheu um caminho!'

cima = True
baixo = True

if(cima == True and baixo == True):
    print('Decida-se!')

else:
    print('Você escolheu um caminho!')





