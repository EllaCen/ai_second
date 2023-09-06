import time
import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
# from fake_useragent import UserAgent


# driver_path=ChromeDriverManager().install() #下載latest release版本的chromedriver，並返回其在本機的下載儲存路徑
# driver = webdriver.Chrome(service=ChromeService(driver_path)) 


# from webdriver_manager.core.utils import get_browser_version_from_os

from webdriver_manager.chrome import ChromeDriverManager
import requests,re,time,os


def driver_setting():
    """setting user agents and cookies
    """
    my_user_agents  = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    # my_user_agents = ua.random
    my_cookies = [
    {
        'domain': '.google.com.tw',
        'expiry': 1705130529,
        'httpOnly': True,
        'name': 'NID',
        'path': '/',
        'sameSite': 'None',
        'secure': True,
        'value': '511=RwZVQHxVjbzOd4ZyFh9izNrk-Len5XAN2xxfW1ufU8ftfcNl-zPIMhmuLoDZtU8Cs02iY56VDdI72rctkabu29vf4L-PYTJ35JolZrf9OI__JjAuXiRfwkhsMmPRbEm5CKqSyvWMQ_X9Ia6mGmtP5rLQDL4uTSuv1lCL0ecvWNY'
    },
    {
        'domain': '.google.com.tw',
        'expiry': 1704871329,
        'httpOnly': True,
        'name': 'AEC',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': 'Ad49MVHBuBDhQUDQFiVzvCm0gthettF2E8G6aEuEqecsiXIwFyNlAOg52sI'
        },
    {
        'domain': '.google.com.tw',
        'expiry': 1691911330,
        'httpOnly': False,
        'name': '1P_JAR',
        'path': '/',
        'sameSite': 'None',
        'secure': True,
        'value': '2023-07-14-07'
        }
    ]
    return my_user_agents, my_cookies

def url_manager(search_keyword: str=None):
    """url manager（直接到新聞頁面）
    """
    url = f'https://www.google.com.tw/search?q={search_keyword}&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiw4of_0Y2AAxVgmVYBHXnwAyMQ0pQJKAR6BAgHEAc&biw=932&bih=600&dpr=2'
    return url

def html_downloader(url: str=None):
    """進入到頁面獲取網頁元素
    """
    # get user_agents, cookies
    user_agents, cookies = driver_setting()
    # setting options
    chrome_options = Options()
    chrome_options.add_argument(user_agents)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popups")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080")
    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager(version="116.0.5845.96").install()),
    #     options=chrome_options 
    #     )

    driver = webdriver.Chrome(
        service = Service(),
        options=chrome_options 
        )
        
    # 登陸頁面，設定 cookies
    driver.get(url)
    time.sleep(3)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url)

    # 抓取 html elements
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def html_parser(soup):
    """解析元素，回傳整理後的網頁
    """
    all_title = soup.find_all("div", {"class":"n0jPhd ynAwRc MBeuO nDgy9d"})
    title_text = "\n".join([title.text for title in all_title])
    link_area = soup.find_all("a", {"class":"WlydOe"})
    link=[i["href"] for i in link_area]
    return title_text,link

def run_crawler(search_keyword: str=None):
    """執行爬蟲程式，最後回傳整理好的 title

    Args:
        search_keyword (str, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    url = url_manager(search_keyword)
    soup = html_downloader(url)
    title_text,link = html_parser(soup)
    return title_text,link
