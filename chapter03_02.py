# Chapter03-2
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 x, Set -> 중복 허용 x
# Dict 및 set 심화
# 중복을 허용하지 않는다는건 내부적으로 중복값이 있는지 검사
# 이때 해시테이블 엔진에서 해쉬값이라는 숫자를 만들어 그게 같으면 중복되는 값인거고 아니면 서로 다른 값이라는거

# Dict 구조
from unicodedata import name
from dis import dis
from types import MappingProxyType
import csv
print('Ex1-1 - ')
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
# 이걸 확인한다는건 중복을 허용할지 말지 생각해볼수있는거
t1 = (10, 20, (30, 40, 50))  # 튜플안에 튜플이기때문에 값을 변경 x
t2 = (10, 20, [30, 40, 50])  # 튜플 안에 변경가능한 리스트가 있으므로 해쉬값을 생성할수없음 (어차피 바뀔수있기떄문에)

print('Ex1-2 - ', hash(t1))
# print('Ex1-2 - ', hash(t2))  # 리스트가 안에 있기때문에 해쉬가 필요없음 그래서 해쉬값이 나오지 않고 에러남

print()
print()

# 지능형 딕셔너리(Comprehending Dict)

# 외부 CSV TO List of tuple 튜플 형태의 리스트

with open('./resources/test1.csv', 'r', encoding='utf-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)

    # 변환
    NA_CODES = [tuple(x) for x in temp] 

print('Ex2-1 - ',)
print(NA_CODES)
print()
print()

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('Ex2-2 - ',)
print(n_code1)

print()
print()

print('Ex2-3 - ',)
print(n_code2)

print()
print()

# Dict Setdefault 예제

source = (  # 이런식으론 키가 중복되고 있음
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5')
)

new_dict1 = {}
new_dict2 = {}

# Not use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('Ex3-1 - ', new_dict1)

# Use setdefault
for k, v in source:
    # 첫번째 인자에 있으면 키를 그냥 사용 없으면 빈 리스트 키 있으면 해당 키에 어펜드 하는거
    new_dict2.setdefault(k, []).append(v)

print('Ex3-2 - ', new_dict2)

print()
print()

# 사용자 정의 dict 상속(UserDict 가능)


class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):  # 인스턴스 키가 문자형일 경우에는
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default  # 없을때는 None 반환

    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])  # 리스트형태의 튜플도 받음


# 출력
print('Ex4-1 - ', user_dict1, user_dict2, user_dict3)
print('Ex4-2 - ', user_dict2.get('two'))
print('Ex4-3 - ', 'one' in user_dict3)  # 내부적으로 contains 메소드 호출됨
# print('Ex4-4 - ',user_dict3['three']) # missing 메소드 실행됨
print('Ex4-5 - ', user_dict2.get('three'))
print('Ex4-6 - ', 'three' in user_dict3)

# immutable Dict 딕셔너리는 값 변경 가능 근데 변경 못하게 하는 클래스가 있음


d = {'key1': 'Test1'}

# Read Only
d_frozen = MappingProxyType(d)

print('Ex5-1 - ', d, id(d))
print('Ex5-2 - ', d, id(d_frozen))
print('Ex5-3 - ', d is d_frozen, d == d_frozen)

# d_frozen['key1'] = 'Test2' # 수정할 수 없음

d['key2'] = 'Test2'  # 이렇게 원본은 수정 가능
print('Ex5-4 - ', d)

# Set 구조 순서 없고 중복 x

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # {} 이건 딕셔너리임
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')
# print('Ex6-1 - ', s1, type(s1))

# 추가 불가
# s5.add('Melon') # 이렇게 추가 할 수 없음
print('Ex6-1 - ', s1, type(s1))
print('Ex6-2 - ', s2, type(s2))
print('Ex6-3 - ', s3, type(s3))
print('Ex6-4 - ', s4, type(s4))
print('Ex6-5 - ', s5, type(s5))

# 선언 최적화

# a = {5}
# b = set([10])
print()
print('Ex6-5 -')
print(dis('{10}'))  # 여긴 3개의 라인으로 구성됨 그래서 이렇게 하는게 더 빠름
print('Ex6-6 -')
print(dis('set([10])'))  # 여긴 5개의 라인으로 구성됨

print()
print()

# 지능형 집합set(Compregending set)
print('Ex7-1 - ')

# chr은 0부터 256까지의 유니코드 데이터를 보여줌 이걸 name으로 하면 이름으로 바꿔줌
print({name(chr(i), '') for i in range(0, 1000)})
