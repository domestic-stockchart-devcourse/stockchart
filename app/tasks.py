from background_task import background
from .models import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


@background(schedule=10)
def crawl_news():
    pass


@background(schedule=60*10)
def crawl_chart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    # 1. 페이지 이동
    url = 'https://finance.naver.com/sise/sise_quant.naver'
    driver.get(url)

    # 조회 항목 초기화
    checkboxes = driver.find_elements(By.NAME, 'fieldIds')
    for checkbox in checkboxes :
        if checkbox.is_selected() : # 체크된 상태라면
            checkbox.click() # 체크 해제

    # 조회 항목 설정 (수정 가능)
    items_to_select = ['시가총액', '거래량', '전일거래량']
    for checkbox in checkboxes :
        parent = checkbox.find_element(By.XPATH, '..') #부모 element
        label = parent.find_element(By.TAG_NAME, 'label')
        if label.text in items_to_select :
            checkbox.click()

    # 적용하기 클릭
    btn_apply = driver.find_element(By.XPATH, '//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img')
    btn_apply.click()

    # 2. 데이터 추출
    df = pd.read_html(driver.page_source)[1] #df[0] = select box구역, df[1] = 주식정보
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    df['N'] = df['N'].astype(int)

    highest_volume_df = df.head(6)

    # db에 데이터 생성
    for index, row in highest_volume_df.iterrows():
        TradingVolume.objects.create(
            rank=row['N'],  
            name=row['종목명'],  
            current_price=row['현재가'],  
            price_change=row['전일비'],  
            percent_change=row['등락률'],  
            volume=row['거래량'], 
            prev_volume=row['전일거래량'], 
            market_cap=row['시가총액']
        )
        
    
    driver.quit()
