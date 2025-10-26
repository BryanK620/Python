#Soma dos 5 primeiros números inteiros e positivos
# resp = 15
print(1 + 2 + 3 + 4 + 5)

#Média entre 23,19 e 31
# resp = 24.33333333333
print ((23 + 19 + 31)/3)

#O número de vezes que 73 cabe em 403
# utiliza o // para o resultado ser um número inteiro, pois sem o mesmo o resultado fica 5.52054794520548 e colocando o // o resultado é 5
print(403//73)

#A sobra quando 403 é dividido por 73
# resp = 38
print(403%73)

#Escrever expressões algébricas em linguagem Python

#2 elevado à décima potência
# resp = 1024
print(2**10)

# O valor absoluto da diferença entre 54 e 57
# resp = 3
print (abs (54 - 57))

# O menor valor entre 34 , 29 e 31
# resp = 29
print (min(34 , 29 , 31))

#Atribuição
 
#Atribuir o valor inteiro 3 à variável a
#Atribuir o valor 4 à variável b
#Atribuir à variável c o valor da expressão a*a+b*b

a = 3
b = 4
c = a*a+b*b
print(c)

#Strings

# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'

#Agora utilizando operadores + e *, crie as saídas 
# 'ant bat cod'
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1, s2, s3)

#'ant ant ant ant ant ant ant ant ant ant'

print(10 * (s1 + ' '))

#ant bat bat cod cod cod

print (1 * (s1 + ' ') + 2 * (s2 + ' ') + 3* (s3 + ' ') )

# ant bat ant bat  ant bat ant bat ant bat ant bat ant bat 
print ((s1 + ' '  +  s2 + ' ')  * 7 )

#batbatcod batbatcod batbatcod batbatcod batbatcod

print ( (s2+s2+s3 + ' ') *5)