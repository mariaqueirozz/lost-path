# Lost Path

Projeto final da disciplina de Introdução a Algoritmos, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Aurelio Augusto
- Larissa Fineli
- Maria Luiza Queiroz
- Matheus Campos

## Descrição do jogo

Lost Path é um jogo de labirinto em 2D onde o jogador controla um personagem (círculo verde) e precisa encontrar a saída do labirinto (célula dourada com "S") no menor tempo possível. O labirinto é composto por paredes e corredores, e o jogador não pode atravessar paredes.

## Objetivo do jogador

Encontrar a saída do labirinto (marcada com "S" dourado) no menor tempo possível.

## Regras do jogo

- O jogador se movimenta em quatro direções usando o teclado.
- Não é possível atravessar paredes.
- O jogo termina quando o jogador encontra a saída.
- O tempo é contado a partir do início da partida.

## Controles

| Tecla | Ação |
|-------|------|
| W ou ↑ | Mover para cima |
| S ou ↓ | Mover para baixo |
| A ou ← | Mover para esquerda |
| D ou → | Mover para direita |
| ESC | Sair do jogo |

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
│   └── player.py        # Jogador: movimentação e colisão
├── assets/              # Imagens, sons e fontes (a adicionar)
├── data/                # Arquivos de dados (ranking, recorde)
├── docs/
│   └── proposta.md      # Proposta inicial do grupo
└── tests/
    └── test_mapa.py     # Testes unitários
```

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
