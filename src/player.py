import pygame
from src.config import TAMANHO_CELULA, COR_JOGADOR, VELOCIDADE_JOGADOR


class Jogador:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tamanho = TAMANHO_CELULA - 8
        self.rect = pygame.Rect(self.x + 4, self.y + 4, self.tamanho, self.tamanho)

    def mover(self, dx, dy, paredes):
        self.rect.x += dx
        if self._colidiu_com_parede(paredes):
            self.rect.x -= dx

        # Move no eixo Y
        self.rect.y += dy
        if self._colidiu_com_parede(paredes):
            self.rect.y -= dy

    def _colidiu_com_parede(self, paredes):
        for parede in paredes:
            if self.rect.colliderect(parede):
                return True
        return False

    def chegou_na_saida(self, saida):
        return self.rect.colliderect(saida)

    def desenhar(self, tela):
        centro_x = self.rect.x + self.tamanho // 2
        centro_y = self.rect.y + self.tamanho // 2
        raio = self.tamanho // 2
        pygame.draw.circle(tela, COR_JOGADOR, (centro_x, centro_y), raio)
        pygame.draw.circle(tela, (0, 100, 0), (centro_x, centro_y), raio, 2)


def processar_movimento(jogador, paredes):
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
