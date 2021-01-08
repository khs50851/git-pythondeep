# Chapter06-1
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking에 *붙여서, *args
# 반복형 객체를 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter(x)라는 함수를 호출하기 때문

import itertools
from collections import abc
t = 'ABCDEF'

# for 사용
for c in t:
    print('Ex1-1 - ', c)

print()

# while
w = iter(t)

while True:
    try:
        print('Ex1-2 - ', next(w))
    except StopIteration:
        break

print()
print()


# 반복형 확인
print('Ex1-3 - ', hasattr(t, '__iter__'))  # 반복 가능한 속성 있는지 물어보는거
print('Ex1-4 - ', isinstance(t, abc.Iterable))

print()
print()

# next 사용


class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # print('Called next')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration
        self._idx += 1
        return word

    def __iter__(self):
        print('Called iter')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')

print('Ex2-1 - ', wi)
print('Ex2-2 - ', next(wi), 'idx : ', wi._idx)
print('Ex2-3 - ', next(wi), 'idx : ', wi._idx)
print('Ex2-4 - ', next(wi), 'idx : ', wi._idx)
print('Ex2-5 - ', next(wi), 'idx : ', wi._idx)
print('Ex2-6 - ', next(wi), 'idx : ', wi._idx)
print('Ex2-7 - ', next(wi), 'idx : ', wi._idx)
print('Ex2-8 - ', next(wi), 'idx : ', wi._idx)

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제네레이터 완화
# 2. 단위 실행 가능한 코루틴 구현에 아주 중요
# 3. 제네레이터는 넥스트가 호출될때 하나씩하나씩 가져오고 다음에 가져올 위치를 기억함
# 4. 딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터 -> 이게 위에 next 함수 만든거랑 똑같이 해줌
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Who says the nights are for sleeping')

wt = iter(wg)  # next가 없어서 iter함수로 구현함 해줘야함

print('Ex3-1 - ', wi)
print('Ex3-2 - ', next(wt))
print('Ex3-3 - ', next(wt))
print('Ex3-4 - ', next(wt))
print('Ex3-5 - ', next(wt))
print('Ex3-6 - ', next(wt))
print('Ex3-7 - ', next(wt))
print('Ex3-8 - ', next(wt))

print()
print()

# Generator 예제1


def generator_ex1():
    print('start!')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')


temp = iter(generator_ex1())

# print('Ex4-1 - ',next(temp)) # AAA에 멈춰있음
# print('Ex4-2 - ',next(temp)) # BBB에 멈춰있음 end전
# print('Ex4-3 - ',next(temp)) # 여긴 에러

for v in generator_ex1():
    pass
    # print('Ex4-3 - ',v) # 처음부터 끝까지 다 출력됨
    # next를 내부적으로 계속 호출하면서 하나씩 보여주는거임
    # for문에서 stop에러 나오는걸 잡아주기때문에 안정적으로 사용 가능

print()
print()

# Generator 예제2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())  # 함수형태로 x에 담아놓음

print('Ex5-1 - ', temp2)  # AAA를 반환하는데 그걸 x로 접근해서 *3하고 리스트에 추가
print('Ex5-2 - ', temp3)  # 이떄는 제네레이터가 반환
print()
print()

for i in temp2:
    print('Ex5-3 - ', i)

print()

for i in temp3:
    print('Ex5-4 - ', i)  # 이건 제네레이터 형태로 출력됨

print()
print()

# Generator 예제3(자주 사용하는 함수)


gen1 = itertools.count(1, 2.5)  # 1부터 2.5씩 증가하면서 무한대의 수를 만듬
print('Ex6-1 - ', next(gen1))  # next호출 전까지 계산식만 가지고 있고 next가 호출되면 만들어냄
print('Ex6-2 - ', next(gen1))
print('Ex6-3 - ', next(gen1))
print('Ex6-4 - ', next(gen1))
# ... 무한

# 조건

print()
print()

gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(
    1, 2.5))  # 첫번째로 종료값을 원하는 함수를 입력받음 예시는 1000미만 수까지 받아라

for v in gen2:
    pass
    # print('Ex6-5 - ',v)


print()
print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print('Ex6-6 - ', v)  # 3미만의 값은 1,2인데 이거의 반대인 3,4,5가 나옴

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('Ex6-7 - ', v)

print()

# 연결1

gen5 = itertools.chain('ABCDE', range(1, 11, 2))

# 반복 가능한것들을 합쳐줌 ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]
print('Ex6-8 - ', list(gen5))

# 연결2

gen6 = itertools.chain(enumerate('ABCDE'))

print('Ex6-9 - ', list(gen6))  # 인덱스 번호랑 함께 튜플형태로 반환

# 개별
gen7 = itertools.product('ABCDE')

print('Ex6-10 - ', list(gen7))  # 반복가능한 자료를 하나씩 다 쪼개서 튜플형태로

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)  # 모든 경우의 수를 2번씩 반복

print('Ex6-11 - ', list(gen8))  # 반복가능한 자료를 하나씩 다 쪼개서 튜플형태로

print()
print()

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print('Ex6-12 - ', list(gen9))

for chr, group in gen9:
    print('Ex6-12 - ', chr, ' : ', list(group))  # 반복되는걸 집합으로 만들어서 리스트로 가지고있음
# Ex6-12 -  A  :  ['A', 'A', 'A']
# Ex6-12 -  B  :  ['B', 'B']
# Ex6-12 -  C  :  ['C', 'C', 'C', 'C']
# Ex6-12 -  D  :  ['D', 'D']
# Ex6-12 -  E  :  ['E', 'E', 'E']

print()
