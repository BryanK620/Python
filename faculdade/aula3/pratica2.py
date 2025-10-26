#Escreva um algoritmo que leia um nome e uma idade. Caso o nome digitado seja Bryan, escreva isso na tela. Caso o usuário digite qualquer outro nome, veirifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for maior que 100 anos, informe que esta pessoal possivelmente não existe.

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if nome == 'Bryan':
    print('Olá, Bryan! ')
elif idade < 18:
    print('Você não é o Bryan e é menor de idade!')
elif idade > 100:
    print('Diferente de você, o Bryan não é imortal!')