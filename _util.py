import base64
import io

import streamlit as st
from PIL import Image


def background():
    # 頁面設計 - 此處不須更動
    PAGE_CONFIG = {'page_title':'SEO文案撰寫工具',
                    'page_icon':'📝','layout':'centered',
                    'initial_sidebar_state':'auto'}
    st.set_page_config(**PAGE_CONFIG)

    # 讀取TMDS圖片
    image_path = "/Users/ranli/Documents/python_ve/TMR_python_02/SEO_copywriting_course/TMDS-LOGO.png"
    image = Image.open(image_path)

    # 將TMDS圖片轉換為base64編碼的字串
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # 隱藏 Made With Streamlit
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # 在右上角顯示 TMDS LOGO
    st.markdown(
        f'''
		<style>
		.stApp {{
        background-image: url("data:image/png;base64,{image_base64}");
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: top right;
        background-size: 15% 35%;
		}}
		</style>
		''',
        unsafe_allow_html=True,
    )
