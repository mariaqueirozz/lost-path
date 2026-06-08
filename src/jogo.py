# jogo.py
# Contém o loop principal do jogo Lost Path

import pygame
import time
from src.config import (
    LARGURA_TELA, ALTURA_TELA, TITULO, FPS,
    COR_FUNDO, COR_TEXTO, COR_TEMPO
)
from src.mapa import desenhar_mapa, obter_paredes, obter_saida, obter_posicao_inicial
from src.player import Jogador, processar_movimento


def desenhar_hud(tela, fonte, tempo_decorrido):
    """
    Desenha o HUD (informações na tela): tempo e controles.
    HUD = Head-Up Display, são as informações exibidas para o jogador.
    """
    # Exibe o tempo no canto superior esquerdo
    minutos = int(tempo_decorrido) // 60
    segundos = int(tempo_decorrido) % 60
    texto_tempo = fonte.render(f"Tempo: {minutos:02d}:{segundos:02d}", True, COR_TEMPO)
    tela.blit(texto_tempo, (10, 10))

    # Dica de controles no canto superior direito
    texto_dica = fonte.render("WASD ou setas para mover | ESC sair", True, COR_TEXTO)
    tela.blit(texto_dica, (LARGURA_TELA - texto_dica.get_width() - 10, 10))


def tela_vitoria(tela, fonte_grande, fonte_pequena, tempo_decorrido):
    """
    Exibe a tela de vitória com o tempo do jogador.
    Fica aguardando o jogador pressionar qualquer tecla para sair.
    """
    tela.fill((20, 20, 20))

    # Título
    texto_vitoria = fonte_grande.render("VOCÊ VENCEU!", True, (255, 215, 0))
    x = LARGURA_TELA // 2 - texto_vitoria.get_width() // 2
    tela.blit(texto_vitoria, (x, 200))

    # Tempo final
    minutos = int(tempo_decorrido) // 60
    segundos = int(tempo_decorrido) % 60
    texto_tempo = fonte_pequena.render(f"Seu tempo: {minutos:02d}:{segundos:02d}", True, COR_TEXTO)
    x_tempo = LARGURA_TELA // 2 - texto_tempo.get_width() // 2
    tela.blit(texto_tempo, (x_tempo, 300))

    # Instrução
    texto_sair = fonte_pequena.render("Pressione qualquer tecla para sair", True, (180, 180, 180))
    x_sair = LARGURA_TELA // 2 - texto_sair.get_width() // 2
    tela.blit(texto_sair, (x_sair, 380))

    pygame.display.flip()

    # Aguarda o jogador pressionar uma tecla
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                aguardando = False
            if evento.type == pygame.KEYDOWN:
                aguardando = False


def executar_jogo():
    """
    Função principal: inicializa o Pygame, cria os objetos e roda o loop do jogo.
    """
    # Inicializa todos os módulos do Pygame
    pygame.init()

    # Cria a janela
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO)

    # Relógio para controlar o FPS
    relogio = pygame.time.Clock()

    # Fontes para texto
    fonte_hud = pygame.font.SysFont(None, 26)
    fonte_grande = pygame.font.SysFont(None, 64)
    fonte_pequena = pygame.font.SysFont(None, 36)

    # Carrega o mapa e obtém os elementos necessários
    paredes = obter_paredes()
    saida = obter_saida()
    pos_inicial = obter_posicao_inicial()

    # Cria o jogador na posição inicial
    jogador = Jogador(pos_inicial[0], pos_inicial[1])

    # Marca o tempo de início
    tempo_inicio = time.time()

    # Variável de controle do loop
    rodando = True

    # ---- LOOP PRINCIPAL ----
    while rodando:

        # 1. Processar eventos (fechar janela, tecla ESC)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        # 2. Atualizar estado do jogo
        processar_movimento(jogador, paredes)

        # Calcula o tempo decorrido
        tempo_decorrido = time.time() - tempo_inicio

        # Verifica se o jogador chegou na saída
        if jogador.chegou_na_saida(saida):
            rodando = False
            tela_vitoria(tela, fonte_grande, fonte_pequena, tempo_decorrido)
            break

        # 3. Desenhar na tela
        tela.fill(COR_FUNDO)        # limpa a tela
        desenhar_mapa(tela)          # desenha o labirinto
        jogador.desenhar(tela)       # desenha o jogador
        desenhar_hud(tela, fonte_hud, tempo_decorrido)  # desenha HUD

        # 4. Atualiza a janela com o que foi desenhado
        pygame.display.flip()

        # 5. Controla a velocidade (FPS)
        relogio.tick(FPS)

    # Encerra o Pygame ao sair do loop
    pygame.quit()
