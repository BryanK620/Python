#Expressões lógicas/booleanas

x = 10
y = 1
res = not x > y
print(res)

x = 10
y = 1
z = 5.5
res = ( x > y)  and (z == y) # x > y true z== y false
print(res)


x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x #1.55
#res = x > y -> true or not z == y ->false and y != y + z / x -> true
#res= True or True and True (primeiro o programa faz o and, depois o or)
print(res)

#Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando. Assuma que a média para aprovação é a partir de 7 e que aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em cada matéria e informe, na tela, se ele passou de ano ou não. (Menezes, 2019, p.60)

m1 = float (input('Digite a nota da 1ª matéria: '))
m2 = float (input('Digite a nota da 2ª matéria: '))
m3 = float (input('Digite a nota da 3ª matéria: '))
if m1 >= 7 and m2 >= 7 and m3 >= 7: #foi utilizado o and, pois precisa que as 3 condições sejam verdadeiras, para que o resultado seja a aprovação
    print('O aluno está aprovado!')
else:
    print('O aluno não passou de ano!')