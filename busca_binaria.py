#!/usr/bin/venv python 
"""Implementação do algoritmo busca binária

"""
__version__ = "0.1.0"


def pesquisa_binaria(lista, item):
    baixo = 0 #mais baixo possivel
    alto = len(lista) - 1 #mais alto possivel é o ultimo numero 

    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        # o algoritmo binario sempre chuta um numero no meio do 
        # intervalo que esta testando
        chute = lista[meio] 
        if chute == item:
            return meio
        if chute > item:
            alto = meio -1
        else: 
            baixo = meio + 1
    return None

lista = [12,2,33,4,45,5,46,7,8,9,100]
lista.sort() # A lista precisa sempre ser ordenada
print(pesquisa_binaria(lista, 8)) #posicao 4
print(pesquisa_binaria(lista, 4)) #posicao 1

