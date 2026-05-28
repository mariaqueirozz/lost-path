# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Lost Path

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Aurelio Augusto
- Nome 2: Larissa Fineli
- Nome 3: Maria Luiza Queiroz
- Nome 4: Matheus Campos

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Tipo escolhido pelo grupo:

> Labirinto simples em 2D

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Descrição:

> O jogo “Lost Path” será um jogo de labirinto em 2D onde o jogador controla um personagem que precisa encontrar a saída do mapa. O cenário será formado por paredes e corredores, criando caminhos que o jogador deverá explorar até encontrar o final do labirinto. Durante a partida, o jogador precisará evitar obstáculos e percorrer o caminho correto para concluir o jogo. O jogo contará com movimentação simples, sistema de colisão e tela de vitória

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Objetivo:

> O objetivo do jogador é encontrar a saída do labirinto no menor tempo possível sem colidir com obstáculos.

## 6. Regras principais

Liste as principais regras do jogo.

Regras do grupo:

- Regra 1: O jogador poderá se movimentar em quatro direções utilizando o teclado.
- Regra 2: O personagem não poderá atravessar paredes do labirinto.
- Regra 3: O jogador deverá encontrar a saída do mapa para vencer.
- Regra 4: Caso exista obstáculo ou inimigo, o jogador perderá ao encostar nele.
- Regra 5: O jogo poderá possuir contagem de tempo para aumentar o desafio.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Condição de vitória:

> O jogador vence ao encontrar a saída do labirinto.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Condição de derrota ou encerramento:

> O jogador perde ao colidir com obstáculos ou caso o tempo da partida termine.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Descrição:

> Um personagem controlado pelo teclado que poderá andar pelos corredores do labirinto

## Obstáculos, inimigos ou desafios

Descrição:

> Paredes impedirão a movimentação do jogador e poderão existir obstáculos ou inimigos simples espalhados pelo mapa.

## Itens, alvos ou objetos de interação

Descrição:

> A saída do labirinto será o principal objetivo do jogador. Poderão existir chaves ou itens simples para interação.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogo poderá possuir cronômetro e sistema simples de pontuação baseado no tempo levado para concluir o labirinto.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Controles do grupo:

- Tecla/comando: W ou seta para cima — mover para cima
- Tecla/comando: S ou seta para baixo — mover para baixo
- Tecla/comando: A ou seta para esquerda — mover para esquerda
- Tecla/comando: D ou seta para direita — mover para direita
- Tecla/comando: ESC — sair do jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Organização planejada:

> - main.py: inicia o jogo e executa o loop principal;
- player.py: controla a movimentação do jogador;
- mapa.py: contém a criação do labirinto;
- config.py: armazena configurações como tamanho da tela, cores e velocidade;
- colisao.py: controla colisões entre jogador e paredes.

## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Recursos previstos:

> - Imagens gratuitas para o personagem e cenário;
- Efeitos sonoros gratuitos;
- Tutoriais de Python e Pygame utilizados apenas como referência.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Dificuldades previstas:

- Dificuldade 1: Implementar colisão entre jogador e paredes.
- Dificuldade 2: Criar o labirinto utilizando matriz.
- Dificuldade 3: Organizar corretamente o código em arquivos separados.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Escopo mínimo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, um mapa de labirinto funcional, colisão com paredes, objetivo de encontrar a saída e tela de vitória.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Melhorias possíveis:

- Melhoria 1: Tela inicial do jogo.
- Melhoria 2: Sistema de fases.
- Melhoria 3: Sons, cronômetro e aumento de dificuldade.