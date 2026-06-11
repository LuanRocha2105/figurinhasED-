# Figurinhas da Copa 2026

Sistema de gerenciamento de figurinhas da Copa do Mundo

Permite colecionar, trocar e organizar figurinhas de jogadores e seleções

- **Lista encadeada** → o álbum (figurinhas únicas, mantidas em ordem por número);
- **Fila FIFO** → as figurinhas repetidas e o histórico de trocas.


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

