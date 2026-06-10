"""
Classe Album — representação do álbum da Copa, feita como LISTA ENCADEADA.

O álbum guarda apenas figurinhas ÚNICAS. As repetidas ficam em uma Fila
separada (controlada pela classe Colecao, criada mais adiante).
"""

from nodos import NodoLista
from excecoes import FigurinhaDuplicadaError


class Album:
    def __init__(self, total_figurinhas):
        if not isinstance(total_figurinhas, int) or total_figurinhas <= 0:
            raise ValueError("total_figurinhas deve ser um inteiro positivo.")
        self._cabeca = None
        self._tamanho = 0
        self.total_figurinhas = total_figurinhas

    def tamanho(self):
        return self._tamanho

    def contem(self, id):
        """Retorna True se a figurinha de número 'id' já está colada."""
        return self.buscar(id) is not None

    def buscar(self, id):
        """Busca por número da figurinha. Retorna a Figurinha ou None."""
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    def adicionar(self, figurinha):
        """
        Adiciona uma figurinha nova no álbum (inserção ordenada por id).
        Se já existir, levanta FigurinhaDuplicadaError (o chamador decide se
        manda para as repetidas).
        """
        if self.contem(figurinha.id):
            raise FigurinhaDuplicadaError(
                f"A figurinha #{figurinha.id} já está colada no álbum."
            )

        novo = NodoLista(figurinha)

        # Caso 1: lista vazia ou inserir antes da cabeça (mantém ordenado por id)
        if self._cabeca is None or figurinha.id < self._cabeca.figurinha.id:
            novo.proximo = self._cabeca
            self._cabeca = novo
        else:
            # Caso 2: procura a posição correta para manter a ordem crescente
            atual = self._cabeca
            while atual.proximo is not None and atual.proximo.figurinha.id < figurinha.id:
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo

        self._tamanho += 1
        return True