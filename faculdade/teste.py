# F. Deve-se inserir comentários relevantes no código
# Implementação do Sistema de Vendas de Pizzas para retirada.
# Tabela de preços (Dados de Referência)
TABELA_PRECOS = {
    "P": {"PS": 30.00, "PD": 34.00},
    "M": {"PS": 45.00, "PD": 48.00},
    "G": {"PS": 60.00, "PD": 66.00}
}

# E. Deve-se implementar um acumulador para somar os valores dos pedidos
valor_total_pedido = 0.0

# A. Mensagem de boas-vindas com nome e sobrenome
print("-----------------------------------------------------")
print("Bem-vindo ao App de Vendas da Pizzaria!")
print("Desenvolvido por: [Seu Nome] [Seu Sobrenome] (Gênio AI)")
print("-----------------------------------------------------")

# A. Implementar um print com um Menu para o cliente
print("\n========== MENU DE OPÇÕES ==========")
print("  Tamanho P:")
print("    - Pizza Salgada (PS): R$ 30.00")
print("    - Pizza Doce (PD): R$ 34.00")
print("  Tamanho M:")
print("    - Pizza Salgada (PS): R$ 45.00")
print("    - Pizza Doce (PD): R$ 48.00")
print("  Tamanho G:")
print("    - Pizza Salgada (PS): R$ 60.00")
print("    - Pizza Doce (PD): R$ 66.00")
print("====================================\n")

# G. Deve-se implementar as estruturas de while, break, continue (todas elas)
# F. Repetição do pedido
while True:
    # --- Etapa 1: Escolha do Sabor (PS/PD) ---
    while True:
        # B. Implementar o input do sabor (PS/PD)
        sabor = input("Digite o SABOR (PS para Salgada ou PD para Doce): ").upper().strip()
        
        # B. e C. Validação do Sabor
        if sabor in ("PS", "PD"):
            # G. Usa 'break' para sair do loop de validação do sabor
            break
        elif sabor == "SAIR":
            # G. Usa 'break' para sair do loop de validação do sabor
            # Esta linha não é estritamente necessária, mas é um bom ponto de quebra
            break
        else:
            # B. "Sabor inválido. Tente novamente"
            print("Sabor inválido. Tente novamente")
            # G. Usa 'continue' para ir para a próxima iteração do loop
            continue

    # Se o cliente digitou SAIR no sabor, encerra o loop principal
    if sabor == "SAIR":
        # G. Usa 'break' para sair do loop principal
        break

    # --- Etapa 2: Escolha do Tamanho (P/M/G) ---
    while True:
        # C. Implementar o input do tamanho (P/M/G)
        tamanho = input("Digite o TAMANHO (P, M ou G): ").upper().strip()
        
        # C. Validação do Tamanho
        if tamanho in ("P", "M", "G"):
            # G. Usa 'break' para sair do loop de validação do tamanho
            break
        else:
            # C. "Tamanho inválido. Tente novamente"
            print("Tamanho inválido. Tente novamente")
            # G. Usa 'continue' para ir para a próxima iteração do loop
            continue

    # --- Etapa 3: Cálculo do Preço (Lógica Aninhada) ---
    
    # Inicializa o preço do item para o cálculo
    preco_item = 0.0 
    
    # D. Implementar if/elif/else aninhado com cada combinação de sabor e tamanho
    
    # Estrutura Externa: Tamanho (P, M ou G)
    if tamanho == "P":
        # Estrutura Interna Aninhada: Sabor (PS ou PD)
        if sabor == "PS":
            preco_item = TABELA_PRECOS["P"]["PS"] # R$ 30.00
        elif sabor == "PD":
            preco_item = TABELA_PRECOS["P"]["PD"] # R$ 34.00
        # else não é estritamente necessário aqui, pois já validamos o sabor,
        # mas garante a estrutura 'if/elif' completa para o requisito.
        else: 
             # Não deve acontecer devido à validação anterior
             print("Erro interno de sabor P.")

    elif tamanho == "M":
        if sabor == "PS":
            preco_item = TABELA_PRECOS["M"]["PS"] # R$ 45.00
        elif sabor == "PD":
            preco_item = TABELA_PRECOS["M"]["PD"] # R$ 48.00
        else:
             print("Erro interno de sabor M.")

    elif tamanho == "G":
        if sabor == "PS":
            preco_item = TABELA_PRECOS["G"]["PS"] # R$ 60.00
        elif sabor == "PD":
            preco_item = TABELA_PRECOS["G"]["PD"] # R$ 66.00
        else:
             print("Erro interno de sabor G.")
    
    # else não é estritamente necessário aqui, pois já validamos o tamanho,
    # mas atende ao requisito de usar 'if, elif e/ou else'.
    else: 
        print("Erro de lógica: O tamanho não foi identificado.")
        # Se for um erro de lógica, podemos usar 'continue' para pular para 
        # o próximo pedido, embora a validação de input deva evitar isso.
        continue 
        
    # E. Atualiza o acumulador
    valor_total_pedido += preco_item
    print(f"\nItem adicionado: {tamanho} de {sabor}. Custo: R$ {preco_item:.2f}")
    print(f"Subtotal atual: R$ {valor_total_pedido:.2f}\n")


    # F. Pergunta se deseja pedir mais
    while True:
        pedido_mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper().strip()
        if pedido_mais in ("S", "N"):
            break
        else:
            print("Resposta inválida. Digite S para Sim ou N para Não.")

    # F. Se a resposta for 'N', encerra o loop principal
    if pedido_mais == "N":
        # G. Usa 'break' para sair do loop principal
        break 
        
# F. Executar o print do acumulador
print("\n====================================")
print("PEDIDO CONCLUÍDO. OBRIGADO!")
print(f"O VALOR TOTAL do seu pedido é: R$ {valor_total_pedido:.2f}")
print("====================================")

# --- FIM DO CÓDIGO ---







#menu para o cliente
print('========== Menu de Opções ==========')
print('Tamanho P:')
print('  -Pizza Salgada (PS): R$ 30.00')
print('  -Pizza Doce (PD): R$ 34.00')
print('Tamanho M:')
print('  -Pizza Salgada (PS): R$ 45.00')
print('  -Pizza Doce (PD): R$ 48.00')
print('Tamanho G:')
print('  -Pizza Salgada (PS): R$ 60.00')
print('  -Pizza Doce (PD): R$ 66.00')
print('====================================')