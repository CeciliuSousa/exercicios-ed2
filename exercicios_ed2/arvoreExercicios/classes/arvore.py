# exercicios_ed2/classes/arvore.py

from classes.gerar_graficos import Gerar


class No:
    def __init__(self, key):
        self.item = key
        self.esq = None
        self.dir = None

class Arvore:
    def __init__(self):
        self.root = None

    def inserir(self, v):
        novo = No(v)

        if self.root is None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item:
                    atual = atual.esq
                    if atual is None:
                        anterior.esq = novo
                        return
                else:
                    atual = atual.dir
                    if atual is None:
                        anterior.dir = novo
                        return

    def gerar_grafico(self):
        gerador = Gerar()
        return gerador.gerar_grafico(self.root)
