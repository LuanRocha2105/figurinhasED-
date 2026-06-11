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
        return self.buscar(id) is not None

    def buscar(self, id):
        
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    
    def adicionar(self, figurinha):
        if self.contem(figurinha.id):
            raise FigurinhaDuplicadaError(
                f"A figurinha #{figurinha.id} já está colada no álbum."
            )
        novo = NodoLista(figurinha)
        if self._cabeca is None or figurinha.id < self._cabeca.figurinha.id:
            novo.proximo = self._cabeca
            self._cabeca = novo
        else:
            atual = self._cabeca
            while atual.proximo is not None and atual.proximo.figurinha.id < figurinha.id:
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo
        self._tamanho += 1
        return True

    def remover(self, id):
        atual = self._cabeca
        anterior = None
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return atual.figurinha
            anterior = atual
            atual = atual.proximo
        return None

    
    def ver_completo(self):
        if self._cabeca is None:
            return "(álbum vazio)"
        linhas = []
        atual = self._cabeca
        while atual is not None:
            linhas.append(str(atual.figurinha))
            atual = atual.proximo
        return "\n".join(linhas)

    def porcentagem_concluida(self):
        return (self._tamanho / self.total_figurinhas) * 100

    


    def buscar_por_jogador(self, nome):
       
        alvo = nome.strip().lower()
        atual = self._cabeca
        while atual is not None:
            if alvo in atual.figurinha.nome.lower():
                yield atual.figurinha
            atual = atual.proximo

    def buscar_por_selecao(self, pais):
        
        alvo = pais.strip().lower()
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.pais.lower() == alvo:
                yield atual.figurinha
            atual = atual.proximo

    def __iter__(self):
        atual = self._cabeca
        while atual is not None:
            yield atual.figurinha
            atual = atual.proximo