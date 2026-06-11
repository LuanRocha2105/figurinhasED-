from historico import RegistroTroca
from excecoes import TrocaInvalidaError


def verificar_troca(colecao_a, colecao_b):
    
    if not colecao_a.tem_repetida():
        raise TrocaInvalidaError(
            f"{colecao_a.dono} não tem figurinhas repetidas para trocar."
        )
    if not colecao_b.tem_repetida():
        raise TrocaInvalidaError(
            f"{colecao_b.dono} não tem figurinhas repetidas para trocar."
        )
    return True


def efetuar_troca(colecao_a, colecao_b, historico):
    
    # 1) valida antes de mexer em qualquer coisa
    verificar_troca(colecao_a, colecao_b)

    # 2) cada um entrega a repetida mais antiga (dequeue)
    fig_a = colecao_a.retirar_repetida()
    fig_b = colecao_b.retirar_repetida()

    # 3) cada um recebe a figurinha do outro
    #    receber() já decide sozinho: vai pro álbum (se for nova) ou pras repetidas
    colecao_b.receber(fig_a)
    colecao_a.receber(fig_b)

    # 4) registra a troca no histórico
    registro = RegistroTroca(colecao_a.dono, fig_a, colecao_b.dono, fig_b)
    historico.registrar(registro)
    return registro