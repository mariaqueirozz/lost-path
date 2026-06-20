import pygame
import random
from src.config import TAMANHO_CELULA, COR_PAREDE, COR_CORREDOR, COR_SAIDA

LABIRINTO = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 4, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

CHAVES = [
    (1, 13, 3),
    (13, 1, 4),
]
 
COR_PORTA = {
    3: (220, 50,  50),  
    4: (50,  100, 220),  
}
 
COR_CHAVE = {
    3: (255, 100, 100),
    4: (100, 160, 255),
}


random.seed(42)
_ESTRELAS = []
for _l in range(len(LABIRINTO)):
    for _c in range(len(LABIRINTO[_l])):
        if LABIRINTO[_l][_c] == 1:
            _x0 = _c * TAMANHO_CELULA
            _y0 = _l * TAMANHO_CELULA
            for _ in range(random.randint(1, 3)):
                sx = _x0 + random.randint(3, TAMANHO_CELULA - 3)
                sy = _y0 + random.randint(3, TAMANHO_CELULA - 3)
                b = random.randint(100, 200)
                _ESTRELAS.append((sx, sy, b))


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

def obter_portas():
    """Retorna lista de (rect, cor_id) para cada porta no mapa."""
    portas = []
    for linha in range(len(LABIRINTO)):
        for coluna in range(len(LABIRINTO[linha])):
            cel = LABIRINTO[linha][coluna]
            if cel in (3, 4):
                rect = pygame.Rect(
                    coluna * TAMANHO_CELULA + TAMANHO_CELULA // 4,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA // 2,
                    TAMANHO_CELULA
                )
                portas.append((rect, cel, linha, coluna))
    return portas
 
 
def abrir_porta(linha, coluna, paredes_lista):
    """Remove a porta do labirinto e da lista de paredes."""
    LABIRINTO[linha][coluna] = 0
    nova_lista = [
        p for p in paredes_lista
        if not (p.x == coluna * TAMANHO_CELULA and p.y == linha * TAMANHO_CELULA)
    ]
    return nova_lista
 
 
def obter_chaves():
    """Retorna lista de (rect, cor_id) de cada chave."""
    resultado = []
    for (l, c, cor_id) in CHAVES:
        rect = pygame.Rect(
            c * TAMANHO_CELULA + TAMANHO_CELULA // 4,
            l * TAMANHO_CELULA + TAMANHO_CELULA // 4,
            TAMANHO_CELULA // 2,
            TAMANHO_CELULA // 2,
        )
        resultado.append((rect, cor_id, l, c))
    return resultado
 
 
def desenhar_chave(tela, x, y, cor_id):
    """Desenha uma chavinha no corredor."""
    cor = COR_CHAVE[cor_id]
    cx = x + TAMANHO_CELULA // 2
    cy = y + TAMANHO_CELULA // 2
    r = 6
 
    pygame.draw.circle(tela, cor, (cx, cy - 4), r, 2)
 
    pygame.draw.line(tela, cor, (cx, cy + 2), (cx, cy + 10), 2)
    pygame.draw.line(tela, cor, (cx, cy + 6), (cx + 3, cy + 6), 2)
    pygame.draw.line(tela, cor, (cx, cy + 9), (cx + 3, cy + 9), 2)
 
 
def desenhar_porta(tela, x, y, cor_id):
    """Desenha uma portinha colorida na parede."""
    cor = COR_PORTA[cor_id]
    t = TAMANHO_CELULA
    rect = pygame.Rect(x, y, t, t)
 
    pygame.draw.rect(tela, COR_PAREDE, rect)
 
    porta_rect = pygame.Rect(x + 4, y + 6, t - 8, t - 6)
    pygame.draw.rect(tela, cor, porta_rect)
 
    pygame.draw.rect(tela, (255, 255, 255), porta_rect, 2)
 
    pygame.draw.circle(tela, (255, 220, 50), (x + t - 10, y + t // 2), 3)
 
    pygame.draw.line(tela, (80, 100, 180), (x, y), (x + t - 1, y), 2)
    pygame.draw.line(tela, (80, 100, 180), (x, y), (x, y + t - 1), 2)
    pygame.draw.line(tela, (10, 10, 30), (x, y + t - 1), (x + t - 1, y + t - 1), 2)
    pygame.draw.line(tela, (10, 10, 30), (x + t - 1, y), (x + t - 1, y + t - 1), 2)



def desenhar_mapa(tela, chaves_restantes=None):
    if chaves_restantes is None:
        chaves_restantes = []
 
    for linha in range(len(LABIRINTO)):
        for coluna in range(len(LABIRINTO[linha])):
            x = coluna * TAMANHO_CELULA
            y = linha * TAMANHO_CELULA
            rect = pygame.Rect(x, y, TAMANHO_CELULA, TAMANHO_CELULA)
            t = TAMANHO_CELULA
            cel = LABIRINTO[linha][coluna]
 
            if cel == 1:
                pygame.draw.rect(tela, COR_PAREDE, rect)
                pygame.draw.line(tela, (80, 100, 180), (x, y), (x + t - 1, y), 2)
                pygame.draw.line(tela, (80, 100, 180), (x, y), (x, y + t - 1), 2)
                pygame.draw.line(tela, (10, 10, 30), (x, y + t - 1), (x + t - 1, y + t - 1), 2)
                pygame.draw.line(tela, (10, 10, 30), (x + t - 1, y), (x + t - 1, y + t - 1), 2)
 
            elif cel in (3, 4):  
                desenhar_porta(tela, x, y, cel)
 
            elif cel == 2:
                pygame.draw.rect(tela, COR_SAIDA, rect)
                pygame.draw.rect(tela, (255, 255, 255), rect, 3)
 
                fonte = pygame.font.SysFont(None, 30)
                texto = fonte.render("S", True, (0, 0, 0))
                texto_x = x + (TAMANHO_CELULA - texto.get_width()) // 2
                texto_y = y + (TAMANHO_CELULA - texto.get_height()) // 2
                tela.blit(texto, (texto_x, texto_y))
 
            else:
                pygame.draw.rect(tela, COR_CORREDOR, rect)
 
    for (sx, sy, b) in _ESTRELAS:
        tela.set_at((sx, sy), (b, b, min(255, b + 40)))
 
    for (_, cor_id, l, c) in chaves_restantes:
        desenhar_chave(tela, c * TAMANHO_CELULA, l * TAMANHO_CELULA, cor_id)
 
