#! /usr/bin/env python
# -*- coding: utf-8 -*-

print("Faça um Programa que peça a IDADE e a ALTURA de 5 pessoas,")
print("armazene cada informação no seu respectivo vetor.")
print("Imprima a idade e a altura na ordem inversa que foi lida.")
print()

idades = []
alturas = []

for i in range(5):
    print()
    idade = int(input("Idade " + str(i + 1) + ": "))
    altura = int(input("Altura " + str(i + 1) + ": "))
    idades.append(idade)
    alturas.append(altura)

idades.sort(reverse=True)
alturas.sort(reverse=True)

# A função zip ajuda na iteração de das listas simultâneas
for idade, altura in zip(idades, alturas):
    print("{}:{}".format(idade, altura))
