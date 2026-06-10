"""
Classe Album — representação do álbum da Copa, feita como LISTA ENCADEADA.

O álbum guarda apenas figurinhas ÚNICAS. As repetidas ficam em uma Fila
separada (controlada pela classe Colecao, criada mais adiante).

  _cabeca -> primeiro nó da lista
  _tamanho -> quantas figurinhas únicas já foram coladas
  total_figurinhas -> total que o álbum completo deve ter (para a %)
"""

from nodos import NodoLista


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