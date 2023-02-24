#!/usr/bin/venv python3
"""Ordendo arrays com recursividade
"""

"""
Retorna o menor valor do array
"""


def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordena(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


arr = [12, 43, 5, 67, 13, 99, 56, 21, 23, 2]
print(buscaMenor(arr))  # 9
print(ordena(arr))  # [2, 5, 12, 13, 21, 23, 43, 56, 67, 99]
