import pygame
import time
from src.config import (
    LARGURA_TELA, ALTURA_TELA, TITULO, FPS,
    COR_FUNDO, COR_TEXTO, COR_TEMPO
)
from src.mapa import desenhar_mapa, obter_paredes, obter_saida, obter_posicao_inicial
from src.player import Jogador, processar_movimento


def desenhar_hud(tela, fonte, tempo_decorrido):
    minutos = int(tempo_decorrido) // 60
    segundos = int(tempo_decorrido) % 60
    texto_tempo = fonte.render(f"Tempo: {minutos:02d}:{segundos:02d}", True, COR_TEMPO)
    tela.blit(texto_tempo, (10, 10))

    texto_dica = fonte.render("WASD ou setas para mover | ESC sair", True, COR_TEXTO)
    tela.blit(texto_dica, (LARGURA_TELA - texto_dica.get_width() - 10, 10))


def tela_vitoria(tela, fonte_grande, fonte_pequena, tempo_decorrido):
    tela.fill((20, 20, 20))

    texto_vitoria = fonte_grande.render("VOCÊ VENCEU!", True, (255, 215, 0))
    x = LARGURA_TELA // 2 - texto_vitoria.get_width() // 2
    tela.blit(texto_vitoria, (x, 200))

    minutos = int(tempo_decorrido) // 60
    segundos = int(tempo_decorrido) % 60
    texto_tempo = fonte_pequena.render(f"Seu tempo: {minutos:02d}:{segundos:02d}", True, COR_TEXTO)
    x_tempo = LARGURA_TELA // 2 - texto_tempo.get_width() // 2
    tela.blit(texto_tempo, (x_tempo, 300))

    texto_sair = fonte_pequena.render("Pressione qualquer tecla para sair", True, (180, 180, 180))
    x_sair = LARGURA_TELA // 2 - texto_sair.get_width() // 2
    tela.blit(texto_sair, (x_sair, 380))

    pygame.display.flip()

    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                aguardando = False
            if evento.type == pygame.KEYDOWN:
                aguardando = False


def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO)

    relogio = pygame.time.Clock()

    fonte_hud = pygame.font.SysFont(None, 26)
    fonte_grande = pygame.font.SysFont(None, 64)
    fonte_pequena = pygame.font.SysFont(None, 36)

    paredes = obter_paredes()
    saida = obter_saida()
    pos_inicial = obter_posicao_inicial()

    jogador = Jogador(pos_inicial[0], pos_inicial[1])

    tempo_inicio = time.time()

    rodando = True

    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        processar_movimento(jogador, paredes)

        tempo_decorrido = time.time() - tempo_inicio

        if jogador.chegou_na_saida(saida):
            rodando = False
            tela_vitoria(tela, fonte_grande, fonte_pequena, tempo_decorrido)
            break

        tela.fill(COR_FUNDO)
        desenhar_mapa(tela)
        jogador.desenhar(tela)
        desenhar_hud(tela, fonte_hud, tempo_decorrido)

        pygame.display.flip()

        relogio.tick(FPS)

    pygame.quit()
