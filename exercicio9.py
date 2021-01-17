# -*- coding: utf-8 -*-

print("Faça um Programa que leia um vetor A com 10 números inteiros,")
print("calcule e mostre a soma dos quadrados dos elementos do vetor.")
print()

vetorA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetorB = []

print("Vetor A: ", vetorA)

for i in vetorA:
    i = i ** 2
    vetorB.append(i)

print("Vetor B", vetorB)

soma = 0
for i in vetorB:
    soma = soma + i

print("Soma dos quadrados: ", soma)
