tabela_precos = {
'P': {'PS': 30.00, 'PD': 34.00},
'M': {'PS': 45.00, 'PD': 48.00},
'G': {'PS': 60.00, 'PD': 66.00}
}

valor_total_pedido = 0.0 #implementação de acumulador para somar os valores

print('-'*50)
print('Bem-vindo(a) ao App de vendas da Pizzaria!') #mensagem de boas vindas
print('Desenvolvido por: Bryan kássio') #nome e sobrenome
print('-'*50)

#menu para o cliente
print('========== Cardápio ==========')
print(f'| {'Tamanho':^8} | {'Pizza Salgada(PS)':^18} | {'Pizza Doce(PD)':^15} |')
print('-' * 50)
print(f'| {'P':^8} | {f'R$ {tabela_precos['P']['PS']:.2f}':^18} | {f'R$ {tabela_precos['P']['PD']:.2f}':^15} |')

print(f'| {'M':^8} | {f'R$ {tabela_precos['M']['PS']:.2f}':^18} | {f'R$ {tabela_precos['M']['PD']:.2f}':^15} |')

print(f'| {'G':^8} | {f'R$ {tabela_precos['G']['PS']:.2f}':^18} | {f'R$ {tabela_precos['G']['PD']:.2f}':^15} |')
print('====================================')

#implementação de while, break, continue (repetição do pedido)
while True:
    #escolha do sabor
    while True:
        sabor = input('Digite o Sabor (PS para Salgada e PD para Doce):').upper().strip()
        #validação do sabor
        if sabor in ('PS', 'PD'):
            break #sair do loop de validação do sabor
        elif sabor == 'Sair':
            break #sair do loop de validação do sabor
        else:
            print('Sabor inválido. Tente novamente!')
            continue #ir para próxima interação
    if sabor == 'Sair': #encerra o loop principal caso cliente digite sair
        break

    #escolha do tamnho
    #.upper() usado para converter em maiúsculas, .strip() usado para remover espaços em branco

    while True:
        tamanho = input('Digite o Tamanho (P,M ou G):').upper() .strip() 
        #validação do tamanho
        if tamanho in ('P', 'M', 'G'):
            break #sair do loop de validação do tamanho
        else:
            print('Tamanho inválido.Tente novamente!')
            return_to_main = True
            break
        #verifica a flag definida a cima
    if 'return_to_main' in locals() and return_to_main: 
        del return_to_main #limpa a flag
        continue

     #cálculo do preço (lógica aninhada) 
    preco_item = 0.0
      #estrutura externa tamanho (P, M ou G)
    if tamanho == 'P':
        # estrutura interna aninhada: Sabor (PS ou PD)
        if sabor == 'PS':
            preco_item = tabela_precos['P']['PS'] # R$ 30.00
        elif sabor == 'PD':
            preco_item = tabela_precos['P']['PD'] # R$ 34.00
        # else não é necessário aqui,porque ja validamos o sabor,mas garante a estrutura 'if/elif' completa 
        else: 
             
             print('Erro interno de sabor P.')

    elif tamanho == 'M':
        if sabor == 'PS':
            preco_item = tabela_precos['M']['PS'] # R$ 45.00
        elif sabor == 'PD':
            preco_item = tabela_precos['M']['PD'] # R$ 48.00
        # else não é necessário aqui,porque ja validamos o sabor,mas garante a estrutura 'if/elif' completa 
        else:  
             print('Erro interno de sabor M.')

    elif tamanho == 'G':
        if sabor == 'PS':
            preco_item = tabela_precos['G']['PS'] # R$ 60.00
        elif sabor == 'PD':
            preco_item = tabela_precos['G']['PD'] # R$ 66.00
        # else não é necessário aqui,porque ja validamos o sabor,mas garante a estrutura 'if/elif' completa 
        else:  
             print('Erro interno de sabor G.')   

    else:
        print('Erro de lógica: O tamanho não foi identificado.') # se ocorrer um erro de lógica, usaremos o continue para pular para o próximo pedido, mas a validação de input deve evitar esse erro
        continue

    #atualizar o acumulador
    valor_total_pedido += preco_item
    print(f'Item adicionado: {tamanho} de {sabor}. Custo: R$ {preco_item:.2f}')
    print(f'Subtotal atual: R$: {valor_total_pedido:.2f}')  

    #deseja algo mais
    while True:
        mais_pedido = input('Deseja mais alguma coisa? (S/N): ').upper() .strip()
        if mais_pedido in ('S', 'N'):
            break
        else: 
            print('Resposta inválida. Digite S para Sim ou N para Não.')
    #caso a resposta seja não, encerra o loop principal
    if mais_pedido == 'N':
        break 
#print do acumulador
print('======================================')
print('Pedido concluído. Obrigado!')
print(f'O valor total do seu pedido é: R$ {valor_total_pedido:.2f}')







