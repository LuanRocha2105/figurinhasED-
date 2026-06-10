"""
Lógica de trocas entre duas coleções.

Regras (do enunciado):
  - Registrar proposta de troca;
  - Verificar se AMBOS possuem repetidas;
  - Efetuar a troca automática.
"""

from excecoes import TrocaInvalidaError


def verificar_troca(colecao_a, colecao_b):
    """
    Verifica se a troca é possível: ambos precisam ter pelo menos uma repetida.
    Levanta TrocaInvalidaError explicando o motivo, se não for possível.
    """
    if not colecao_a.tem_repetida():
        raise TrocaInvalidaError(
            f"{colecao_a.dono} não tem figurinhas repetidas para trocar."
        )
    if not colecao_b.tem_repetida():
        raise TrocaInvalidaError(
            f"{colecao_b.dono} não tem figurinhas repetidas para trocar."
        )
    return True