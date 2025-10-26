#Vamos testar se uma palavra é um palíndromo ou seja, se ela é lida da mesma forma de trás para frente
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]
if palavra.lower() == palavra_invertida.lower():
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
