import streamlit as st
import time

import streamlit_crawler_Ella_addlink
import _util
import SEO_prompt_course

#存取圖片
if "image" not in st.session_state:
    st.session_state.image = ''


def main():

    _util.background()
    global api_key

    if 'api_key' in st.session_state:
        api_key = st.session_state.api_key

        st.header('💭 產出參考圖片及連結')
        st.info('圖片產出中，請稍候')

        #圖片
        st.markdown('#### 參考圖片')
        photo_sample = st.session_state.image
        st.image('https:'+photo_sample.split(':')[1])

        #source link
        st.markdown('#### 參考資料來源')
        st.text_area("資料來源",value=st.session_state.link_tweet)

    else:
        st.warning("請至首頁 Home 填寫 API Key")



if __name__ == '__main__':
    main()