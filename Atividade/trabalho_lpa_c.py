print('-'*76) #Multiplicação do pontilhado para organização
print('BEM-VINDO(A) ao Sistema de Precificação de Planos de Saúde do Bryan Kássio')
print('-'*76)

try:
    valor_Base = float(input("Digite o valor base do plano: R$ "))# Solicita o valor base do plano e tenta converter para float
    
    idade_cliente = int(input("Digite a idade do cliente (em anos): "))# Solicita a idade do cliente e tenta converter para int
    
except ValueError:
    print("\nERRO: Por favor, insira valores numéricos válidos para o valor base e a idade.")
    # Encerra o programa se a entrada for inválida
    exit()

fator_multiplicacao = None # Isso serve como uma bandeira de segurança: o cálculo final só prosseguirá se esta variável receber um valor numérico válido (em um dos blocos 'elif')

#Verifica se a idade é válida (maior ou igual a zero) antes de continuar
if idade_cliente < 0:
    print('\nERRO: Idade não pode ser número negativo.')

#Se a idade for maior ou igual a zero e menor que 19 (100%)
elif 0 <= idade_cliente < 19:
    fator_multiplicacao = 1.00 #100/100

#Se a idade for maior ou igual a 19 e menor que 29 (150%)
elif 19<= idade_cliente < 29:
    fator_multiplicacao = 1.50 #150/100

#Se a idade for maior ou igual a 29 e menor que 39 (225%)
elif 29<= idade_cliente < 39:
    fator_multiplicacao = 2.25 #225/100

#Se a idade for maior ou igual a 39 e menor que 49 (240%)
elif 39<= idade_cliente < 49:
    fator_multiplicacao = 2.40 #225/100

#Se a idade for maior ou igual a 49 e menor que 59 (350%)
elif 49 <= idade_cliente < 59:
    fator_multiplicacao = 3.50 #350/100

#Se a idade for maior ou igual a 59 (600%)
elif idade_cliente >= 59:
    fator_multiplicacao = 6.00 #600/100

if fator_multiplicacao is not None: # Verifica se um fator de multiplicação foi atribuído com sucesso com algumas das faixas de idades e porcentagens disponíveis.
    valorMensal = valor_Base * fator_multiplicacao

    print('\n--------------------Resumo do Cálculo-----------------')
    print(f'Idade Informada: {idade_cliente} anos')
    print(f'O Valor Mensal do Plano é de: R$ {valorMensal:.2F}')

else:
    print('Cálculo nãp pôde ser realizado devido a erro na entrada')