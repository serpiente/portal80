import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")

st.title("Analisis precios de escritura")
st.title("Centro Comercial Portal 80")

# Load images
images = {
    "Piso 3": Image.open('./piso3.jpeg'),
    "Piso 2": Image.open('./piso2.jpg'),
    "Piso 1": Image.open('./piso1.jpg'),
}

# Dropdown to select an image
option = st.selectbox(
    'Selecione un piso',
    list(images.keys())
)

# Display the selected image

# Display the image with a title

st.image(images[option])

piso = 3
df = pd.read_csv("./enriched.csv")
match option:
    case "Piso 3":
        piso = 3
    case "Piso 2":
        piso = 2
    case "Piso 1":
        piso = 1

filtered = df[df.piso == piso]
st.dataframe(filtered, hide_index=True)
