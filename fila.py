"""
Classe Fila — implementação própria de fila FIFO (First In, First Out).

Mantemos dois ponteiros:
  _inicio -> primeiro nó (de onde sai no dequeue)
  _fim    -> último nó   (onde entra no enqueue)

Guardar o _fim permite enqueue em O(1) (sem percorrer a fila toda).
Nada de list/deque do Python: tudo com NodoFila encadeados.
"""

from nodos import NodoFila


class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._inicio is None

    def tamanho(self):
        return self._tamanho

    def enqueue(self, valor):
        """Insere um elemento no FIM da fila."""
        novo = NodoFila(valor)
        if self.esta_vazia():
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self):
        """Remove e retorna o elemento do INÍCIO da fila (ou None se vazia)."""
        if self.esta_vazia():
            return None
        nodo = self._inicio
        self._inicio = nodo.proximo
        if self._inicio is None:      # a fila ficou vazia
            self._fim = None
        self._tamanho -= 1
        return nodo.valor

    def peek(self):
        """Espia o elemento do início SEM remover (ou None se vazia)."""
        if self.esta_vazia():
            return None
        return self._inicio.valor

    def limpar(self):
        """Esvazia a fila."""
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def __iter__(self):
        """Permite percorrer a fila (for x in fila) sem remover os elementos."""
        atual = self._inicio
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self._tamanho