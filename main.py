"""
main.py — Interface de texto (menu) do Sistema de Figurinhas da Copa.

Junta as classes do projeto e trata as entradas inválidas do usuário.
Rode com:  python main.py
"""

from dados_exemplo import criar_colecao_exemplo, figurinha_por_id, TOTAL_FIGURINHAS


# ---------------------------------------------------------------------- #
# Funções auxiliares de entrada (tratamento de entradas inválidas)
# ---------------------------------------------------------------------- #
def ler_inteiro(mensagem):
    """Lê um inteiro do usuário, repetindo até a entrada ser válida."""
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("  >> Entrada inválida: digite um número inteiro.\n")


def pausar():
    input("\n(enter para continuar) ")


# ---------------------------------------------------------------------- #
# Ações do menu
# ---------------------------------------------------------------------- #
def acao_inserir(colecao):
    print("\n--- Inserir figurinha (pelo número do catálogo) ---")
    id = ler_inteiro("Número da figurinha: ")
    fig = figurinha_por_id(id)
    if fig is None:
        print(f"  >> Não existe figurinha #{id} no catálogo (1 a {TOTAL_FIGURINHAS}).")
        return
    destino = colecao.receber(fig)
    if destino == "album":
        print(f"  Figurinha {fig} colada no ÁLBUM!")
    else:
        print(f"  Você já tinha essa! {fig} foi para as REPETIDAS.")


def acao_remover(colecao):
    print("\n--- Remover figurinha do álbum ---")
    id = ler_inteiro("Número da figurinha: ")
    removida = colecao.remover_do_album(id)
    if removida is None:
        print(f"  >> A figurinha #{id} não está no seu álbum.")
    else:
        print(f"  Removida: {removida}")


def acao_consultar(colecao):
    print("\n--- Consultar figurinha no álbum ---")
    id = ler_inteiro("Número da figurinha: ")
    fig = colecao.album.buscar(id)
    if fig is None:
        print(f"  >> A figurinha #{id} ainda não está no seu álbum.")
    else:
        print(f"  Encontrada: {fig}")


def acao_ver_album(colecao):
    print("\n--- Álbum completo ---")
    print(colecao.album.ver_completo())
    print(f"\n  {colecao.album.tamanho()} de {colecao.album.total_figurinhas} figurinhas.")


def acao_porcentagem(colecao):
    pct = colecao.album.porcentagem_concluida()
    print(f"\n  Álbum {pct:.1f}% concluído "
          f"({colecao.album.tamanho()}/{colecao.album.total_figurinhas}).")


def acao_repetidas(colecao):
    print("\n--- Figurinhas repetidas ---")
    print(colecao.listar_repetidas())
    print(f"\n  Total de repetidas: {colecao.contar_repetidas()}")


def acao_buscar(colecao):
    print("\n--- Buscar ---")
    print("  1) Por número")
    print("  2) Por jogador")
    print("  3) Por seleção")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        id = ler_inteiro("Número: ")
        fig = colecao.album.buscar(id)
        print(f"  {fig}" if fig else f"  >> #{id} não está no álbum.")
    elif opcao == "2":
        nome = input("Nome do jogador: ").strip()
        achou = False
        for fig in colecao.album.buscar_por_jogador(nome):
            print(f"  {fig}")
            achou = True
        if not achou:
            print("  >> Nenhum jogador encontrado.")
    elif opcao == "3":
        pais = input("Seleção: ").strip()
        achou = False
        for fig in colecao.album.buscar_por_selecao(pais):
            print(f"  {fig}")
            achou = True
        if not achou:
            print("  >> Nenhuma figurinha dessa seleção no álbum.")
    else:
        print("  >> Opção inválida.")


# ---------------------------------------------------------------------- #
# Menu principal
# ---------------------------------------------------------------------- #
MENU = """
==================== ALBUM DA COPA 2026 ====================
 1 - Inserir figurinha     5 - Ver porcentagem
 2 - Remover figurinha      6 - Ver repetidas
 3 - Consultar figurinha    7 - Buscar (num/jogador/selecao)
 4 - Ver album completo     0 - Sair
===========================================================
"""


def main():
    colecao = criar_colecao_exemplo("Voce")
    print("Bem-vindo ao Sistema de Figurinhas da Copa!")
    print("(uma coleção de exemplo já foi carregada para você testar)")

    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            acao_inserir(colecao)
        elif opcao == "2":
            acao_remover(colecao)
        elif opcao == "3":
            acao_consultar(colecao)
        elif opcao == "4":
            acao_ver_album(colecao)
        elif opcao == "5":
            acao_porcentagem(colecao)
        elif opcao == "6":
            acao_repetidas(colecao)
        elif opcao == "7":
            acao_buscar(colecao)
        elif opcao == "0":
            print("\nAté a próxima!")
            break
        else:
            print("  >> Opção inválida. Tente novamente.")

        pausar()


if __name__ == "__main__":
    main()