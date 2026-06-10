"""
Nós (nodos) usados nas estruturas encadeadas do projeto.

NodoLista -> usado na lista encadeada do Álbum.
NodoFila  -> usado nas Filas (repetidas e histórico).

Cada nó guarda um dado e um ponteiro para o próximo nó. É com esses ponteiros
que montamos as estruturas "na mão", sem usar list/deque do Python.
"""


class NodoLista:
    """Nó da lista encadeada do álbum. Guarda uma Figurinha."""

    def __init__(self, figurinha):
        self.figurinha = figurinha   # dado armazenado
        self.proximo = None          # referência para o próximo nó


class NodoFila:
    """
    Nó da fila. Guarda um 'valor' genérico em vez de só uma Figurinha.

    Decisão de projeto: deixando o nó genérico, a MESMA classe Fila pode ser
    reutilizada para a fila de repetidas (que guarda Figurinhas) E para o
    Histórico (que guarda registros de troca). Reuso de código com uma única
    estrutura bem feita.
    """

    def __init__(self, valor):
        self.valor = valor           # dado armazenado (Figurinha, RegistroTroca...)
        self.proximo = None          # referência para o próximo nó