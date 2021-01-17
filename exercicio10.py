#! /usr/bin/env python
# -*- coding: utf-8 -*-

print("Faça um Programa que leia dois vetores com 10 elementos cada.")
print("Gere um terceiro vetor de 20 elementos,")
print("cujos valores deverão ser compostos pelos elementos intercalados")
print("dos dois outros vetores.")
print()


def criaVetor():
    vetor = []
    for i in range(10):
        elemento = int(input("Digite um número: "))
        vetor.append(elemento)
    print("\n")
    return vetor


vetor1 = criaVetor()
vetor2 = criaVetor()
vetor3 = []

for i in vetor1:
    vetor3.append(i)
for j in vetor2:
    vetor3.append(j)

print(vetor3)
print(type(vetor3))
