from paddleocr import PaddleOCR
import streamlit as st
from PIL import Image
import numpy as np

st.title("OCR App")

@st.cache_resource
def load_ocr():
    return PaddleOCR(
        use_angle_cls=True,
        lang='japanese'
    )

ocr = load_ocr()

uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image)

    img = np.array(image)

    result = ocr.ocr(img)

    text = ""

    for line in result[0]:
        text += line[1][0] + "\n"

    st.text_area("OCR結果", text, height=300)