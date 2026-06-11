from dados_exemplo import (
    criar_colecao_exemplo,
    criar_colecao_amigo,
    figurinha_por_id,
    TOTAL_FIGURINHAS,
)
from historico import Historico
from trocas import efetuar_troca
from persistencia import salvar_colecao, carregar_colecao
from excecoes import ErroFigurinhas

ARQUIVO_PADRAO = "minha_colecao.json"


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


def acao_trocar(colecao, amigo, historico):
    print("\n--- Troca automática com o amigo ---")
    print(f"  Você ({colecao.dono}): {colecao.contar_repetidas()} repetidas")
    print(f"  Amigo ({amigo.dono}): {amigo.contar_repetidas()} repetidas")
    try:
        registro = efetuar_troca(colecao, amigo, historico)
        print("\n  Troca realizada!")
        print(f"  {registro}")
    except ErroFigurinhas as erro:
        print(f"  >> Não foi possível trocar: {erro}")


def acao_historico(historico):
    print("\n--- Histórico de trocas ---")
    print(historico.listar())
    print(f"\n  Total de trocas: {historico.quantidade()}")


def acao_salvar(colecao):
    try:
        salvar_colecao(colecao, ARQUIVO_PADRAO)
        print(f"\n  Coleção salva em '{ARQUIVO_PADRAO}'.")
    except OSError as erro:
        print(f"  >> Erro ao salvar: {erro}")


def acao_carregar():
    """Tenta carregar a coleção do arquivo. Retorna a Colecao ou None."""
    try:
        colecao = carregar_colecao(ARQUIVO_PADRAO)
        print(f"\n  Coleção de '{colecao.dono}' carregada de '{ARQUIVO_PADRAO}'.")
        return colecao
    except FileNotFoundError:
        print(f"  >> Arquivo '{ARQUIVO_PADRAO}' não encontrado.")
    except (OSError, ValueError, KeyError, ErroFigurinhas) as erro:
        print(f"  >> Erro ao carregar: {erro}")
    return None



def main():
    colecao = criar_colecao_exemplo("Voce")
    amigo = criar_colecao_amigo("Amigo")
    historico = Historico()

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
        elif opcao == "8":
            acao_trocar(colecao, amigo, historico)
        elif opcao == "9":
            acao_historico(historico)
        elif opcao == "10":
            acao_salvar(colecao)
        elif opcao == "11":
            nova = acao_carregar()
            if nova is not None:
                colecao = nova
        elif opcao == "0":
            print("\nAté a próxima! Boa sorte completando o álbum.")
            break
        else:
            print("  >> Opção inválida. Tente novamente.")

        pausar()


if __name__ == "__main__":
    main()