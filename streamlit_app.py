import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

st.title("AI OCR アプリ")

# OCRモデル読み込み
@st.cache_resource
def load_ocr():
    return PaddleOCR(
        use_angle_cls=True,
        lang='japan'
    )

ocr = load_ocr()

# 画像アップロード
uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="アップロード画像")

    img_array = np.array(image)

    with st.spinner("OCR実行中..."):

        result = ocr.ocr(img_array)

    extracted_text = ""

    for line in result[0]:
        text = line[1][0]
        extracted_text += text + "\n"

    st.subheader("認識結果")

    st.text_area(
        "",
        extracted_text,
        height=300
    )