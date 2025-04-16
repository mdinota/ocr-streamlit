import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="Streamlit", layout="wide")
st.title("Streamlit OCR App")

column_1, column_2, column_3 = st.columns(3)

with column_1:
    st.subheader("📷 Subir")
    st.write("Subí una imagen de un texto para extraerlo.")
    uploaded_file = st.file_uploader("Subí una imagen", type=["png", "jpg", "jpeg"])

image = None
if uploaded_file:
    image = Image.open(uploaded_file)

with column_2:
    st.subheader("🖼️ Imagen")
    if image:
        st.image(image, caption="Imagen subida")

with column_3:
    st.subheader("📄 Texto detectado")
    if image:
        with st.spinner("Analizando imagen..."):
            texto = pytesseract.image_to_string(image)

        st.text_area("Resultado", value=texto, height=300)
