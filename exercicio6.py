# -*- coding: utf-8 -*-

print("Faça um Programa que peça as 4 notas de 10 alunos,")
print("calcule e armazene num vetor a média de cada aluno,")
print("imprima o número de alunos com média maior ou igual a 7.0")
print()


def adicionaNotas():
    notas = []
    for i in range(4):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
    return notas


def calculaMedia(listaNotas):
    soma = 0.0
    for nota in listaNotas:
        soma = soma + nota
    media = soma / len(listaNotas)
    return media


def contabilizaAprovados(medias):
    contadorAlunos = 0
    for media in medias:
        if media >= 7.0:
            contadorAlunos = contadorAlunos + 1
    return contadorAlunos


medias = []
for aluno in range(2):
    print("\nNotas do aluno ", aluno + 1, "\n")
    media = calculaMedia(adicionaNotas())
    medias.append(media)

print("\nQuantidade de alunos aprovados: ", contabilizaAprovados(medias))
