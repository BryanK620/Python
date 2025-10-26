import sys
#tabale preços (valor por m³)
preco_madeira = {
    'PIN': 150.00, #TORA DE PINHO
    'PER': 170.00, #TORA DE PEROBA
    'MOG': 190.90, #TORA DE MOGNO
    'IPE': 210.10, #TORA DE IPÊ
    'IMB': 22.70, #TORA DE IMBUIA
}
#tabela desconto
descontos = {
    'sem_desc': 0.00,
    'desc_4': 0.04,
    'desc_9': 0.09,
    'desc_16': 0.16
}

valor_transporte = {
    '1': 1000.00, #rodoviário
    '2': 2000.00, #ferroviário
    '3': 2500.00, #hidroviário
}

#implementando a função escolha_tipo()
def escolha_tipo ():
    '''
    Pergunta o tipo de madeira, valida a entrada e retorna o valor m3 correspondente.

    '''
    while True:
        print('\n--- Tipos de Madeira Disponíveis ---')
        print(' PIN - Tora de Pinho')
        print(' PER - Tora de Peroba')
        print(' MOG - Tora de Mogno')
        print(' IPE - Tora de Ipê')
        print(' IMB - Tora de Imbuia')
        #pergunta o tipo de madeira
        tipo = input('Entre com o Tipo de Madeira desejado: ').upper().strip()
        #repete se a opção for diferente das válidas
        if tipo in preco_madeira:
            # retorna o VALOR do tipo de madeira
            return preco_madeira[tipo]
        else:
           
            print('Erro: Tipo de Madeira Inválido. Tente novamente.')

def qtd_toras():
    '''
    Pergunta a quantidade de toras em m³, valida a entrada e retorna a quantidade de toras e o valor do desconto.
    '''
    # loop while True para repetição em caso de entrada inválida
    while True:
        try:
            #pergunta a quantidade de toras
            quantidade = input('Digite a quantidade de toras (m³): ').strip()
            
            #tratamento para valor não numérico
            quantidade = float(quantidade)
            
            #validação: maior que 2000 m³
            if quantidade > 2000:
                print('Não aceitamos pedidos com quantidade de toras acima de 2000 m³.')
                # repete a pergunta
                continue
            
            #validação: valor negativo/zero
            if quantidade <= 0:
                print('A quantidade deve ser um valor positivo.')
                continue
                
            #retorna a quantidade e o desconto (lógica de desconto)
            desconto = 0.0
            
            #se a quantidade (em m³) de toras for menor que 100
            if quantidade < 100:
                desconto = descontos['sem_desc'] # 0%
            
            #se a quantidade for igual ou maior que 100 e menor que 500
            elif 100 <= quantidade < 500:
                desconto = descontos['desc_4'] # 4%
                
            #se a quantidade for igual ou maior que 500 e menor que 1000
            elif 500 <= quantidade < 1000:
                desconto = descontos['desc_9'] # 9%
                
            #se a quantidade for igual ou maior que 1000 e menor ou igual que 2000
            elif 1000 <= quantidade <= 2000:
                desconto = descontos['desc_16'] # 16%

            #retorna a tupla (quantidade, desconto)
            return quantidade, desconto
            
        #bloco except para tratar a conversão para float
        except ValueError:
            print('Entrada inválida. Por favor, digite um valor numérico para a quantidade.')
            #repete a pergunta
            continue
# implementar a função qtd_toras()
def qtd_toras():
    '''
    Pergunta a quantidade de toras em m³, valida a entrada e retorna a quantidade de toras e o valor do desconto.
    '''
    #loop while True para repetição em caso de entrada inválida
    while True:
        try:
            #pergunta a quantidade de toras
            quantidade = input('Digite a quantidade de toras em m³: ').strip()
            
            #tratamento para valor não numérico
            quantidade = float(quantidade)
            
            #validação: maior que 2000 m³
            if quantidade > 2000:
                print('Não aceitamos pedidos com quantidade de toras acima de 2000 m³.')
                #repete a pergunta
                continue
            
            #validação: valor negativo/zero
            if quantidade <= 0:
                print('A quantidade deve ser um valor positivo.')
                continue
                
            #retorna a quantidade e o desconto (lógica de desconto)
            desconto = 0.0
            
            #quantidade (em m³) de toras menor que 100
            if quantidade < 100:
                desconto = descontos['sem_desc'] # 0%
            
            #  quantidade igual ou maior que 100 e menor que 500
            elif 100 <= quantidade < 500:
                desconto = descontos['desc_4'] # 4%
                
            #quantidade igual ou maior que 500 e menor que 1000
            elif 500 <= quantidade < 1000:
                desconto = descontos['desc_9'] # 9%
                
            #quantidade igual ou maior que 1000 e menor ou igual que 2000
            elif 1000 <= quantidade <= 2000:
                desconto = descontos['desc_16'] # 16%

            #retorna a tupla (quantidade, desconto)
            return quantidade, desconto
            
        #bloco except para tratar a conversão para float
        except ValueError:
            print('Entrada inválida. Por favor, digite um valor numérico para a quantidade.')
            #repete a pergunta
            continue
#implementar a função transporte()
def transporte():
    '''
    Pergunta pelo serviço adicional de transporte, valida a entrada e retorna o valor extra do transporte escolhido.
    '''
    #loop while True para repetição em caso de opção inválida
    while True:
        print('\n--- Opções de Transporte ---')
        print(' 1 - Rodoviário (R$ 1000.00)')
        print(' 2 - Ferroviário (R$ 2000.00)')
        print(' 3 - Hidroviário (R$ 2500.00)')
        
        #pergunta pelo serviço adicional de transporte
        opcao = input('Digite a OPÇÃO de transporte (1/2/3): ').strip()
        
        #repete se a opção for diferente de 1/2/3
        if opcao in valor_transporte:
            #retorna o valor de apenas uma das opções
            return valor_transporte[opcao]
        else:
            print('Opção inválida. Por favor, digite 1, 2 ou 3.')

# =================================================================
# CÓDIGO PRINCIPAL (MAIN)
# =================================================================

# mensagem de boas-vindas
print('-----------------------------------------------------')
print('Bem-vindo ao Sistema de Vendas de Toras da Empresa Tora Feliz!')
print('Desenvolvido por: Bryan Kássio')
print('-----------------------------------------------------')

#chamada da função para escolher o tipo de madeira
valor_m3 = escolha_tipo()
#variável 'valor_m3' recebe o valor do metro cúbico.

#chamada da função para obter a quantidade e o desconto
#desempacotamento de tupla: a função retorna 2 valores
try:
    quantidade_toras, percentual_desconto = qtd_toras()
except Exception as e:
    #captura erro, embora o try/except da função já resolva a maioria dos casos
    print(f'\nErro ao processar a quantidade de toras: {e}. Encerrando o programa.')
    sys.exit()

#chamada da função para obter o valor do transporte
valor_transporte = transporte()

#implementar o total a pagar no código principal (main)
# Fórmula: total = ((tipoMadeira * qtdToras) * (1 - desconto)) + transporte

# cálculo do preço base sem desconto
preco_bruto = valor_m3 * quantidade_toras

# cálculo do valor do desconto e do preço com desconto
# O (1 - desconto) aplica o desconto percentual
preco_com_desconto = preco_bruto * (1 - percentual_desconto)

#cálculo do valor final
total_pagar = preco_com_desconto + valor_transporte

#exibição do resumo e valor final
print('\n=====================================================')
print(' RESUMO DO PEDIDO')
print(f'Preço Base da Madeira (por m³): R$ {valor_m3:.2f}')
print(f'Quantidade de Toras (m³): {quantidade_toras:.2f}')
print(f'-----------------------------------------------------')
print(f'Preço Bruto: R$ {preco_bruto:.2f}')
print(f'Desconto Aplicado ({percentual_desconto * 100:.0f}%): - R$ {(preco_bruto - preco_com_desconto):.2f}')
print(f'Valor do Transporte Adicional: + R$ {valor_transporte:.2f}')
print('-----------------------------------------------------')
print(f'TOTAL A PAGAR: R$ {total_pagar:.2f}')
print('=====================================================')

#-----------fim do código--------------