# -*- coding: utf-8 -*-

# Exercício 2
print(
    "Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."
)

vetor = []

for i in range(10):
    numero = float(input("Digite um número: "))
    vetor.append(numero)

vetor.sort(reverse=True)
print(vetor)