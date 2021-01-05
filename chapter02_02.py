# Chapter02-2
# 파이썬 심화
# special Method(Magic Method)

# 매직 메소드
# 파이썬의 핵심

# 매직 메소드 기초 설명

# 기본형
# 이미 파이썬 내부에서 만들어진 어떤 연산자들을 내부적으로 오버로딩해서 사용할수 있게 먼저 만들어놓은 메소드들의 집합을 의미함

print(int)
# 모든 속성 및 메소드 출력
print(dir(int))  # 언더바 두개로 시작하는걸 매직메소드라고함
print()
print()
print()
n = 100

# 사용
print('Ex1-1 - ', n+200)
print('Ex1-2 - ', n.__add__(200))  # 이게 +를 썼을씨 자동으로 이런식으로 매직메소드가 실행이 되는거임
print('Ex1-3 - ', n.__doc__)
print('Ex1-4 - ', n.__bool__(), bool(n))  # 0이면 false 아니면 true
print('Ex1-5 - ', n*100, n.__mul__(100))  # 곱셈

print('-'*80)
print('-'*80)

# 클래스 예제1


class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('Called. >> __ge__ Method.')

        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):  # 뺄셈
        print('Called >>> __sub__')
        return abs(self._height - x._height)


# 인스턴스 생성
s1 = Student('Jame', 181)
s2 = Student('Mie', 156)

# print(s1._height > s2._height)

# 매직메소드 출력
print('Ex2-1 - ', s1 >= s2)
print('Ex2-2 - ', s2 <= s1)
print('Ex2-3 -', s1 - s2)
print('Ex2-4 -', s2 - s1)
print('Ex2-5 - ', s1)
print('Ex2-6 - ', s2)

print('*'*80)
print('*'*80)
print()

# 클래스 예제2

# 벡터(Vector) # Numpy에서 사용 / 데이터분석
# 좌표평면에서 크기와 방향을 가짐


class Vector(object):
    def __init__(self, *args):
        '''Create a vector example : v = Vector(1,2)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Returns the vector informations'''
        return 'Vector(%r,%r)' % (self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addtion of self and other '''
        return Vector(self._x + other._x, self._y+other._y)

    # def __mul__(self, other):
    #     return Vector(self._x * other._x, self._y*other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y*y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직 메소드 출력
print('Ex3-1 - ', Vector.__init__.__doc__)
print('Ex3-2 - ', Vector.__repr__.__doc__)
print('Ex3-3 - ', Vector.__add__.__doc__)
print('Ex3-4 - ', v1, v2, v3)
print('Ex3-5 - ', v1+v2)
print('Ex3-6 - ', v1*3)
print('Ex3-7 - ', v2*10)
print('Ex3-8 - ', bool(v1), bool(v2))
print('Ex3-9 - ', bool(v3))


print()
print()
