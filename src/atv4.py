import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

img = np.array(Image.open("imagens/foto.jpg").convert("RGB"))

st.header("Leitura da foto")
col1, col2 = st.columns(2)

col1.image(img, caption="Fotografia original em RGB")
col2.text(f"Dimensões (altura, largura, canais): {img.shape}")
col2.text(f"Pixel img[100, 100] em RGB: {img[100, 100]}")

st.header("Canais")
col1, col2, col3 = st.columns(3)

col1.image(img[:, :, 0], caption="R em tons de cinza")
col2.image(img[:, :, 1], caption="G em tons de cinza")
col3.image(img[:, :, 2], caption="B em tons de cinza")

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col1.image(so_r, caption="Só R")

so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0
col2.image(so_g, caption="Só G")

so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0
col3.image(so_b, caption="Só B")

st.header("Cubo e BGR")
col1, col2 = st.columns(2)

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="Amarelo")

quadrado[:, :] = (255, 0, 0)
col1.image(quadrado, caption="Vermelho")

quadrado[:, :] = (0, 255, 0)
col1.image(quadrado, caption="Verde")

quadrado[:, :] = (0, 0, 255)
col1.image(quadrado, caption="Azul")

col2.image(img, channels="BGR", caption="Fotografia interpretada como BGR")

st.header("Tons de cinza")
col1, col2 = st.columns(2)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="Média")

ponderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col2.image(ponderada, caption="Média ponderada")