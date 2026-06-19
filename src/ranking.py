import os

CAMINHO_RANKING = "ranking.txt"


def carregar_ranking():
    ranking = []

    if os.path.exists(CAMINHO_RANKING):
        with open(CAMINHO_RANKING, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, tempo = linha.strip().split(";")
                ranking.append((nome, float(tempo)))

    ranking.sort(key=lambda x: x[1])

    return ranking


def salvar_tempo(nome, tempo):
    ranking = carregar_ranking()

    ranking.append((nome, tempo))

    ranking.sort(key=lambda x: x[1])

    ranking = ranking[:5]

    with open(CAMINHO_RANKING, "w", encoding="utf-8") as arquivo:
        for nome, tempo in ranking:
            arquivo.write(f"{nome};{tempo}\n")