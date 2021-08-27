
'''
* 표준 모듈 random

- 프로그램이 무작위 동작을 하게 하려면 난수값(랜덤값)이 필요합니다.

- 랜덤값을 난수라고 부르며, 난수를 쉽게 발생시킬수 있는
함수를 제공하는 모듈이 random 모듈입니다.

- random 모듈의 random() 함수는 0.0이상 1.0미만의
실수 난수값을 발생시킵니다.
'''
import random as r

rn = r.random()
# print('랜덤값:', rn)

'''
- 정수 난수는 randint() 함수를 사용합니다.
- randint() 는 인수로 시작범위와 끝 범위를 지정하는데,
끝 범위도 난수값에 포함되는 특징이 있습니다. (주의! 미만이 아님)
'''
pets = ['멍멍이', '야옹이', '짹짹이', '호랑이', '코끼리']
idx = r.randint(0, 4) # ('미만이 아니에요!')
print('애완동물을 뭘 키울까??: ', pets[idx])

# choice() 함수는 리스트 내부의 임의의 요소를 랜덤으로
# 선택하여 리턴합니다.
print('애완동물을 뭘 키울까??: ', r.choice(pets))

# -shuffle 함수는 리스트의 요소를 무작위로 섞습니다.
print(pets)
r.shuffle(pets)
print(pets)

# -sample() 함수는 리스트의 항목 중 n개를 무작위로 추출하여
# 새로운 리스트로 만들어서 리턴합니다.
# 중복값은 자동으로 배제시키며, 원본 리스트는 변하지 않습니다.

print('-' * 40)
s_list = r.sample(pets, 2)
print(s_list)
print(pets)

# sample함수를 활용한 로또번호 6개 뽑기(중복은 알아서 제거)
lotto_nums = list(range(1, 46))
lotto = r.sample(lotto_nums, 6)
lotto.sort()
print(lotto)


