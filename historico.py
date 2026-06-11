from datetime import datetime
from fila import Fila


class RegistroTroca:
    def __init__(self, usuario_a, fig_a, usuario_b, fig_b):
        self.usuario_a = usuario_a   # quem ofereceu fig_a
        self.fig_a = fig_a           # figurinha que A entregou
        self.usuario_b = usuario_b   # quem ofereceu fig_b
        self.fig_b = fig_b           # figurinha que B entregou
        self.data = datetime.now()

    def __str__(self):
        quando = self.data.strftime("%d/%m/%Y %H:%M")
        return (f"[{quando}] {self.usuario_a} deu #{self.fig_a.id} ({self.fig_a.nome}) "
                f"<-> {self.usuario_b} deu #{self.fig_b.id} ({self.fig_b.nome})")

    def para_dict(self):
        return {
            "usuario_a": self.usuario_a,
            "fig_a": self.fig_a.para_dict(),
            "usuario_b": self.usuario_b,
            "fig_b": self.fig_b.para_dict(),
            "data": self.data.isoformat(),
        }


class Historico:
    def __init__(self):
        self._fila = Fila()

    def registrar(self, registro):
        
        self._fila.enqueue(registro)

    def quantidade(self):
        return self._fila.tamanho()

    def esta_vazio(self):
        return self._fila.esta_vazia()

    def listar(self):
      
        if self._fila.esta_vazia():
            return 
        linhas = []
        n = 1
        for registro in self._fila:
            linhas.append(f"{n}. {registro}")
            n += 1
        return "\n".join(linhas)

    def __iter__(self):
        return iter(self._fila)