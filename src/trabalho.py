import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

st.header("1. Saturação")
col1, col2 = st.columns(2)
fator = col2.slider("Saturação", 0.0, 2.0, 1.0)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
saturada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
col1.image(img, caption="Foto original")
col2.image(saturada, caption="Saturação ajustada")

st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
peso_r = col2.slider("Peso R", 0.01, 1.0, 0.30)
peso_g = col2.slider("Peso G", 0.01, 1.0, 0.59)
peso_b = col2.slider("Peso B", 0.01, 1.0, 0.11)
ponderada = ((r * peso_r + g * peso_g + b * peso_b) / (peso_r + peso_g + peso_b)).astype(np.uint8)
col1.image(media, caption="Média dos canais")
col2.image(ponderada, caption="Média ponderada")

st.header("5. Canais")
col1, col2 = st.columns(2)
canal = col2.slider("Canal escolhido: 0=R, 1=G, 2=B", 0, 2, 0)
so_canal = np.zeros(img.shape, dtype=np.uint8)
so_canal[:, :, canal] = img[:, :, canal]
col1.image(img[:, :, 0], caption="Canal R em cinza")
col1.image(img[:, :, 1], caption="Canal G em cinza")
col1.image(img[:, :, 2], caption="Canal B em cinza")
col2.image(so_canal, caption="Canal escolhido em sua cor")

st.header("9. Recorte")
col1, col2 = st.columns(2)
altura, largura = img.shape[0], img.shape[1]
limite = int(np.clip(altura, 1, largura))
t = col2.slider("Tamanho do quadrado", 1, limite, limite // 3)
y = col2.slider("Linha inicial", 0, altura - t, (altura - t) // 4)
x = col2.slider("Coluna inicial", 0, largura - t, (largura - t) // 4)
recorte = img[y:y + t, x:x + t]
col1.image(img, caption="Foto original")
col2.image(recorte, caption="Quadrado recortado")

st.header("13. Máscara de cor")
col1, col2 = st.columns(2)
h_min, h_max = col1.slider("Faixa de H", 0, 179, (140, 179))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
so_cor = img.copy()
fora = mascara == 0
so_cor[fora] = 0
col1.image(mascara, caption="Máscara (branco = selecionado)")
col2.image(so_cor, caption="Somente a cor escolhida")