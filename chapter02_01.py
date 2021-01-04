# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value
# 파이썬은 -> 일관성이 있음

# 일반적인 튜플 사용
# 인덱스 0번은 x 1번은 y 이런식으로 말해야하는데 그래서 나온게 namedtuple임

# 네임드튜플 가져옴
from collections import namedtuple
from math import sqrt
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

line_leng1 = sqrt((pt2[0]-pt1[0]) ** 2 + (pt2[1]-pt1[1]) ** 2)

print('Ex1-1 -', line_leng1)

# 네임드 튜플 사용
Point = namedtuple('Point', 'x y')  # 앞에 Point는 아무렇게나 써도됨

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt2.x-pt1.x) ** 2 + (pt2.y-pt1.y) ** 2)

# 출력
print('Ex1-2 -', line_leng2)
print('Ex1-3 - ', line_leng1 == line_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])  # 띄어쓰기도 받지만 이런식으로 리스트로도 받음
Point2 = namedtuple('Point', 'x, y')  # 컴마로 구분도 가능
Point3 = namedtuple('Point', 'x y')  # 이렇게하면 띄어쓰기 주의
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default = False

# 출력
print('Ex2-1 -', Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

p1 = Point1(x=10, y=35)  # x가 없으면 첫번째에 알아서 x로 인식 저렇게 지정할수도있음
p2 = Point2(20, 40)  # x는 20 y는 40
p3 = Point3(45, y=20)  # 첫번째인자인 x에 40 y에 20
# rename 옵션으로 두번째 중복된 x와 class(변수이름으로 할수없음) 이걸 알아서 바꿈
p4 = Point4(10, 20, 30, 40)
# p5 = Point3(temp_dict) # 이렇게하면 저거 하나 자체는 x로 봐서 y가 없다고 나옴
p5 = Point3(**temp_dict)  # 그래서 딕셔너리를 언패킹할땐 아스타(*)를 두개 붙임

print('Ex2-2 -', p1, p2, p3, p4, p5)
print()
print()

# 사용
print('Ex3-1 - ', p1[0]+p2[1])  # Index Error 주의
print('Ex3-2 - ', p1.x+p2.y)  # 클래스 변수 접근방식

# Unpacking
x, y = p3
print('Ex3-3 - ', x+y)

# Rename 테스트
print('Ex3-4 - ', p4)

print()
print()


# 네임드 튜플 메소드

temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point2._make(temp)

print('Ex4-1 - ', p4)

# _fields : 필드 네임 확인
print('Ex4-2 - ', p1._fields, p2._fields,
      p3._fields, p4._fields)  # 필드 네임만 가져옴 x,y

# as_dict() : OrderedDict로 반환
print('Ex4-3 - ', p1._asdict(), p4._asdict())  # ordereddict안에는 튜플로 되어있음
print(dict(p1._asdict()))

# _replace() : 값을 바꿔줌, 근데 튜플은 불변이라 새로운 객체를 반환함 // 수정된 '새로운' 객체 반환
print('Ex4-4 - ', p2._replace(x=100))

print()
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A,B,C,D) 번호 A1~2- B1~20 C1~20 D1~20

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]  # 리스트 컴프리헨션
ranks = 'A B C D'.split()  # 공백을 기준으로 리스트로 만듬
# print(ranks, numbers)

# List Comprehension
# 먼저 랭크로 4번도는데 그 한번한번에 numbers 20번 반복
students = [Classes(rank, number) for rank in ranks for number in numbers]

# print('Ex5-1 - ', len(students))
# print('Ex5-2 - ', students[4].rank)


# 가독성 x
students2 = [Classes(rank, number) for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1, 21)]]

print('Ex6-1 - ', students2)
print('Ex6-2 - ', students2[1])

print()
print()
# 출력
print(type(students2))
for s in students:
    print('Ex7-1 - ', s)
