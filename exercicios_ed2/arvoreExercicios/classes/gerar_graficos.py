# exercicios_ed2/classes/gerar_graficos.py

import os

from graphviz import Digraph


class Gerar:
    def gerar_grafico(self, no, grafo=None, pasta='grafico_output'):
        if not os.path.exists(pasta):
            os.makedirs(pasta, exist_ok=True)

        if grafo is None:
            grafo = Digraph()

        if no:
            if no.esq:
                grafo.node(str(no.esq.item))
                grafo.edge(str(no.item), str(no.esq.item))
                self.gerar_grafico(no.esq, grafo, pasta)

            if no.dir:
                grafo.node(str(no.dir.item))
                grafo.edge(str(no.item), str(no.dir.item))
                self.gerar_grafico(no.dir, grafo, pasta)

        return grafo
