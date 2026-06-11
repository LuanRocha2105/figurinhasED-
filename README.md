# Figurinhas da Copa 2026

Sistema de gerenciamento de figurinhas da Copa do Mundo, desenvolvido para a
disciplina de **Estrutura de Dados** (Fatec Rio Claro).

Permite **colecionar, trocar e organizar** figurinhas de jogadores e seleções,
usando estruturas de dados implementadas **do zero**:

- **Lista encadeada** → o álbum (figurinhas únicas, mantidas em ordem por número);
- **Fila FIFO** → as figurinhas repetidas e o histórico de trocas.

> Nenhuma estrutura pronta do Python (`list`, `deque`, etc.) é usada para
> *implementar* essas estruturas — tudo é feito com nós encadeados (`NodoLista`
> e `NodoFila`). `list` só aparece pontualmente na serialização JSON.

## Como rodar

```bash
python main.py
```

Sem dependências externas (apenas a biblioteca padrão do Python 3).
Ao iniciar, já vem uma coleção de exemplo carregada para facilitar os testes.

## Estrutura dos arquivos

| Arquivo            | Responsabilidade |
|--------------------|------------------|
| `excecoes.py`      | Exceções de domínio (entradas inválidas) |
| `figurinha.py`     | Classe `Figurinha` (entidade) + validação |
| `nodos.py`         | `NodoLista` e `NodoFila` (nós encadeados) |
| `fila.py`          | Classe `Fila` (FIFO própria) |
| `album.py`         | Classe `Album` (lista encadeada) |
| `colecao.py`       | Classe `Colecao` (álbum + fila de repetidas) |
| `historico.py`     | `RegistroTroca` + `Historico` (fila de trocas) |
| `trocas.py`        | Regras de troca entre coleções |
| `persistencia.py`  | Salvar/carregar em JSON |
| `dados_exemplo.py` | Catálogo de figurinhas e dados de teste |
| `main.py`          | Menu interativo no terminal |

## Decisões de projeto (resumo para defesa)

- **Lista encadeada no álbum:** cresce conforme o usuário cola figurinhas, sem
  redimensionar nada. Inserção **ordenada por número** → o álbum sai em ordem.
- **Fila (FIFO) nas repetidas:** justo trocar primeiro a repetida há mais tempo
  "encalhada" — a primeira que entra é a primeira a sair.
- **Fila genérica reutilizada:** o `NodoFila` guarda um `valor` genérico, então a
  **mesma** `Fila` serve para repetidas (`Figurinha`) e histórico (`RegistroTroca`).
- **Separação de responsabilidades:** cada classe tem um papel único; o `main`
  só cuida da interface e do tratamento das entradas.

## Funcionalidades atendidas

**Álbum:** inserir, remover, consultar, ver completo, ver % concluída.
**Repetidas:** armazenar, listar, contar.
**Buscas:** por número, por jogador, por seleção.
**Trocas:** propor, verificar se ambos têm repetidas, efetuar troca automática.
**Persistência:** salvar e carregar em **JSON**.
**Robustez:** tratamento de entradas inválidas (número, seleção, raridade...).