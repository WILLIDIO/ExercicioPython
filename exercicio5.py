# -*- coding: utf-8 -*-

print("Faça um Programa que leia 5 números inteiros e armazene-os num vetor.")
print(
    "Armazene os números pares no vetor PAR e os números IMPARES no vetor impar."
)
print("Imprima os três vetores.")
print()

vetorPar = []
vetorImpar = []
numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        vetorPar.append(numero)
    else:
        vetorImpar.append(numero)

print("Números do vetor total: ", numeros)
print("Vetor par: ", vetorPar)
print("Vetor impar: ", vetorImpar)
