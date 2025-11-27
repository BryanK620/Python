import random 

print("Gerador de Senhas")
tamanho = int(input("Digite o tamanho da senha desejada: "))
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
senha = "".join(random.choice(caracteres) for _ in range(tamanho))
print("Senha gerada:", senha)
input("Pressione Enter para sair...")

