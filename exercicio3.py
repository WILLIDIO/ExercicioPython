# -*- coding: utf-8 -*-

# Exercício 3
print("Faça um Programa que leia 4 notas, mostre as notas e a média na tela.")


def media(lista):
    return float(sum(lista)) / len(lista)


def imprimeNotas (lista):
    for nota in lista:
        print ("Nota:", nota)


def pedeNotas ():
    listaDeNotas = []
    for i in range(4):
        nota = int(input("Digite uma nota: "))
        listaDeNotas.append(nota)
    return listaDeNotas

notas = pedeNotas()
imprimeNotas (notas)
print ("Média: ", media (notas))
