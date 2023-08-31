import openai

api_key = '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'

def test(api_key):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"測試",
            }
        ],
        temperature=0.4,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response["choices"][0]["message"]["content"]


def SEO_crawler_keyword(api_key, crawler):

    # 定義函式，名稱為 SEO_crawler_keyword。
    # 函式的功能是透過 OpenAI 的 GPT 模型來生成 SEO 文案。
    # crawler 為爬蟲下來的資訊。
    
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"你現在是文案小編,需要篩選出有助於提升文案SEO的關鍵字詞，\
                                            請仔細閱讀完從網路爬取下來的內容：{crawler}。\
                                            整理出10項最助於提升文案SEO的關鍵字詞，\
                                            關鍵字詞間使用'、'分隔，不需撰寫文案。\
                                            "}],
        temperature=0.8,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return (response["choices"][0]["message"]["content"])

def SEO_title(api_key, article,keyword,more):

    # 定義函式，名稱為 SEO_title。
    # 函式的功能是透過 OpenAI 的 GPT 模型來生成 SEO 文案。
    # info 為 prompt 的一部分，提供更多範例讓模型學習；more 則為使用者自行提供的補充說明 
    # article、keyword 分別為已生成的文案內容、使用者選擇的關鍵字。
    
    openai.api_key = api_key


    info = '''
    範例一：標題公式，數字+形容詞+目標關鍵字+原理+承諾
    舉例如下：
    一天15分鐘輕鬆學習英文變達人
    5大簡單內容行銷秘訣，讓你超越競爭對手
    怎麼樣的勇氣讓我離職創業，建立10人團隊新創公司
    範例二：在標題點出解法，卻不完整說出答案
    舉例如下：
    誰來過你的部落格？新手部落客自架站的3大注意事項
    家中 Wi-Fi 訊號老是斷線？可以先用這3個方法測試'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"接下來我將請你產出10個文章標題，有助於提升{article}這篇文案的SEO，\
                                            請閱讀範例：{info}，請先學習範例，並閱讀{more}後，再開始文案標題的設計。\
                                            範例中的目標關鍵字請運用{keyword}\
                                            "}],
        temperature=0.8,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # 預期prompt
    # 接下來我將請你產出10個助於提升{crawler}這篇文章的SEO的文章標題，\
    # 請閱讀範例：{info}，請先學習範例，閱讀{more}與後，再開始文案標題的設計。\
    # 範例中的目標關鍵字請運用{keyword}

    return (response["choices"][0]["message"]["content"])

def Unsplash(api_key, word):

    # 定義函式，名稱為 resource_link
    # 函式的功能是透過 OpenAI 的 GPT 模型與Unsplash API 找尋圖片
    # word 為使用者搜尋字詞。
    
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"我現在需要你找圖片，從現在起，當你想發送一張圖片時，請使用「markdown 語法」，\
                                            並且不要有反斜線，不要用代碼塊，\
                                            使用 Unsplash API (https://source.unsplash.com/1600x900/?<PUT YOUR QUERY HERE>)。\
                                            如果你明白了，請給我一張{word}的照片"
                                            }],
        temperature=0.8,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return (response["choices"][0]["message"]["content"])


def SEO_content(api_key, crawler_select, more, target_audience,style_choice, emoji_num):

    # 定義函式，名稱為 SEO_content。
    # 函式的功能是透過 OpenAI 的 GPT 模型來生成 SEO 文案。
    # info 為 prompt 的一部分，提供更多範例讓模型學習
    # crawler_select, content, target_audience,style_choice, emoji_num 分別為使用者選擇的關鍵字,使用者自行提供的補充說明, 目標受眾, 文案風格, emoji 數量 。
    
    openai.api_key = api_key


    info = '''
    [SEO 說明以及文案範例]
    1. SEO 為「搜尋引擎優化」，是「想辦法提高 Google 搜尋排名」的一種內容規劃與行銷技巧。

    2. 文案範例：手機文案（平台 Instagram)
    連假去哪裡😋？
    快帶著Galaxy S21 Ultra 5G來場Road Trip🚗🚙🚗🚙
    遠方的山嵐、牛奶般的雲朵、一望無際的大海
    用億級畫素記錄所有沿途美景😍

    手機界的單眼 星勢力來襲
    🎁Galaxy S21 5G 旗艦系列即日起~3/31
    🎁登錄送藍牙智慧防丟器以及三合一無線閃充充電板
    🎁購買Galaxy S21 Ultra 5G再送矽膠薄型背蓋(附S Pen)


    3. 範例：課程募資文案 （平台 Facebook)
    【 🏃‍♀️ 募資特惠最後倒數 11 小時 🏃‍♀️ 女孩必修穿搭術：打造專屬於你的穿搭美學 👚 】
    流行總是瞬息萬變 🌪，而 #穿衣風格 也是五花八門，讓人難以選擇 🤔
    您是否想知道自己的身形、膚色適合什麼樣的衣服？🤷🏻‍♀️
    您是否覺得在學習 #穿搭  的路上花費了許多心力和金錢？💰
    您是否想學會穿搭的小技巧？👗
    ✨ 我們可以解決您的煩惱！

    【女孩必修穿搭術：打造屬於你的穿搭美學】
    👉🏻 募資期間:4/26 (三) 中午 12:00 至 5/25 (四) 晚上 11:59
    👉🏻 募資優惠價:NT$999 / 原價 NT$1,588
    👉🏻 課程詳情:https://hahow.in/cr/nicole-outfit

    4. 範例：水壺商品文案 （平台 商品頁面）
    - 台灣人氣插畫家WHOSMiNG聯名
    - 真空304不鏽鋼
    - 雙層結構保溫保冷6小時
    - 圓潤好握取把手設計
    - 輕盈重量持握感加分

    生活是什麼? 打開一本有溫度的書不被打擾的細讀，漫步在生活城市之中觀察平常不會注意的小細節，拎著自己喜愛的保溫瓶，好好喝上一口令你滿足的飲品。
    以圓潤好握取的把手,配上啞光色的外型,讓您的OFF TIME格外輕鬆自在,以雙層真空304不銹鋼結構,讓溫度能保冷/保溫6小時,而輕盈的重量為持握感大加分！'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"你現在是文案小編,需要撰寫「好的 SEO 文案」,\
                                            請結合{crawler_select}的關鍵字，以及{more}所提供的資訊,\
                                            以{target_audience}為撰寫對象\
                                            學習{info}所提供的說明與範例,\
                                            協助產出以{style_choice}為撰寫風格的一個版本的文案,\
                                            並適時加入{emoji_num}個表情符號。"}],
        temperature=0.8,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return (response["choices"][0]["message"]["content"]) 


def SEO_hashtag(api_key, content):

    # 定義函式，名稱為 SEO_hashtag。
    # 函式的功能是透過 OpenAI 的 GPT 模型來生成 SEO 文案的標籤（hashtag)。
    # content 為生成的文案。
    
    openai.api_key = api_key

    info = '''
    [Hashtag 標籤的目的與範例]

    1. Hashtag 是「 依照主題來互相參照的使用者自訂標籤 」，有助於用戶找到對主題感興趣的貼文
    
    2. 目的：告訴演算法這篇貼文的主題、增加這篇貼文出現在 Hashtag 的頁面的曝光機會

    3. 範例：
    假設發布「台北甜點店的抹茶甜點 」貼文，Hashtag 可以這樣設定：
    - 思考內容與 Hashtag 的關聯度：如 #抹茶 #抹茶甜點 #抹茶蛋糕
    - 希望吸引的使用者族群？：如 #台北美食、#台北甜點、#台北抹茶
    - 你的帳號主題、定位？：如 # XX台北探店記、# XX吃美食、 # XX愛甜點（ XX等於品牌專屬字）
    因此，你的 hashtag 會有 #抹茶 #抹茶甜點 #抹茶蛋糕 #台北美食、#台北甜點、#台北抹茶、 # XX愛甜點 等
    
    '''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"你現在是文案小編,需要協助生成與{content}相關的標籤，\
                                            來增加貼文被曝光、被搜尋的機會。\
                                            請參考{info}的說明，\
                                            生成 8-15 個文案標籤(Hashtag)。\
                                            "}],
        temperature=0.8,
        max_tokens=1121,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return (response["choices"][0]["message"]["content"])   