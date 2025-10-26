#Comando de saída
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
idade = input ('Qual sua idade?')
print (idade)

nome = input ('Qual seu nome?')
print(f'Olá {nome}, seja bem-vindo!')

nota = float(input('Qual nota você recebeu na disciplina?'))
print(f'Você tirou{nota}.')

'''O input sempre retorna um dado do tipo string, se quiser um dado numérico, utilizamos a função int ou float antes do input
int= número inteiro
float=número com vírgula
'''
'''Casting de variáveis
Ocorre quando existe a conversão de uma variável de um tipo de dado para outro, pode ser feito desde que essa conversão seja lógica e faça sentido no contexto do programa, como no último exemplo a cima, acrescentando o float antes da nota, para converter de string para número'''

'''Fluxo de execução do programa e Teste de mesa'''

x = 1
y = 1
z = x + y #z = 2

x = x + 2 #x = 1+2 = 3
y = y - 1 #y = 1-1 = 0
z = x + y #z = 3+0 = 3

x = y + 1 #x = 0+1 = 1
y = x - 1 #y = 1-1 = 0
z = x + y #z = 1+0 = 1

print(z)