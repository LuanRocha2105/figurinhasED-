from figurinha import Figurinha
from colecao import Colecao

# (id, nome, pais, posicao, raridade)
CATALOGO = [
    (1,  "Alisson",        "Brasil",     "Goleiro",  "rara"),
    (2,  "Vinicius Jr",    "Brasil",     "Atacante", "lendaria"),
    (3,  "Rodrygo",        "Brasil",     "Atacante", "rara"),
    (4,  "Casemiro",       "Brasil",     "Volante",  "comum"),
    (5,  "Marquinhos",     "Brasil",     "Zagueiro", "comum"),
    (6,  "Brasil",         "Brasil",     "Escudo",   "lendaria"),
    (7,  "Messi",          "Argentina",  "Atacante", "lendaria"),
    (8,  "Julian Alvarez", "Argentina",  "Atacante", "rara"),
    (9,  "Dibu Martinez",  "Argentina",  "Goleiro",  "rara"),
    (10, "De Paul",        "Argentina",  "Meia",     "comum"),
    (11, "Argentina",      "Argentina",  "Escudo",   "lendaria"),
    (12, "Mbappe",         "Franca",     "Atacante", "lendaria"),
    (13, "Griezmann",      "Franca",     "Meia",     "rara"),
    (14, "Tchouameni",     "Franca",     "Volante",  "comum"),
    (15, "Franca",         "Franca",     "Escudo",   "lendaria"),
    (16, "Bellingham",     "Inglaterra", "Meia",     "lendaria"),
    (17, "Harry Kane",     "Inglaterra", "Atacante", "rara"),
    (18, "Saka",           "Inglaterra", "Atacante", "comum"),
    (19, "Inglaterra",     "Inglaterra", "Escudo",   "rara"),
    (20, "Cristiano Ronaldo", "Portugal", "Atacante", "lendaria"),
    (21, "Bruno Fernandes", "Portugal",  "Meia",     "rara"),
    (22, "Portugal",       "Portugal",   "Escudo",   "rara"),
    (23, "Modric",         "Croacia",    "Meia",     "rara"),
    (24, "Croacia",        "Croacia",    "Escudo",   "comum"),
]

TOTAL_FIGURINHAS = len(CATALOGO)


def figurinha_por_id(id):
    """Retorna uma Figurinha nova a partir do catálogo, pelo número."""
    for (cid, nome, pais, posicao, raridade) in CATALOGO:
        if cid == id:
            return Figurinha(cid, nome, pais, posicao, raridade)
    return None


def criar_colecao_exemplo(dono="Jogador 1"):
    """Cria uma coleção de exemplo já com algumas figurinhas e repetidas."""
    colecao = Colecao(dono, TOTAL_FIGURINHAS)
    # figurinhas que esse jogador "abriu nos pacotinhos" (alguns ids repetem!)
    abertas = [1, 2, 2, 4, 7, 7, 7, 11, 12, 16, 16, 20, 23]
    for id in abertas:
        fig = figurinha_por_id(id)
        if fig is not None:
            colecao.receber(fig)
    return colecao


def criar_colecao_amigo(dono="Jogador 2"):
    """Cria uma segunda coleção, útil para demonstrar as trocas."""
    colecao = Colecao(dono, TOTAL_FIGURINHAS)
    abertas = [3, 3, 5, 6, 8, 8, 13, 13, 17, 21, 21, 24]
    for id in abertas:
        fig = figurinha_por_id(id)
        if fig is not None:
            colecao.receber(fig)
    return colecao