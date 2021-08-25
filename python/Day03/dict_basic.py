
'''
* 사전 (Dictionary)

- 사전은 키(key)와 값(value)의 쌍을 저장하는 대용량의 자료구조.
- 사전은 Map이라고도 부르며 연관배열이라고도 부릅니다.
- 사전을 정의하는 기호는 {}이고, 괄호 안에 데이터를
key:value 형태로 나열하여 저장합니다.
'''
students = {'멍멍이':'김철수', '야옹이':'박영희', '짹짹이':'홍길동'}
print(type(students))
print(len(students))

'''
- 사전에 사용되는 key값은 중복값을 가질 수 없고 변경도 안됩니다.
- 그러나 value값은 중복을 허요하며 데이터를 자유롭게 편집할 수도
있습니다.
- 사전 내부에 저장된 데이터를 검색할 때는 인덱스 대신 
key를 사용합니다. (시퀀스 자료가 아닙니다.)
'''
print(students['멍멍이'])
print(students['짹짹이'])
# print(students['메롱이']) (x)

# in 키워드를 사용하여  key의 존재 유무를 알수 있습니다.
print('멍멍이' in students)
print('메롱이' in students)




