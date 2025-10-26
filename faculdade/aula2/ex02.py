#Exercício

x = int(input('Digite um número inteiro: '))
y = int (input('Digite outro número inteiro: '))
#maneira moderna
resp = 'O resultado da soma de {} com {} é {}.'.format(x,y,x+y)
print(resp)

#maneira com f=string
res = f'O resultado da soma de {x} com {y} é {x+y}'
print(res)