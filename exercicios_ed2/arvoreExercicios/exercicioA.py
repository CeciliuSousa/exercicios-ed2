# exercicios_ed2/pagina69.py

import os

from classes.arvore import Arvore
from classes.gerar_graficos import Gerar


def gerar_graficos():
    arvore = Arvore()
    gerar = Gerar()

    pasta_output = 'grafico_output'
    if not os.path.exists(pasta_output):
        os.makedirs(pasta_output, exist_ok=True)

    elementos = [9, 10, 2, 12, 8, 7, 1, 13, 4, 5, 6, 3, 11]

    for elemento in elementos:
        arvore.inserir(elemento)

    grafo = gerar.gerar_grafico(arvore.root)
    grafo.render(os.path.join(pasta_output, 'arvore_binaria'), format='png', view=True)

gerar_graficos()