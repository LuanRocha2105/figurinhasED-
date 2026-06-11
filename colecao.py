from album import Album
from fila import Fila
from excecoes import FigurinhaDuplicadaError


class Colecao:
    def __init__(self, dono, total_figurinhas):
        self.dono = dono
        self.album = Album(total_figurinhas)
        self.repetidas = Fila()

    
    def receber(self, figurinha):
        """
        Recebe uma figurinha e a encaminha para o álbum ou para as repetidas.
        Retorna a string "album" ou "repetida" para o chamador saber o destino.
        """
        try:
            self.album.adicionar(figurinha)
            return "album"
        except FigurinhaDuplicadaError:
            self.repetidas.enqueue(figurinha)
            return "repetida"

    def remover_do_album(self, id):
        """Remove uma figurinha do álbum. Retorna a Figurinha ou None."""
        return self.album.remover(id)

    
    def contar_repetidas(self):
        return self.repetidas.tamanho()

    def tem_repetida(self):
        return not self.repetidas.esta_vazia()

    def listar_repetidas(self):
        """Retorna uma string com as figurinhas repetidas (da mais antiga p/ mais nova)."""
        if self.repetidas.esta_vazia():
            return "(sem repetidas)"
        linhas = []
        for fig in self.repetidas:          # usa o __iter__ da Fila (não remove nada)
            linhas.append(str(fig))
        return "\n".join(linhas)

    def proxima_repetida(self):
        """Espia a próxima repetida que sairia em uma troca (sem remover)."""
        return self.repetidas.peek()

    def retirar_repetida(self):
        """Retira (dequeue) a repetida mais antiga para usar em uma troca."""
        return self.repetidas.dequeue()