import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

st.header("1. HSV")
col1, col2 = st.columns(2)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
col1.image(img, caption="img")

so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255
rgb = cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB)
col2.image(rgb, caption="H")

st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

fator = col1.slider("Brilho", 0.0, 2.0, 1.5)
v = hsv[:, :, 2].astype(float)
v = v * fator
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

giro = col2.slider("Graus", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
girada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
col2.image(girada)

