import numpy as np
import streamlit as st


def criar_bandeira():
    verde = (0, 156, 59)
    amarelo = (255, 223, 0)
    azul = (0, 39, 118)
    branco = (255, 255, 255)

    bandeira = np.zeros((140, 200, 3), dtype=np.uint8)
    bandeira[:] = verde
    linhas, colunas = np.indices(bandeira.shape[:2])
    x = colunas - 100
    y = linhas - 70

    losango = np.abs(x) / 83 + np.abs(y) / 53 <= 1
    bandeira[losango] = amarelo

    circulo = x**2 + y**2 <= 35**2
    bandeira[circulo] = azul

    centro_faixa = 58 + 0.32 * x + 0.003 * x**2
    faixa = circulo & (np.abs(linhas - centro_faixa) <= 4)
    bandeira[faixa] = branco

    estrelas = [
        (46, 110, 1),
        (64, 73, 1), (70, 79, 1), (76, 71, 1), (82, 77, 1),
        (87, 83, 1), (80, 88, 1), (74, 86, 1), (72, 94, 1),
        (81, 99, 2), (91, 99, 1), (86, 94, 1), (86, 104, 1),
        (96, 102, 1), (101, 100, 1),
        (76, 109, 1), (81, 114, 1), (87, 110, 1), (94, 111, 1),
        (84, 121, 1), (91, 119, 1), (88, 126, 1),
        (95, 92, 1), (99, 87, 1), (103, 94, 1),
        (98, 107, 1), (75, 119, 1),
    ]
    for linha, coluna, raio in estrelas:
        estrela = np.abs(linhas - linha) + np.abs(colunas - coluna) <= raio
        bandeira[estrela & circulo & ~faixa] = branco

    return bandeira


st.title("Bandeira do Brasil")
st.write("Atividade 2 — bandeira")

bandeira = criar_bandeira()
st.image(bandeira, width=600)

