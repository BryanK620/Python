#agora vamos solicitar uma string e um número inteiro como entrada do usuário e repetir a string o número de vezes indicado pelo inteiro
string = input("Digite uma string: ")
num_repeticoes = int(input("Digite um número inteiro: "))
# gerar a string repetida com um espaço entre cada ocorrência
resultado = " ".join(string for _ in range(max(0, num_repeticoes)))
print(resultado)

