# -*- coding: utf-8 -*-

"""
15  Utilize uma lista para resolver o problema a seguir.
    Uma empresa paga seus vendedores com base em comissões. O vendedor recebe
    $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
    Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
    recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
    Escreva um programa (usando um array de contadores) que determine quantos
    vendedores receberam salários nos seguintes intervalos de valores:
    A - $200 - $299
    B - $300 - $399
    C - $400 - $499
    D - $500 - $599
    E - $600 - $699
    F - $700 - $799
    G - $800 - $899
    H - $900 - $999
    I - $1000 em diante
"""


def criaListas(qtd):
    salarios = []
    vendas = []
    for vendedor in range(qtd):
        salario = input(
            "Digite o salario do vendedor " + str(vendedor + 1) + ": "
        )
        salarios.append(float(salario))
        venda = input(
            "Digite quanto o vendedor "
            + str(vendedor + 1)
            + " conseguiu vender na semana: "
        )
        vendas.append(float(venda))
    return salarios, vendas


def aplicaComissao(salarios, vendas):
    novoSalarios = []
    for salario in salarios:
        for venda in vendas:
            calculo = 0.09 * venda
        salario = salario + calculo
        novoSalarios.append(salario)
    return novoSalarios


def contabilizaSalarios(listaSalarios):
    a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0

    for salario in listaSalarios:
        if salario in range(200, 299):
            a += 1
        elif salario in range(300, 399):
            b += 1
        elif salario in range(400, 499):
            c += 1
        elif salario in range(500, 599):
            d += 1
        elif salario in range(600, 699):
            e += 1
        elif salario in range(700, 799):
            f += 1
        elif salario in range(800, 899):
            g += 1
        elif salario in range(900, 999):
            h += 1
        elif salario >= 1000:
            i += 1
        else:
            pass
    return a, b, c, d, e, f, g, h, i


listaDeSalarios, listaDeVendas = criaListas(2)
novoSalarios = aplicaComissao(listaDeSalarios, listaDeVendas)

print("\nSalários com aumento de 9%:", novoSalarios)
print(
    """
Vendedores com salário igual a:
A - 200 - 299: %s
B - 300 - 399: %s
C - 400 - 499: %s
D - 500 - 599: %s
E - 600 - 699: %s
F - 700 - 799: %s
G - 800 - 899: %s
H - 900 - 999: %s
I -   >= 1000: %s
    """
    % (contabilizaSalarios(novoSalarios))
)
