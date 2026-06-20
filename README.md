# Lost Path

Projeto final da disciplina de Introdução a Algoritmos, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Aurelio Augusto
- Larissa Fineli
- Maria Luiza Queiroz
- Matheus Campos

## Descrição do jogo

Lost Path é um jogo de labirinto em 2D desenvolvido em Python utilizando a biblioteca Pygame. O jogador deve explorar o labirinto, coletar chaves coloridas para abrir portas correspondentes e encontrar a saída antes que o tempo acabe. Ao final da partida, o tempo é registrado em um ranking local com os melhores resultados.

## Objetivo do jogador

Encontrar a saída do labirinto antes que o tempo se esgote. Para isso, é necessário coletar as chaves corretas para abrir as portas que bloqueiam o caminho.

## Regras do jogo

- O jogador pode se mover em quatro direções.
- Não é possível atravessar paredes.
- Algumas portas bloqueiam o caminho.
- Cada porta só pode ser aberta após coletar sua chave correspondente.
- O jogador possui 60 segundos para escapar.
- O jogo pode ser pausado durante a partida.
- Ao vencer, o tempo é salvo em um ranking local.

## Controles

| Tecla | Ação |
|-------|------|
| W ou ↑ | Mover para cima |
| S ou ↓ | Mover para baixo |
| A ou ← | Mover para esquerda |
| D ou → | Mover para direita |
| ESC | Sair do jogo |
| p | Pausar jogo |

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/mariaqueirozz/lost-path.git
cd lost-path
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o jogo

```bash
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Estrutura do projeto

```
lost-path/
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências do projeto
├── README.md
├── src/
│   ├── config.py        # Configurações (tela, cores, velocidade)
│   ├── jogo.py          # Loop principal do jogo
│   ├── mapa.py          # Labirinto (matriz) e funções de desenho
    ├── ranking.py       # Salvamento e leitura do ranking
│   └── player.py        # Jogador: movimentação e colisão
├── assets/              # Imagens, sons e fontes (a adicionar)
├── data/                # Arquivos de dados (ranking, recorde)
├── docs/
│   └── proposta.md      # Proposta inicial do grupo
└── tests/
    └── test_mapa.py     # Testes unitários
```

## ## Funcionalidades

O jogo possui as seguintes funcionalidades:

- Movimentação utilizando as teclas **WASD** ou **setas direcionais**.
- Colisão com paredes do labirinto.
- Sistema de portas bloqueando o caminho.
- Coleta de chaves coloridas para desbloquear as portas correspondentes.
- Contador regressivo de tempo durante a partida.
- Sistema de pausa acionado pela tecla **P**.
- Tela inicial antes do início da partida.
- Tela de vitória com o tempo final do jogador.
- Tela de derrota quando o tempo se esgota.
- Ranking local com os melhores tempos registrados.
- Interface (HUD) exibindo o tempo restante e as chaves coletadas.



## Estado atual (Semana 2 – Protótipo)

- [x] Janela do Pygame funcionando
- [x] Loop principal implementado
- [x] Movimentação do jogador (WASD e setas)
- [x] Labirinto desenhado via matriz
- [x] Colisão com paredes funcionando
- [x] Célula de saída identificada
- [x] Tela de vitória com tempo
- [x] Código organizado em funções e módulos
- [x] Testes básicos implementados

## Estado atual (Semana 4 – Versão Final)

- [x] Tela inicial
- [x] Sistema de movimentação (WASD e setas)
- [x] Colisão com paredes
- [x] Labirinto desenhado por matriz
- [x] Sistema de portas e chaves coloridas
- [x] Contador regressivo de tempo
- [x] Tela de pausa
- [x] Tela de vitória
- [x] Tela de derrota
- [x] Ranking local de jogadores
- [x] Persistência de dados em arquivo texto
- [x] Testes automatizados
- [x] Código modularizado

