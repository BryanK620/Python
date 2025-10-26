import textwrap

def menu():
    menu = """
    ================= MENU ===================
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nv_us]Novo usuário
    [x]Sair
    ⇛ """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor , extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:R$ {valor:.2f}'
        print('===Depósito realizado!===')
    else:
        print('@@@ Operação não realizada! @@@')

    return saldo, extrato
    

def sacar (*, saldo, valor, extrato, limite, num_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques= num_saques >= limite_saque
    if excedeu_saldo:
        print('@@@ Operação não realizada! Saldo insuficiente. @@@')

    elif excedeu_limite:
        print('@@@ Operação não realizada! O valor excede o limite de saque. @@@')

    elif excedeu_saques:
        print('@@@ Operação não realizada! Número de saques excedido. @@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:R${valor:.2f}'
        num_saques += 1
        print('=== Saque realizado com sucesso!===')

    else:
        print('@@@Operação não realizada. Valor inválido.')

    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    print(' ===============Extrato=============')
    print('Sem movimentações recentes.' if not extrato else extrato)
    print(f'Saldo:R$ {saldo:.2f}')
    print('=================================================')

def nv_usuario (usuarios):
    cpf = input('Informe o número do CPF (somente número): ')
    usuario = filtro_usuario (cpf, usuarios)
    if usuario:
        print('@@@ Usuário já cadastrado. @@@')
        return
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd/mm/aaa): ')
    endereco = input('Informe seu endereço (Rua, número - bairro - cidade/estado): ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco':endereco})

    print('=== Usuário cadastrado com sucesso! ===')

def filtro_usuario (cpf,usuarios):
    usuario_filtrado = [usuarios for usuarios in usuarios if usuarios['cpf'] ==cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def nova_conta(agencia, numero_conta, usuario):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtro_usuario(cpf, usuario)

    if usuario:
        print('=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('@@@ Usuário não localizado, encerrando...! ')


def main():
    limite_saque = 3
    agencia = '0001'

    saldo = 0
    limite = 1000
    extrato = ""
    num_saques = 0
    usuario = []
    contas = []

    while True:
        opcoes = menu()
        if opcoes == 'd':
            valor = float(input('Digite o valor do depósito: '))

            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcoes == 's':
            valor = float(input('Digite o valor a ser sacado: '))

            saldo, extratp = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saque=limite_saque,
            )
        elif opcoes == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcoes == 'nv_us':
            nv_usuario(usuario)

        elif opcoes == 'nc':
            numero_conta = len(contas) +1
            conta = nova_conta (agencia, numero_conta, usuario)

            if conta:
                contas.append(conta)

        elif opcoes =='x':
            break

main()