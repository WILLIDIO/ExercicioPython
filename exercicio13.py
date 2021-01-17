# -*- coding: utf-8 -*-

"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. as perguntas são:
    "telefonou para a vítima?"
    "esteve no local do crime?"
    "mora perto da vítima?"
    "devia para a vítima?"
    "já trabalhou com a vítima?"
o programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "suspeita", entre 3 e 4 como "cúmplice" e 5 como "assassino".
caso contrário, ele será classificado como "inocente".
"""

import time


def fazPerguntas():
    print("Responda com sim ou não")
    print("considerando o crime em questão...\n")
    pergunta1 = input("Telefonou para a vítima?\n: ")
    pergunta2 = input("Esteve no local do crime?\n: ")
    pergunta3 = input("Mora perto da vítima?\n: ")
    pergunta4 = input("Devia dinheiro para vítima?\n: ")
    pergunta5 = input("Já trabalhou com a vítima?\n: ")
    listaDeRespostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
    return listaDeRespostas


def contabilizaRespostas(listaDeRespostas):
    contador_de_sins = 0
    for resposta in listaDeRespostas:
        if resposta == "Sim" or resposta == "sim":
            contador_de_sins += 1
    return contador_de_sins


def julgaSujeito(contadorSim):
    if contadorSim == 0:
        print("Você é inocente! Obrigado pelas respostas...")
    elif contadorSim <= 2:
        print(
            "Você é suspeito no crime! Refaça o teste sem esconder suas intencões!"
        )
    elif contadorSim < 5:
        print(
            "Você no mínimo é cúmplice do assassino... Contatarei as autoridades em segundos!"
        )
        print("\nDiscando 190...")
        time.sleep(2)
        for i in range(5):
            print(".")
        print("Concluido!")
    else:
        print("\nVocê é culpado!!!")
        print("Contatarei as autoridades em segundos!")
        print("Discando 190...")
        time.sleep(2)
        for i in range(5):
            print(".")
        print("Concluido!")
        print("Você será prezo. Tem o direito de permanecer em silêncio!")


lista_de_perguntas = fazPerguntas()

julgaSujeito(contabilizaRespostas(lista_de_perguntas))
