import streamlit as st
import time

import streamlit_crawler_Ella_addlink
import _util
import SEO_prompt_course


#關鍵字用 使步驟可連續
if "keyword_button" not in st.session_state:
    st.session_state.keyword_button = False
if 'keyword_tweet' not in st.session_state:
    st.session_state.keyword_tweet = ""
if 'keyword_text_error' not in st.session_state:
    st.session_state.keyword_text_error = ""
if "keyword_n_requests" not in st.session_state:
    st.session_state.keyword_n_requests = 0


def keyword_function(word , api_key):

        if st.session_state.keyword_n_requests >= 5:
            st.session_state.keyword_text_error = "按太多次了，請等待約5秒再點擊"
            st.session_state.keyword_n_requests = 1
            return
        
        if not word:
            st.warning("請輸入搜尋字詞")
            return

        with text_spinner_placeholder_1:
            with st.spinner("SEO關鍵字生成中..."):
                # time.sleep(5)
                crawler,link = streamlit_crawler_Ella_addlink.run_crawler(word)
                crawler_keyword=SEO_prompt_course.SEO_crawler_keyword(api_key,crawler)
                
                st.session_state.keyword_tweet = (crawler_keyword)
                st.session_state.link_tweet = (link)


def main():
    _util.background()
    global api_key

    global text_spinner_placeholder_1,text_spinner_placeholder_2,text_spinner_placeholder_3,text_spinner_placeholder_4
    text_spinner_placeholder_1 = st.empty()


    global choice1,choice2,choice3
    choice1 = bool
    choice2 = bool
    choice3 = bool

    if 'api_key' in st.session_state:
        api_key = st.session_state.api_key

        st.header('💭 找出將使用的SEO關鍵字')

        st.subheader('輸入您想了解的事物關鍵字')
        word = st.text_input('例如：水壺、短靴、或是您會打在搜尋引擎的字詞',key="搜尋字詞")

        #執行SEO關鍵字找尋function
        st.session_state.keyword_button = not st.button(
        label="開始找尋",
        on_click=keyword_function,
        args=(word, api_key),key='找尋SEO')

        #若過程有錯顯示錯誤
        text_spinner_placeholder_1 = st.empty()

        #產出最後成果
        if st.session_state.keyword_tweet:
            with st.expander('可使用以下SEO關鍵字'):
                st.write(st.session_state.keyword_tweet)
    else:
        st.warning("請至首頁 Home 填寫 API Key")

if __name__ == '__main__':
    main()