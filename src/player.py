# player.py
# Controla o personagem principal do jogo

import pygame
from src.config import TAMANHO_CELULA, COR_JOGADOR, VELOCIDADE_JOGADOR


class Jogador:
    """Representa o personagem controlado pelo jogador."""

    def __init__(self, x, y):
        # Posição inicial (em pixels)
        self.x = x
        self.y = y
        # Tamanho do personagem (um pouco menor que a célula para caber nos corredores)
        self.tamanho = TAMANHO_CELULA - 8
        # Retângulo de colisão do jogador
        self.rect = pygame.Rect(self.x + 4, self.y + 4, self.tamanho, self.tamanho)

    def mover(self, dx, dy, paredes):
        """
        Move o jogador na direção (dx, dy) e verifica colisão com as paredes.
        Se houver colisão, o movimento é desfeito.
        """
        # Move no eixo X
        self.rect.x += dx
        if self._colidiu_com_parede(paredes):
            self.rect.x -= dx  # desfaz o movimento

        # Move no eixo Y
        self.rect.y += dy
        if self._colidiu_com_parede(paredes):
            self.rect.y -= dy  # desfaz o movimento

    def _colidiu_com_parede(self, paredes):
        """Verifica se o rect do jogador está colidindo com alguma parede."""
        for parede in paredes:
            if self.rect.colliderect(parede):
                return True
        return False

    def chegou_na_saida(self, saida):
        """Verifica se o jogador tocou na célula de saída."""
        return self.rect.colliderect(saida)

    def desenhar(self, tela):
        """Desenha o jogador como um círculo verde na tela."""
        centro_x = self.rect.x + self.tamanho // 2
        centro_y = self.rect.y + self.tamanho // 2
        raio = self.tamanho // 2
        pygame.draw.circle(tela, COR_JOGADOR, (centro_x, centro_y), raio)
        # Contorno escuro para destacar
        pygame.draw.circle(tela, (0, 100, 0), (centro_x, centro_y), raio, 2)


def processar_movimento(jogador, paredes):
    """
    Lê as teclas pressionadas e move o jogador.
    Aceita tanto WASD quanto as setas do teclado.
    """
    teclas = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        dy = -VELOCIDADE_JOGADOR
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        dy = VELOCIDADE_JOGADOR
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        dx = -VELOCIDADE_JOGADOR
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        dx = VELOCIDADE_JOGADOR

    jogador.mover(dx, dy, paredes)
