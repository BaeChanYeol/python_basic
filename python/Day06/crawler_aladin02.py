
from selenium import webdriver
import time

from bs4 import BeautifulSoup
import traceback
import codecs
from datetime import datetime

'''
* 표준 모듈 codecs

- 웹이나 다른 프로그램의 텍스트 데이터와 
파이썬 내부의 텍스트 데이터의 인코딩 방식이 서로 다를 경우에
내장함수 open()이 제대로 인코딩을 적용할 수가 없어서
에러가 발생합니다. (UnicodeEncodeError)

- 파일 입/출력 시 인코딩 코덱을 변경하고 싶다면
 codecs 모듈을 사용합니다.
'''

d = datetime.today()

file_path = f'rC:\Users\USER\Desktop\chanyeol\Java_Web_BCY\python\crawling\알라딘 베스트셀러 1~400위_{d.year}_{d.month}_{d.day}.txt'

'''
# with문을 사용하면 with 블록을 벗어나는 순간 
객체가 자동으로 해제됩니다.(자바의 try with resource와 비슷)
# with 작성 시 사용할 객체의 이름을 as 뒤에 작성해 줍니다.
'''

with codecs.open(file_path, mode='w', encoding='utf-8') as f:

    driver = webdriver.Chrome(r'C:\Users\USER\Desktop\chanyeol\Java_Web_BCY\python\crawling\chromedriver.exe')
    driver.get('https://www.aladin.co.kr')
    time.sleep(1.5)

    driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

    rank = 1

    for n in range(2, 10):
        best_tab = f'//*[@id="newbg_body"]/div[3]/ul/li[{n}]'
        driver.find_element_by_xpath(best_tab).click()

        src = driver.page_source

        soup = BeautifulSoup(src, 'html.parser')

        div_list = soup.find_all('div', class_='ss_book_box')


        for div in div_list:
            book_info = div.find_all('li')

            if book_info[0].text[0] != '[':
                book_title = book_info[0].text
                book_author = book_info[1].text
                book_price = book_info[2].text
            else:
                book_title = book_info[1].text
                book_author = book_info[2].text
                book_price = book_info[3].text


            auth_info = book_author.split('|')

            f.write(f'# 순위: {rank}위 \n')
            f.write('# 제목:' + book_title + '\n')
            f.write('# 저자:' + auth_info[0] + '\n')
            f.write('# 출판사:' + auth_info[1] + '\n')
            f.write('# 출판일:' + auth_info[2] + '\n')
            f.write('# 가격:' + book_price.split(', ')[0] + '\n')
            f.write('-' * 40 + '\n')
            rank += 1


