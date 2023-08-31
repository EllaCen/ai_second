import streamlit as st
import time

import streamlit_crawler_Ella_addlink
import _util
import SEO_prompt_course


# 使步驟可連續
if "word" not in st.session_state:
    st.session_state.word = None

if 'word' in st.session_state:
    word = st.session_state.word

if "keyword_tweet" not in st.session_state:
    st.session_state.keyword_tweet = None


#文案製作用 使步驟可連續
if 'article_tweet' not in st.session_state:
    st.session_state.article_tweet = ""

#文案標題用 使步驟可連續
if 'title_tweet' not in st.session_state:
    st.session_state.title_tweet = ""

#文案標籤用 使步驟可連續
if 'tag_tweet' not in st.session_state:
    st.session_state.tag_tweet = ""

#存取圖片
if "image" not in st.session_state:
    st.session_state.image = ''


def make_function(api_key, keyword_choice,more,target_audience,style_choice, emoji_num,word):
    if choice1 == True:
        article_function(api_key, keyword_choice, more, target_audience,style_choice, emoji_num)
    if choice2 == True:
        title_function(api_key, keyword_choice,more)
    if choice3 == True:
        tag_function(api_key)
    
    st.session_state.image = SEO_prompt_course.Unsplash(api_key,word)
    

def article_function(api_key, keyword_choice, more, target_audience,style_choice, emoji_num):
        with text_spinner_placeholder_2:
            with st.spinner("文案生成中..."):
                # time.sleep(5)
                article_final = SEO_prompt_course.SEO_content(api_key, keyword_choice, more, target_audience,style_choice, emoji_num)
                
                st.session_state.article_tweet = (
                    article_final
                )

#文案標題製作
def title_function(api_key, keyword_choice,more):
        article_final = st.session_state.article_tweet
        with text_spinner_placeholder_3:
            with st.spinner("標題生成中..."):
                # time.sleep(5)
                title_final = SEO_prompt_course.SEO_title(api_key, article_final,keyword_choice,more) #測試用
                
                st.session_state.title_tweet = (
                    title_final
                )

#文案標籤製作
def tag_function(api_key):
        with text_spinner_placeholder_4:
            with st.spinner("標籤生成中..."):
                article = st.session_state.article_tweet
                # time.sleep(5)
                tag_final = SEO_prompt_course.SEO_hashtag(api_key, article)
                
                st.session_state.tag_tweet = (
                    tag_final
                )


def main():
    _util.background()
    global api_key
    
    global text_spinner_placeholder_1,text_spinner_placeholder_2,text_spinner_placeholder_3,text_spinner_placeholder_4
    text_spinner_placeholder_1 = st.empty()
    text_spinner_placeholder_2 = st.empty()
    text_spinner_placeholder_3 = st.empty()
    text_spinner_placeholder_4 = st.empty()

    global choice1,choice2,choice3
    choice1 = bool
    choice2 = bool
    choice3 = bool

    if 'api_key' in st.session_state:
        api_key = st.session_state.api_key

        st.header('💭 開始製作文案')
        st.subheader('輸入文章呈現風格')

        #文章風格
        style = ['直接明瞭','故事情節','幽默風趣','專業精準','家庭溫馨']
        style_choice = st.selectbox('**風格語氣**',style) 

        #關鍵字方法一：自動抓前面的關鍵字，讓使用者選擇，但需要依據輸出成果斷字
        keyword = st.session_state.keyword_tweet.split("、")
        keyword_choice = st.multiselect('**關鍵字選擇｜備註：請先產出SEO關鍵字**',keyword,default=keyword[0])

        #表情符號，是否需要emoji,數量為何
        # emoji2 = st.number_input('**emoji數量**｜可直接輸入或運用右邊加減號',0)
        emoji = ['4','8','12','0']
        emoji_num = st.selectbox('**emoji數量**',emoji)

        #目標客群描述
        target_audience = st.text_area('**目標客群描述**',key='simple describe')
        
        
        if not  target_audience or not style_choice or not keyword_choice or not emoji_num :
            st.warning("請完整輸入文案敘述")
            return
        
            
        #補充資料
        more = st.text_area('**補充資料**',key='more')

        if len(more)== 0 :
            more = ""
        
        
        #選擇需求
        col1,col2,col3 = st.columns(3)
        with col1:
            choice1 = st.checkbox('製作文案(建議勾選)',key='選擇製作文案',value=True) #,disabled=True
        with col2:
            choice2 = st.checkbox('製作標題',key='選擇製作標題')
        with col3:
            choice3 = st.checkbox('製作標籤',key='選擇製作標籤')


        st.session_state.start_button = not st.button(
        label="開始製作",
        on_click=make_function,
        args=(api_key, keyword_choice,more,target_audience,style_choice, emoji_num,word),key='開始製作')
            
        text_spinner_placeholder_2 = st.empty()
        text_spinner_placeholder_3 = st.empty()
        text_spinner_placeholder_4 = st.empty()
            
            ##製作文案內容
            #產出最後成果
        if st.session_state.article_tweet:
            st.markdown('#### 文案內容')
            final_article = st.text_area('**若需微調可直接修改**', value= st.session_state.article_tweet,key='文案內容產出',height=400)


            ##製作文案標題
            #產出最後成果
        if st.session_state.title_tweet:
            st.markdown('#### 文案標題')
            final_title = st.text_area('**若需微調可直接修改**', value= st.session_state.title_tweet,key='文案標題產出',height=200)

            ##製作文案標籤
            #產出最後成果
        if st.session_state.tag_tweet:
            st.markdown('#### 文案標籤')
            final_tag = st.text_area('**若需微調可直接修改**', value= st.session_state.tag_tweet,key='文案標籤產出',height=300)
            
    else:
        st.warning("請至首頁 Home 填寫 API Key")

if __name__ == '__main__':
    main()