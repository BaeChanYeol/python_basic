from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime

# 엑셀처리 모듈 임포트
import xlsxwriter

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
from fake_useragent import UserAgent

# 이미지를 바이트 변환 처리 모듈
from io import BytesIO

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

from xlsxwriter import workbook
from xlsxwriter import worksheet

d = datetime.today()

file_path = f'C:/Users/admin/Desktop/java_web_LKM/python/crawling/멜론차트 1~100위_{d.year}_{d.month}_{d.day}.xlsx'

# User Agent 정보 변환 (필수는 아니다.)
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().ie)]
req.install_opener(opener) # 새로운 헤더 정보 삽입.

workbook = xlsxwriter.Workbook(file_path)

worksheet = workbook.add_worksheet()

chrome_options = Options()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome('C:/Users/admin/Desktop/java_web_LKM/python/crawling/chromedriver.exe', options = chrome_options)

browser.implicitly_wait(5)

cell_format = workbook.add_format({'bold':True, 'font_color':'white', 'bg_color':'red'})
worksheet.write('A1', '커버 사진', cell_format)
worksheet.write('B1', '순위', cell_format)
worksheet.write('C1', '가수 이름', cell_format)
worksheet.write('D1', '앨범명', cell_format)
worksheet.write('E1', '노래명', cell_format)

cell_cnt = 2

# 페이지 이동
target_page = 'https://www.melon.com/chart/index.htm'
browser.get(target_page)

soup = BeautifulSoup(browser.page_source, 'html.parser')

for cnt in [50, 100]:

    song_tr_list = soup.select(f'#lst{cnt}')

    for song_tr in song_tr_list:

        # 순위 찾기
        rank = song_tr.select_one('div.wrap.t_center').text.strip()
        print(rank)

        # 이미지 찾기
        img_tag = song_tr.select_one('div.wrap > a > img')
        img_url = img_tag['src']
        print('이미지:', img_url)

        # 가수 이름 찾기
        artist_name = song_tr.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
        print('가수 이름:',artist_name)

        # 앨범명 찾기
        album_name = song_tr.select_one('div.wrap div.ellipsis.rank03 > a').text.strip()
        print('앨범명:',album_name)

        # 노래명 찾기
        song_name = song_tr.select_one('div.wrap div.ellipsis.rank01 > span > a').text.strip()
        print('노래명:',song_name)

        print('=' * 40)

        try:
            img_data = BytesIO(req.urlopen(img_url).read())

            worksheet.insert_image(f'A{cell_cnt}', img_url, {'image_data':img_data, 'x_scale':0.5, 'y_scale':0.5})
        except:
            pass
            # traceback.print_exc()
        
        worksheet.write(f'B{cell_cnt}', rank)
        worksheet.write(f'C{cell_cnt}', artist_name)
        worksheet.write(f'D{cell_cnt}', album_name)
        worksheet.write(f'E{cell_cnt}', song_name)

        cell_cnt += 1

browser.close()
workbook.close()


