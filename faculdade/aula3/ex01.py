#Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
#a) Equilátero (três lados iguais)
#b)Isósceles (dois lados iguais)
#c)Escaleno (Três lados diferentes)
#Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois.

A = int(input('Digite o Primeiro lado do triângulo'))
B = int(input('Digite o Segundo lado do triângulo'))
C = int(input('Digite o Terceiro lado do triângulo'))

if((A > 0 and B > 0 and C > 0) and (A + B > C and  A + C > B and B + C > A)):
    if(A!= B and A != C and B != C):
        print('Triângulo escaleno')
    else:
        if(A == B and B == C):
            print('Triângulo Equilátero')

        else:
            print('Triângulo Isósceles')

else: 
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')