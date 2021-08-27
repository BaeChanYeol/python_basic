

'''
네이버로 접속하셔서
뉴스 스탠드 쪽에 있는 파란색 '네이버 뉴스'를
클릭하세요

상단 메뉴중 정치, 경제, 사회, 생활/문화, 세계, IT/과학
탭을 돌아다니면서 헤드라인 뉴스 4개씩 클리해 주시면됩니다.
driver.back()

XPATH를 따다 보면 규칙을 발견할 수있다.
'''

from selenium import webdriver
import time

#다운로드 받은 크롬 물리드라이버 가동 명령
driver = webdriver.Chrome(r'C:\Users\USER\Desktop\chanyeol\Java_Web_BCY\python\crawling\chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('http://www.naver.com')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)


num = 1
cnt = 0

for i in range(3,9):
    driver.find_element_by_xpath(f'//*[@id="lnb"]/ul/li[{i}]/a/span').click()
    time.sleep(1)
    for j in range(1,5):
        try:
            driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j}]/div[{num}]/ul/li[1]/div[2]/a').click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        except:
            driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j}]/div[{num}]/ul/li[1]/div/a').click()
            time.sleep(1)
       
    if num == 1:
        num = 2