import json


def salvar_colecao(colecao, caminho):
   
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