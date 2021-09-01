
print("!! 최초 실행시 약간의 로딩이 발생할 수 있으니 잠시만 기다려주세요!(최대 1분)")
print("인터넷 연결이 되어있어야 합니다!!" )
import os
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
import time as t

# 헤더 정보 초기화
opener = req.build_opener()
# User Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
# 헤더 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

print("\n### 검색어를 입력하시면 해당 검색어에 맞는 이미지를 50개 다운로드 받습니다.")
print("### 이미지 자료는 네이버 검색자료를 수집합니다.")
print("### 다운받은 이미지는 C드라이브 imagedown폴더에 자동 저장됩니다.")

# 검색어
s = input("### 검색어 입력: ")
quote = rep.quote_plus(s)
# URL 완성
url = base + quote

# 요청 url 확인
# print("req url:",url)

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "C:/imagedown/"

# 폴더 생성 예외처리
try:
    # 기존 폴더 있는지 체크
    if not os.path.isdir(savePath):
        # 없으면 폴더 생성
        os.mkdir(savePath)
except OSError as e:
    print("folder creation failed.")
    print("folder name: {}".format(e.filename))

    #런타임 에러
    raise RuntimeError("System exit!")

else:
    # 폴더 생성이 되었거나, 존재할 경우
    print("folder created")


# bs4 초기화
soup = BeautifulSoup(res, 'html.parser')

# print(soup.prettify())

# select 사용
img_list = soup.select('div.img_area > a.thumb._thumb > img')
# print(img_list)

for i, img in enumerate(img_list, 1):
    # 속성 확인
    # print(img, i)
    
    # 저장 파일명 및 경로
    full_file_name = os.path.join(savePath, savePath + str(i) + '.png')

    # 파일명
    # print(full_file_name)

    # 다운로드 요청
    req.urlretrieve(img['data-source'], full_file_name)

# 다운 완료
print("download success!")

path = os.path.realpath(savePath)
os.startfile(path)

print("5초 뒤 자동 종료됩니다!")
t.sleep(5)