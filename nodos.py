class NodoLista:
   
    def __init__(self, figurinha):
        self.figurinha = figurinha   # dado armazenado
        self.proximo = None          # referência para o próximo nó


class NodoFila:
    
    def __init__(self, valor):
        self.valor = valor           # dado armazenado (Figurinha, RegistroTroca...)
        self.proximo = None          # referência para o próximo nó