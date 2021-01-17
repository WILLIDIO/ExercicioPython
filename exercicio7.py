# -*- coding: utf-8 -*-

# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação (montante das duas operações)
# e os números em sí.


def criaLista():
    lista = []
    for i in range(5):
        numero = int(input("Digite o número: "))
        lista.append(numero)
    return lista


def somaLista(lista):
    soma = 0.0
    for numero in lista:
        soma = soma + numero
    return soma


def multiplicaLista(lista):
    multiplica = 1
    for numero in lista:
        multiplica = multiplica * numero
    return multiplica


lista1 = criaLista()
print(lista1)
print("Soma da lista", somaLista(lista1))
print("Multiplicação da lista", multiplicaLista(lista1))
