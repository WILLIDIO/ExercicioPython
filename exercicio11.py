# -*- coding: utf-8 -*-

print("Foram anotadas as idades e alturas de 5 alunos.")
print(
    "Faça um Programa que determine quantos alunos com mais de 13 anos possuem"
)
print("altura inferior à média de alturas desses alunos.")
print()


def comparaAlturaMedia(idades, alturas):
    soma = 0
    for altura in alturas:
        soma = soma + altura
    media = soma / len(alturas)
    print()
    print("Média de alturas", media)
    # AND testará a condição se e somente se!
    contador = 0
    for idade, altura in zip(idades, alturas):
        if (idade > 13) and (altura < media):
            contador = contador + 1
    return contador


idades = []
alturas = []

for i in range(5):
    print()
    idade = int(input("Idade " + str(i + 1) + ": "))
    altura = int(input("Altura " + str(i + 1) + ": "))
    idades.append(idade)
    alturas.append(altura)

# Imprime a quantidade de alunos com mais de 13 anos e altura abaixo da média
print("Abaixo da média: ", comparaAlturaMedia(idades, alturas))
