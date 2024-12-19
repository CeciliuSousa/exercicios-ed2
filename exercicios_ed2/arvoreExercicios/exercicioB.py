# exercicios_ed2/pagina70.py

import os

from classes.arvore import Arvore
from classes.gerar_graficos import Gerar


def arvore_altura_2():
    elementos = [10, 5, 17]
    arvore = Arvore()
    for elemento in elementos:
        arvore.inserir(elemento)
    return arvore

def arvore_altura_3():
    elementos = [10, 5, 17, 1]
    arvore = Arvore()
    for elemento in elementos:
        arvore.inserir(elemento)
    return arvore

def arvore_altura_4():
    elementos = [10, 5, 17, 1, 4]
    arvore = Arvore()
    for elemento in elementos:
        arvore.inserir(elemento)
    return arvore

def arvore_altura_5():
    elementos = [10, 5, 17, 1, 4, 16]
    arvore = Arvore()
    for elemento in elementos:
        arvore.inserir(elemento)
    return arvore

def arvore_altura_6():
    elementos = [10, 5, 17, 1, 4, 16, 21]
    arvore = Arvore()
    for elemento in elementos:
        arvore.inserir(elemento)
    return arvore

def gerar_graficos():
    gerar = Gerar()

    pasta_output = 'grafico_output'
    if not os.path.exists(pasta_output):
        os.makedirs(pasta_output)

    arvore2 = arvore_altura_2()
    grafo2 = gerar.gerar_grafico(arvore2.root)
    grafo2.render(os.path.join(pasta_output, 'arvore_altura_2'), format='png', view=True)

    arvore3 = arvore_altura_3()
    grafo3 = gerar.gerar_grafico(arvore3.root)
    grafo3.render(os.path.join(pasta_output, 'arvore_altura_3'), format='png', view=True)

    arvore4 = arvore_altura_4()
    grafo4 = gerar.gerar_grafico(arvore4.root)
    grafo4.render(os.path.join(pasta_output, 'arvore_altura_4'), format='png', view=True)

    arvore5 = arvore_altura_5()
    grafo5 = gerar.gerar_grafico(arvore5.root)
    grafo5.render(os.path.join(pasta_output, 'arvore_altura_5'), format='png', view=True)

    arvore6 = arvore_altura_6()
    grafo6 = gerar.gerar_grafico(arvore6.root)
    grafo6.render(os.path.join(pasta_output, 'arvore_altura_6'), format='png', view=True)

gerar_graficos()
