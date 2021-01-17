# -*- coding: utf-8 -*-

print("Faça um Programa que leia um vetor de 7 caracteres")
print("e diga quantas consoantes foram lidas. Imprima as consoantes.")
print()

vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

palavra = input("Digite uma palavra com sete letras: ")

contaLetras = 0
for letra in palavra:
    if letra not in vogais:
        contaLetras += 1
print()
print(palavra, "contém: ", contaLetras, "consoantes")
print()
