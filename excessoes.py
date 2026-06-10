"""
Exceções de domínio do sistema de figurinhas.

Centralizar os erros em uma classe base (ErroFigurinhas) deixa o tratamento
de entradas inválidas mais organizado: no menu basta capturar ErroFigurinhas
para pegar qualquer erro previsto pela regra de negócio.
"""


class ErroFigurinhas(Exception):
    """Classe base para todos os erros do sistema."""
    pass


class FigurinhaInvalidaError(ErroFigurinhas):
    """Dados da figurinha estão incorretos (id, nome, raridade...)."""
    pass


class SelecaoInvalidaError(ErroFigurinhas):
    """Código/nome de seleção não reconhecido."""
    pass


class FigurinhaDuplicadaError(ErroFigurinhas):
    """Tentativa de inserir no álbum uma figurinha que já existe nele."""
    pass


class TrocaInvalidaError(ErroFigurinhas):
    """A troca não pode ser realizada (falta de repetidas, etc.)."""
    pass