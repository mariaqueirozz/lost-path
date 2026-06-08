import pygame
from src.config import TAMANHO_CELULA, COR_PAREDE, COR_CORREDOR, COR_SAIDA

LABIRINTO = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def obter_posicao_inicial():
    return (1 * TAMANHO_CELULA, 1 * TAMANHO_CELULA)


def obter_paredes():
    paredes = []
    for linha in range(len(LABIRINTO)):
        for coluna in range(len(LABIRINTO[linha])):
            if LABIRINTO[linha][coluna] == 1:
                rect = pygame.Rect(
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                )
                paredes.append(rect)
    return paredes


def obter_saida():
    for linha in range(len(LABIRINTO)):
        for coluna in range(len(LABIRINTO[linha])):
            if LABIRINTO[linha][coluna] == 2:
                return pygame.Rect(
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                )
    return None


def desenhar_mapa(tela):
    for linha in range(len(LABIRINTO)):
        for coluna in range(len(LABIRINTO[linha])):
            x = coluna * TAMANHO_CELULA
            y = linha * TAMANHO_CELULA
            rect = pygame.Rect(x, y, TAMANHO_CELULA, TAMANHO_CELULA)

            if LABIRINTO[linha][coluna] == 1:
                pygame.draw.rect(tela, COR_PAREDE, rect)
            elif LABIRINTO[linha][coluna] == 2:
                pygame.draw.rect(tela, COR_SAIDA, rect)
                fonte = pygame.font.SysFont(None, 28)
                texto = fonte.render("S", True, (0, 0, 0))
                tela.blit(texto, (x + 12, y + 10))
            else:
                pygame.draw.rect(tela, COR_CORREDOR, rect)
