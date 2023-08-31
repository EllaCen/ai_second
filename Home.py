import streamlit as st

import _util
import SEO_prompt_course as functions


# api輸入
def api_key_input():
    st.title("💭 api 輸入")
    st.info("輸入您的 api key，我們將為連結 ChatGPT")
    api_key = st.text_input('請輸入 openai api key')
    return api_key


def api_key_input_button_result(api_key):
    st.write('連接成功')
    st.session_state.api_key = api_key


def main():
    _util.background()
    
    global text_spinner_placeholder_1,text_spinner_placeholder_2,text_spinner_placeholder_3,text_spinner_placeholder_4
    text_spinner_placeholder_1 = st.empty()
    text_spinner_placeholder_2 = st.empty()
    text_spinner_placeholder_3 = st.empty()
    text_spinner_placeholder_4 = st.empty()

    api_key = api_key_input()
    if st.button("測試 api key"):
        with st.spinner('連接 api 中...'):
            result = functions.test(api_key)
            api_key_input_button_result(api_key)


if __name__ == '__main__':
    main()
