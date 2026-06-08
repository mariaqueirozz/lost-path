# tests/test_mapa.py
# Testes simples para as funções de lógica do jogo Lost Path
#
# Para executar: python -m pytest
# (na pasta raiz do projeto)

import sys
import os

# Garante que a pasta raiz do projeto está no caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pygame
pygame.init()  # necessário para usar pygame.Rect nos testes

from src.mapa import LABIRINTO, obter_posicao_inicial, obter_paredes, obter_saida
from src.config import TAMANHO_CELULA


def test_labirinto_e_uma_lista():
    """Verifica que o labirinto é uma lista (estrutura de dados correta)."""
    assert isinstance(LABIRINTO, list)


def test_labirinto_tem_linhas():
    """Verifica que o labirinto tem pelo menos uma linha."""
    assert len(LABIRINTO) > 0


def test_labirinto_tem_saida():
    """Verifica que existe pelo menos uma célula de saída (valor 2) no labirinto."""
    saida_encontrada = False
    for linha in LABIRINTO:
        if 2 in linha:
            saida_encontrada = True
            break
    assert saida_encontrada, "O labirinto precisa ter uma saída (valor 2)"


def test_posicao_inicial_e_corredor():
    """Verifica que a posição inicial do jogador é um corredor (não é parede)."""
    pos_x, pos_y = obter_posicao_inicial()
    coluna = pos_x // TAMANHO_CELULA
    linha = pos_y // TAMANHO_CELULA
    assert LABIRINTO[linha][coluna] == 0, "A posição inicial deve ser um corredor (0)"


def test_obter_paredes_retorna_lista():
    """Verifica que obter_paredes() retorna uma lista."""
    paredes = obter_paredes()
    assert isinstance(paredes, list)


def test_obter_paredes_nao_vazia():
    """Verifica que existem paredes no labirinto."""
    paredes = obter_paredes()
    assert len(paredes) > 0, "O labirinto deve ter paredes"


def test_obter_saida_nao_e_none():
    """Verifica que a função obter_saida() retorna um objeto válido."""
    saida = obter_saida()
    assert saida is not None, "A saída não deve ser None"


def test_saida_e_um_rect():
    """Verifica que a saída retornada é um pygame.Rect."""
    saida = obter_saida()
    assert isinstance(saida, pygame.Rect)
