# -*- coding: utf-8 -*-

print("Faça um programa que receba a temperatura média de cada mês do ano e")
print(
    "armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e"
)
print(
    "mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram"
)
print("mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ")
print()

# A função ano cria um dicionário de meses do ano por exetenso
def ano():
    meses = {
        '0': "janeiro",
        '1': "fevereiro",
        '2': "março",
        '3': "abril",
        '4': "maio",
        '5': "junho",
        '6': "julho",
        '7': "agosto",
        '8': "setembro",
        '9': "outubro",
        '10': "novembro",
        '11': "dezembro",
    }
    return meses


# A função pede média retorna uma lista anual de temperaturas
def pedeMedias():
    temperaturas = []
    meses = ano()
    for mes in range(12):
        temp = int(
            input("Digite a temperatura do mês de " + meses[str(mes)] + ": ")
        )
        temperaturas.append(temp)
    return temperaturas


# A função calcula média retorna o cálculo de qualquer média (genérica)
def calculaMedia(lista):
    soma = 0
    for i in lista:
        soma = soma + i

    media = soma / len(lista)
    return media


# Criando uma lista de temperaturas
lista_de_temperaturas = pedeMedias()

# Calculando a média
media = calculaMedia(lista_de_temperaturas)

# Estabelecendo os meses do ano por extenso
meses = ano()

# A função enumerate retorna o indice e o valor das iterações da lista...
for indice, temperatura in enumerate(lista_de_temperaturas):
    if temperatura < media:
        print(
            "\nMês de "
            + meses[str(indice)]
            + " teve temperatura abaixo da média anual..."
        )
        print("A temperatura foi: " + str(temperatura) + "º graus Celsius")


# CÓDIGO UTILIZADO NO RACIOCÍNIO...
"""

def posicoesQueIniciamCom(lista, letra):
    result = []
    for i, palavra in enumerate(lista):
        if palavra.startswith(letra):
            result.append(i)
    return result

nomes = ['abc', 'hua', 'aaa', 'asdfg', 'bnm']
print posicoesQueIniciamCom(nomes,'a')
"""
