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
                    
    def pre_ordem(self, raiz):
        elementos = []
        if raiz:
            elementos.append(raiz.item)
            elementos.extend(self.pre_ordem(raiz.esq))
            elementos.extend(self.pre_ordem(raiz.dir))
        return elementos

    def pos_ordem(self, raiz):
        elementos = []
        if raiz:
            elementos.extend(self.pos_ordem(raiz.esq))
            elementos.extend(self.pos_ordem(raiz.dir))
            elementos.append(raiz.item)
        return elementos

    def in_ordem(self, raiz):
        elementos = []
        if raiz:
            elementos.extend(self.in_ordem(raiz.esq))
            elementos.append(raiz.item)
            elementos.extend(self.in_ordem(raiz.dir))
        return elementos

    def ordenar(self):
        return self.in_ordem(self.root)

    def equilibrar(self):
        elementos = self.ordenar()
        
        def reconstruir_arvore(elementos):
            if not elementos:
                return None
            meio = len(elementos) // 2
            raiz = No(elementos[meio])
            raiz.esq = reconstruir_arvore(elementos[:meio])
            raiz.dir = reconstruir_arvore(elementos[meio+1:])
            return raiz

        self.root = reconstruir_arvore(elementos)

    def gerar_grafico(self):
        gerador = Gerar()
        return gerador.gerar_grafico(self.root)
