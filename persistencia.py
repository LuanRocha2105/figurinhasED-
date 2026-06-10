"""
Persistência em JSON — salva uma coleção (álbum + repetidas).

Observação sobre o requisito técnico:
O JSON exige listas/dicionários do Python apenas no MOMENTO de serializar
(transformar em texto). Isso NÃO viola a regra, porque a regra proíbe usar
list/deque para IMPLEMENTAR as estruturas de dados. Aqui as estruturas
continuam sendo lista encadeada e fila; a list aparece só na "ponte" de I/O.
"""

import json


def salvar_colecao(colecao, caminho):
    """Salva a coleção (álbum + repetidas) em um arquivo JSON."""
    dados = {
        "dono": colecao.dono,
        "total_figurinhas": colecao.album.total_figurinhas,
        # percorre o álbum (lista encadeada) gerando os dicionários
        "album": [fig.para_dict() for fig in colecao.album],
        # percorre a fila de repetidas gerando os dicionários
        "repetidas": [fig.para_dict() for fig in colecao.repetidas],
    }
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)