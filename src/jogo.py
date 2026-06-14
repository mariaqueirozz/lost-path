import pygame
import time
from src.config import (
    LARGURA_TELA, ALTURA_TELA, TITULO, FPS,
    COR_FUNDO, COR_TEXTO, COR_TEMPO
)
from src.mapa import (desenhar_mapa, obter_paredes, obter_saida, obter_posicao_inicial, obter_portas, obter_chaves, abrir_porta, COR_CHAVE)
from src.player import Jogador, processar_movimento
 
TEMPO_MAXIMO = 60 


def desenhar_hud(tela, fonte, tempo_decorrido, chaves_coletadas):

    tempo_restante = max(0, TEMPO_MAXIMO - int(tempo_decorrido))

    minutos = tempo_restante // 60
    segundos = tempo_restante % 60

    texto_tempo = fonte.render(
        f"Tempo restante: {minutos:02d}:{segundos:02d}",
        True,
        COR_TEMPO
    )

    tela.blit(texto_tempo, (10, 10))

    texto_dica = fonte.render(
        "Objetivo: encontre a saida | WASD/Setas | ESC",
        True,
        COR_TEXTO
    )

    tela.blit(
        texto_dica,
        (LARGURA_TELA - texto_dica.get_width() - 10, 10)
    )

    for i, cor_id in enumerate(chaves_coletadas):
        cor = COR_CHAVE[cor_id]
        pygame.draw.circle(tela, cor, (15 + i * 20, 35), 6)
        pygame.draw.circle(tela, (255, 255, 255), (15 + i * 20, 35), 6, 1)


def desenhar_aviso(tela, fonte, mensagem):
    surf = pygame.Surface((360, 40), pygame.SRCALPHA)
    surf.fill((0, 0, 0, 160))
    tela.blit(surf, (LARGURA_TELA // 2 - 180, ALTURA_TELA // 2 - 20))
    texto = fonte.render(mensagem, True, (255, 80, 80))
    tela.blit(texto, (LARGURA_TELA // 2 - texto.get_width() // 2, ALTURA_TELA // 2 - texto.get_height() // 2))



def tela_vitoria(tela, fonte_grande, fonte_pequena, tempo_decorrido):
    tela.fill((20, 20, 20))

    texto_vitoria = fonte_grande.render("VOCE ESCAPOU!", True, (255, 215, 0))
    x = LARGURA_TELA // 2 - texto_vitoria.get_width() // 2
    tela.blit(texto_vitoria, (x, 200))

    minutos = int(tempo_decorrido) // 60
    segundos = int(tempo_decorrido) % 60
    texto_tempo = fonte_pequena.render(f"Tempo final: {minutos:02d}:{segundos:02d}", True, COR_TEXTO)
    x_tempo = LARGURA_TELA // 2 - texto_tempo.get_width() // 2
    tela.blit(texto_tempo, (x_tempo, 300))
    
    texto_parabens = fonte_pequena.render("Parabens! Voce encontrou a saida do labirinto.", True, COR_TEXTO)

    x_parabens = LARGURA_TELA // 2 - texto_parabens.get_width() // 2
    tela.blit(texto_parabens, (x_parabens, 340))

    texto_sair = fonte_pequena.render("Pressione qualquer tecla para encerrar", True, (180,180,180))
    x_sair = LARGURA_TELA // 2 - texto_sair.get_width() // 2
    tela.blit(texto_sair, (x_sair, 380))

    pygame.display.flip()

    aguardando = True

    while aguardando:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_r:
                    return True

                if evento.key == pygame.K_ESCAPE:
                    return False

def tela_derrota(tela, fonte_grande, fonte_pequena):
    tela.fill((20, 20, 20))

    texto = fonte_grande.render("TEMPO ESGOTADO!", True, (255, 0, 0))
    x = LARGURA_TELA // 2 - texto.get_width() // 2
    tela.blit(texto, (x, 220))

    texto2 = fonte_pequena.render(
        "Pressione qualquer tecla para encerrar",
        True,
        (180, 180, 180)
    )

    x2 = LARGURA_TELA // 2 - texto2.get_width() // 2
    tela.blit(texto2, (x2, 320))

    texto3 = fonte_pequena.render("Voce nao conseguiu escapar a tempo.", True, COR_TEXTO)

    x3 = LARGURA_TELA // 2 - texto3.get_width() // 2
    tela.blit(texto3, (x3, 290))

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_r:
                    return True

                if evento.key == pygame.K_ESCAPE:
                    return False

def tela_pausa(tela, fonte_grande, fonte_pequena):

    tela.fill((20, 20, 20))

    titulo = fonte_grande.render("JOGO PAUSADO", True, (255, 255, 0))
    tela.blit(
        titulo,
        (
            LARGURA_TELA // 2 - titulo.get_width() // 2,
            220
        )
    )

    texto = fonte_pequena.render(
        "Pressione P para continuar",
        True,
        COR_TEXTO
    )

    tela.blit(
        texto,
        (
            LARGURA_TELA // 2 - texto.get_width() // 2,
            320
        )
    )

    pygame.display.flip()

    tempo_pausa = time.time()

    while True:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return None

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_p:
                    return time.time() - tempo_pausa
                

def tela_inicial(tela, fonte_grande, fonte_pequena):
    tela.fill((20, 20, 20))

    titulo = fonte_grande.render("LOST PATH", True, (255, 215, 0))
    x = LARGURA_TELA // 2 - titulo.get_width() // 2
    tela.blit(titulo, (x, 180))

    texto = fonte_pequena.render("Pressione ENTER para iniciar", True, COR_TEXTO)
    x2 = LARGURA_TELA // 2 - texto.get_width() // 2
    tela.blit(texto, (x2, 300))

    texto2 = fonte_pequena.render("ESC para sair", True, COR_TEXTO)
    x3 = LARGURA_TELA // 2 - texto2.get_width() // 2
    tela.blit(texto2, (x3, 350))

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:
                    return True

                if evento.key == pygame.K_ESCAPE:
                    return False
                

def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Lost Path - Escape do Labirinto")

    relogio = pygame.time.Clock()

    fonte_hud = pygame.font.SysFont(None, 26)
    fonte_grande = pygame.font.SysFont(None, 64)
    fonte_pequena = pygame.font.SysFont(None, 36)
    
    if not tela_inicial(tela, fonte_grande, fonte_pequena):
        pygame.quit()
        return

    paredes = obter_paredes()
    saida = obter_saida()
    pos_inicial = obter_posicao_inicial()
    portas = obter_portas()        
    chaves = obter_chaves()

    jogador = Jogador(pos_inicial[0], pos_inicial[1])

    chaves_coletadas = []   
    aviso_texto = ""
    aviso_timer = 0

    tempo_inicio = time.time()

    rodando = True

    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                if evento.key == pygame.K_p:

                    tempo_parado = tela_pausa(
                        tela,
                        fonte_grande,
                        fonte_pequena
                    )

                    if tempo_parado is None:
                        rodando = False
                    else:
                        tempo_inicio += tempo_parado


        processar_movimento(jogador, paredes)

        for chave in chaves[:]:
            (rect, cor_id, l, c) = chave
            if jogador.rect.colliderect(rect):
                chaves_coletadas.append(cor_id)
                chaves.remove(chave)

        for porta in portas[:]:
            (rect, cor_id, linha, coluna) = porta
            area_porta = rect.inflate(4, 4)
            if jogador.rect.colliderect(area_porta):
                if cor_id in chaves_coletadas:
                    chaves_coletadas.remove(cor_id)
                    portas.remove(porta)
                    paredes = abrir_porta(linha, coluna, paredes)
                else:
                    nome_cor = "vermelha" if cor_id == 3 else "azul"
                    aviso_texto = f"Precisa da chave {nome_cor}!"
                    aviso_timer = 90

        tempo_decorrido = time.time() - tempo_inicio

        if tempo_decorrido >= TEMPO_MAXIMO:
            tela_derrota(tela, fonte_grande, fonte_pequena)
            break

        if jogador.chegou_na_saida(saida):
            rodando = False
            tela_vitoria(tela, fonte_grande, fonte_pequena, tempo_decorrido)
            break

        tela.fill(COR_FUNDO)
        desenhar_mapa(tela, chaves)
        jogador.desenhar(tela)
        desenhar_hud(tela, fonte_hud, tempo_decorrido, chaves_coletadas)

        if aviso_timer > 0:
            desenhar_aviso(tela, fonte_hud, aviso_texto)
            aviso_timer -= 1

        pygame.display.flip()

        relogio.tick(FPS)

    pygame.quit()
