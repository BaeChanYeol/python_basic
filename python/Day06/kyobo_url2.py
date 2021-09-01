
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs
from datetime import datetime

d = datetime.today()

file_path = f"C:/Users/admin/Desktop/java_web_LKM/python/crawling/교보 베스트셀러({d.year}년 {d.month}월 {d.day}일).html"

with codecs.open(file_path, mode="w", encoding="utf-8") as f:
    driver = webdriver.Chrome(r'C:\Users\USER\Desktop\chanyeol\Java_Web_BCY\python\crawling\chromedriver.exe')
    driver.get('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79')

    time.sleep(1)

    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')

    title_list = soup.find_all('div', class_='title')
    # print(title_list)
    
    rank = 1

    f.write("<!DOCTYPE HTML> \r\n")
    f.write("<html> \r\n")
    f.write("<head> \r\n")
    f.write('<meta charset="UTF-8" \r\n')
    f.write('<title>교보문고 베스트셀러 1~20위</title>')
    f.write('</head>')
    f.write('<body>')

    for idx in range(len(title_list)):
        if idx > 31:
            f.write('<p style="font-size:20px;"> \r\n')
            f.write(f'<b>순위: {rank}위 </b> <br> \r\n' )
            a_url = str(title_list[idx].find('a'))
            f.write(a_url + "\n <hr> \n")
            rank += 1
            f.write('</p>')
    
    f.write('</body> \r\n')
    f.write('</html> \r\n')




