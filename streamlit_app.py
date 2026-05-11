import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

st.title("PaddleOCR Web")

@st.cache_resource
def load_ocr():
    return PaddleOCR(
        use_angle_cls=False,
        lang='japan',
        show_log=False
    )

ocr = load_ocr()

uploaded_file = st.file_uploader(
    "画像アップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    image.thumbnail((1200, 1200))

    st.image(image)

    img_array = np.array(image)

    with st.spinner("OCR中..."):
        result = ocr.ocr(img_array)

    texts = []

    if result and result[0]:
        for line in result[0]:
            texts.append(line[1][0])

    st.text_area(
        "OCR結果",
        "\n".join(texts),
        height=300
    )