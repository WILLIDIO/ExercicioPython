# -*- coding: utf-8 -*-

# Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando
# for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
#    Mostre a quantidade de valores que foram lidos;
#    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#    Calcule e mostre a soma dos valores;
#    Calcule e mostre a média dos valores;
#    Calcule e mostre a quantidade de valores acima da média calculada;
#    Encerre o programa com uma mensagem;

# Função que calcula a média
def calculaMedia(lista):
    soma = somaNumeros(lista)
    media = soma / len(lista)
    return media


"""
def media(lista):
    return float(sum(lista)) / len(lista)
"""


# Função que cria a lista
def pedeNumeros():
    teste = True
    listaNumeros = []
    while teste:
        numero = input("Digite um número: ")
        if numero == "-1":
            teste = False
            print()
        else:
            listaNumeros.append(int(numero))
            print(numero)
    return listaNumeros


# Função que imprime os elementos
def imprimeLista(lista):
    for numero in lista:
        print(numero)
    print()


# Função que imprime os elementos na ordem inversa
def imprimeListaInversa(lista):
    for numero in lista[::-1]:
        print(numero)
    print ()


# Função que soma os elementos da lista
def somaNumeros(listaNumeros):
    soma = 0
    for numero in listaNumeros:
        soma = soma + float(numero)
    return soma


# Função que analisa os elementos abaixo e acima da média
def analisaMedia(lista, media):
    contadorAcima = 0
    contadorAbaixo = 0
    for item in lista:
        if item > media:
            contadorAcima += 1
        elif item == media:
            pass
        else:
            contadorAbaixo += 1
    return contadorAcima, contadorAbaixo


# Cria a lista de números do usuário
listaDeNumeros = pedeNumeros()

# Imprime a lista criada
print("Lista:", listaDeNumeros)
print()

print("Elementos da lista na ordem que foi criada")
imprimeLista(listaDeNumeros)

print("Elementos da lista na ordem inversa")
imprimeListaInversa(listaDeNumeros)

print("Soma dos números digitados")
print(somaNumeros(listaDeNumeros))

print("Média dos números digitados")
print(calculaMedia(listaDeNumeros))

# Calcula os elementos que estão acima ou abaixo da media
# Duas variáveis para receber duas saídas da função analisaMedia
mediaAcima, mediaAbaixo = analisaMedia(
    listaDeNumeros, calculaMedia(listaDeNumeros)
)

print("Quantidade acima")
print(mediaAcima)

print("Quantidade abaixo")
print(mediaAbaixo)

print("Mensagem de encerramento!")
print("Até logo!!!!!!")
print()
