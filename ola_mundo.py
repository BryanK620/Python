print('Olá, Mundo!')
print(2+3)
print('2+3')
print('2' + '3')
print('Olá ' + 'Mundo')
print('Olá,' , 'Mundo' )
print('O resulto da soma de 2 + 3 é:', 2+3)
print(10*(5+7)/4)
print(10*(5+7/4))

nota = 8.5
disciplina = 'Lógica de Programação e Algoritmo'

print(nota)
print(disciplina)

print('Disciplina' , disciplina, '. Nota:' , nota)

'''Lista de operadores lógicos

= Atribuição
== Igualdade
> Maior que
< Menor que
>= Maior ou igual a 
<= Menor ou igual a 
!= Diferente'''


'''Concatenação'''

s1 = 'Lógica de Programação'
s1= s1 + ' e Algoritmos'
print(s1)


'''Repetindo strings na concatenação'''

s1 = 'A' + '-' *10 + 'B'

print(s1)

s1 = 'A' + ' ' *10 + 'B'
print(s1)


'''Juntar diferentes variáveis e strings
Marcador: %d ou %i - Números inteiros
Marcador: %f - Números de ponto flutuante
Marcador: %s - Strings
'''

nota = 8.5

s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)  
'''Número com casa decimal'''

s1 = 'Você tirou %.2f na disciplina de Algoritmo' % nota
'''Número com 2 casas decimais'''

s1 = 'Você tirou %d na disciplina de Algoritmos' % nota
print(s1)   
'''Número inteiro'''

nota = 8.5
disciplina = 'Algoritmos'

s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)
'''Misturando números e palavras'''


'''Forma moderna de escrever'''

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina {}' . format (nota, disciplina)
print(s1)

'''Composição com f-string'''

nota = 8.5
disciplina = 'Algoritmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}'
print(s1)


'''Fatiamento de Strings'''

s1 = 'Lógica de Programação e Algoritmos'
print(s1 [0:6])

s1 = 'Lógica de Programação e Algoritmos'
print(s1 [24:34])

s1 = 'Lógica de Programação e Algoritmos'
print(s1 [:6])

'''Tamanho (length)
Podemos descobrir o tamnho da cadeia de caracteres com uma função chamada len'''

s1 = 'Lógica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)



'''Comando de entrada
input: comando, instrução, função
'''

