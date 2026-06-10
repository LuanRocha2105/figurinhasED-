"""
Classe Figurinha — entidade central do sistema.

Cada figurinha representa um jogador ou uma seleção da Copa.
A validação é feita no próprio construtor para garantir que nunca exista
uma figurinha em estado inválido dentro das estruturas de dados.
"""

from excecoes import FigurinhaInvalidaError

# Raridades aceitas. Uso uma tupla (imutável) só para validar a entrada;
# isso NÃO é uma estrutura de dados do projeto, é apenas uma lista de opções.
RARIDADES_VALIDAS = ("comum", "rara", "lendaria", "legendaria")


class Figurinha:
    def __init__(self, id, nome, pais, posicao, raridade):
        # --- validação de entrada ---
        if not isinstance(id, int) or id <= 0:
            raise FigurinhaInvalidaError(
                f"Número da figurinha inválido: {id!r} (deve ser inteiro positivo)."
            )
        if not nome or not str(nome).strip():
            raise FigurinhaInvalidaError("Nome do jogador não pode ser vazio.")
        if not pais or not str(pais).strip():
            raise FigurinhaInvalidaError("Seleção (país) não pode ser vazia.")

        raridade = str(raridade).strip().lower()
        if raridade not in RARIDADES_VALIDAS:
            raise FigurinhaInvalidaError(
                f"Raridade inválida: {raridade!r}. "
                f"Use uma destas: {', '.join(RARIDADES_VALIDAS)}."
            )

        self.id = id
        self.nome = str(nome).strip()
        self.pais = str(pais).strip()
        self.posicao = str(posicao).strip()
        self.raridade = raridade

    def __str__(self):
        return (f"#{self.id:>3} | {self.nome} ({self.pais}) "
                f"- {self.posicao} [{self.raridade}]")

    def __repr__(self):
        return f"Figurinha(id={self.id}, nome={self.nome!r}, pais={self.pais!r})"

    def para_dict(self):
        """Converte a figurinha em dicionário (usado na persistência JSON)."""
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "posicao": self.posicao,
            "raridade": self.raridade,
        }

    @staticmethod
    def de_dict(d):
        """Reconstrói uma Figurinha a partir de um dicionário."""
        return Figurinha(
            id=int(d["id"]),
            nome=d["nome"],
            pais=d["pais"],
            posicao=d["posicao"],
            raridade=d["raridade"],
        )