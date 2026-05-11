import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("AI OCR")

@st.cache_resource
def load_reader():
    return easyocr.Reader(['ja', 'en'])

reader = load_reader()

uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="アップロード画像")

    img = np.array(image)

    with st.spinner("OCR実行中..."):

        result = reader.readtext(img)

    text = ""

    for r in result:
        text += r[1] + "\n"

    st.subheader("OCR結果")

    st.text_area(
        "",
        text,
        height=300
    )