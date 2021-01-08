# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# class 선언
import random
import abc
from collections.abc import Sequence
import timeit


class VectorP(object):
    def __init__(self, x, y):  # 이닛메소드에서 값을 받을거 제한거는건 별로 안좋음 어차피 나중에 바꿔버릴수있어서
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):  # 객체를 for문으로 next 메소드로 순회
        # 이걸 넥스트로 호출하면 x부터 호출하고 y도 i를 리턴 Generator : 하나씩 반환을 함
        return (i for i in (self.__x, self.__y))

    @property  # 이게 먼저 선행작업을 하고 우리가 만든 메소드가 거기로 들어가서 리턴값이 나옴
    def x(self):  # 함수 이름은 보통 변수 이름으로
        print('Called Property x')
        return self.__x

    @x.setter    # setter는 getter 메소드를 먼저 만들어야함
    def x(self, v):
        print('Called Property x setter')
        self.__x = float(v)

    @property
    def y(self):
        print('Called Property y')
        return self.__y

    @y.setter
    def y(self, v):
        if v < 30:
            raise ValueError('30이하는 불가')
        print('Called Property y setter')
        self.__y = float(v)


# 객체 선언
v = VectorP(20, 40)

# print('Ex1-1 - ', v.__x, v.__y)  # 밑줄 두개면 직접 접근이 안됨


# Getter, Setter
# print(v.__x) # 이건 안됨
# v.x = 10
# v.y = 6 이렇게 하면 30이하라 막힘
# print('x : ', v.x)  # 이렇게 직접적으로 접근 가능
# print('y:', v.y)

print('Ex1-2 - ', dir(v), v.__dict__)  # _VectorP__y ,x,y, 이런식으로
print('Ex1-3 - ', v.x, v.y)

for val in v:  # 이터 메소드가 있기때문에 이런식으로 for문으로 돌릴 수 있음
    print('Ex1-4 - ', val)

# __slot__
# 파이썬 인터프리터에게 통보하는 역할
# 해당 클래스가 가지는 속성을 제한
# 모든 속성은 __dict__으로 관리됨
# 슬롯을 사용해 __dict__ 속성 최적화 -> 다수 객체 생성시 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용 그래서 지정된 속성만 사용가능한 단점이 있음


class TestA(object):
    __slots__ = ('a',)


class TestB(object):
    pass


print()
print()

use_slot = TestA()
no_slot = TestB()

no_slot.a = 10
print(type(no_slot.a))

print('Ex2-1 - ', use_slot)
# print('Ex2-2 - ',use_slot.__dict__) # dict대신 set사용이라 딕 속성이 없다고 나옴
print('Ex2-3 - ', no_slot)
print('Ex2-4 - ', no_slot.__dict__)

# 메모리 사용량 비교

# 측정을 위한 함수 선언


def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner


# print(min(timeit.repeat(repeat_outer(use_slot),number=500000)))  # 함수를 천번이든 만번이든 내가 지정한 만큼 숫자를 실행하는 시간을 반환
# print(min(timeit.repeat(repeat_outer(no_slot),number=500000)))  # 함수를 천번이든 만번이든 내가 지정한 만큼 숫자를 실행하는 시간을 반환

print()
print()

# 객체 슬라이싱


class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):  # 파이썬 어딘가에 있는 len메소드를 구현한거 매직메소드할때랑 같음
        return len(self._numbers)

    def __getitem__(self, idx):  # 이렇게하면 객체 자체를 슬라이싱 가능
        return self._numbers[idx]


s = ObjectS()

print('Ex3-1 - ', s.__dict__)
print('Ex3-2 - ', len(s))  # 안에 len메소드 만들었기 때문에 가능
print('Ex3-3 - ', len(s._numbers))
print('Ex3-4 - ', s[1:100])  # 클래스를 리스트 형식으로
print('Ex3-5 - ', s[-1])
print('Ex3-6 - ', s[::10])

print()
print()

# 파이썬 추상클래스
# 참고 : https://docs.python.org./3/library/collections.abc.html


# 자체적으로 객체 생성 불가
# 상속을 통해 자식 클래스에서 인스턴스를 생성해야 함
# 추상 클래스를 사용하는 이유 : 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 함

# Sequence 상속 받지 않았지만, 자동으로 __iter__,contain__ 기느을 작동
# getitem을 상속받았으면 튜플이나 리스트에 접근하는 메소드인데 iter메소드도 있고 in을 사용하려면 contain도 사용해야한다고 알아서 판단
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1,50,2) # idx 없으면 range 전체를 무조건 리턴


i1 = IterTestA()

print('Ex4-1 - ', i1[4])
print('Ex4-2 - ', i1[4:10])
print('Ex4-3 - ', 3 in i1[1:10])  # contain이 알아서 호출
print('Ex4-4 - ', [i for i in i1])  # 이터레이터, 넥스트 메소드를 알아서 호출

print()
print()

# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작


class IterTestB(Sequence):  # Sequence 추상클래스를 상속 받음
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1,50,2)

    def __len__(self):
        return len(range(1, 50, 2))


i2 = IterTestB()  # __len__ 메소드를 상속받아야 가능

print('Ex4-5 - ', i2[4])
print('Ex4-6 - ', i2[4:10])
print('Ex4-7 - ', 3 in i2[1:10])

# abc 활용 예제


class RandomMachine(abc.ABC):  # 3.4 이하에선 metaclass=abc.ABCMeta 이런식으로 했어야했음

    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''

    @abc.abstractmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))


class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()  # 실행할때마다 난수 생성
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self):
        return self.pick()

# 서브 클래스 확인


print('Ex5-1 - ', issubclass(RandomMachine, CraneMachine))  # 부모자식 확인
print('Ex5-2 - ', issubclass(CraneMachine, RandomMachine))  # 부모자식 확인 뒤에꺼가 부모

# 상속 구조 확인
print('Ex5-3 - ', CraneMachine.__mro__)
cm = CraneMachine(range(1, 100))  # 추상 메소드 구현 안하면 에러

print('Ex5-4 - ', cm._items)
print('Ex5-5 - ', cm.pick())
print('Ex5-6 - ', cm())
print('Ex5-7 - ', cm.inspect())  # 자식에 없는 메소드인데 없으면 알아서 부모에서 끌어옴
print('Ex5-7 - ', cm.inspect())
