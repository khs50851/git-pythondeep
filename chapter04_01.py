# Chapter04-1
# 파이썬 심화
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화 가능 (실행시에 초기화)
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달가능 (sorted(keys=len))
# 4. 함수 결과로 반환 가능 return funcs

# 함수 객체 예제

from functools import partial
from operator import mul
from inspect import signature  # 함수 인자에 대한 정보를 표시하는 클래스형태의 메소드
import random
from operator import add
from functools import reduce


def factorial(n):
    '''Factorial Function -> n:int'''
    if n == 1:  # n < 2
        return 1
    return n*factorial(n-1)  # 5 * 4 * 3 * 2 * 1


class A:
    pass


print('Ex1-1 - ', factorial(5))
print('Ex1-2 - ', factorial.__doc__)
# 함수도 객체 취급함 그래서 많은 속성과 메소드를 가지고 있음
print('Ex1-3 - ', type(factorial), type(A))
print('Ex1-4 - ', dir(factorial))
print()
print('Ex1-5 - ', set(sorted(dir(factorial))) -
      set(sorted(dir(A))))  # 함수만 갖고있는 속성들이 보임
print('Ex1-5 - ', factorial.__name__)  # 함수의 이름 출력
print('Ex1-6 - ', factorial.__code__)  # 파이썬 파일의 위치 인자와 이 안에 코드들을 갖고음

print()
print()

# 변수 할당
var_func = factorial  # 함수 할당

print('Ex2-1 -', var_func)
print('Ex2-2 -', var_func(5))
# 맵을 담음 첫번째 인자로 함수, 두번째인자로 반복가능한거 그 함수를 반복인자만큼 반복함
print('Ex2-3 - ', map(var_func, range(1, 6)))
print('Ex2-4 - ', list(map(var_func, range(1, 6))))  # 1!~5!을 리스트로 반환

# 함수 인수 전달  및 함수로 결과 반환 -> 고위 함수 (Higher-order Function)

# 맵 함수 안에 팩토리얼 함수를 인수로 전달 필터도 필터라는 함수 안에 람다함수를 넣음
print('Ex3-1 - ', list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print('Ex3-2 - ', [var_func(i) for i in range(1, 6) if i % 2])  # 리스트 컴프리헨션

print()
print()

# reduce()


print('Ex3-3 - ', reduce(add, range(1, 11)))  # reduce는 인자를 누적시킴
print('Ex3-4 - ', sum(range(1, 11)))

print()

# 익명 함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장

print('Ex3-5', reduce(lambda x, t: x+t, range(1, 11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인

# funcs() 이런식으로 호출해서 사용가능한지


# 로또 추첨 클래스 선언

class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):  # 이거 오버라이딩 하면 함수처럼 동작할 수 있게함
        return self.pick()


# 객체 생성
game = LottoGame()

# 게임 실행
# 호출 가능 확인
print('Ex4-1 - ', callable(str), callable(list), callable(factorial),
      callable(3.14), callable(game))  # 자료형이나 함수, 클래스를 넣으면 참거짓으로 알려줌
print('Ex4-2 - ', game.pick())
print('Ex4-3 - ', game())
print('Ex4-4 - ', callable(game))  # 원래 false였는데 __call__ 매직메소드를 통해 true로 됨

print()
print()

# 다양한 매개변수 입력(*args, **kwargs)


def args_test(name, *contents, point=None, **attrs):
    return '<args_test> -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)


print('Ex5-1 - ', args_test('test1'))
print('Ex5-2 - ', args_test('test1', 'test2'))
print('Ex5-3 - ', args_test('test1', 'test2', 'test3', id='admin'))
print('Ex5-4 - ', args_test('test1', 'test2', 'test3', id='admin',
                            point=7, user='kwon'))  # 인수에 이름을 지정했으면 함수의 매개변수랑 이름이 같아야함
print('Ex5-5 - ', args_test('test1', 'test2', 'test3', id='admin',
                            point=7, user='kwon', password='1234'))

print()
print()

# 함수 Signatures


sg = signature(args_test)

print('Ex6-1 - ', sg)
print('Ex6-2 - ', sg.parameters)

print()

# 모든 정보 출력

for name, param in sg.parameters.items():
    # name은 POSITIONAL_OR_KEYWORD 위치가 있으면 넣어주고 아니면 키워드로 받음 기본값은 비어있음
    print('Ex6-3 - ', name, param.kind, param.default)
    # contents 는 튜플형태로 비어있음
    # 포인트는 키워드 온리 (꼭 이 키워드로 해야 받음)

# partial 사용법 : 인수 고정해서 새로운 함수를 리턴 -> 주로 특정 인수 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된(채워진) 함수의 새버전 반환
# 함수의 새 객체 타입은 이전 함수의 자체를 기술하고 있다

print()
print()


print('Ex7-1 - ', mul(100, 10))  # a*b 이런식으로 인자 2개만 방음

# 인수 고정
# 이렇게 되면 mul(5) 이런식으로 mul함수에 5를 박아놓는거임 그럼 이제 five를 인자를 하나만 받을수있음
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print('Ex7-2 - ', five(1000))
print('Ex7-3 - ', six())
print('Ex7-4 - ', [five(i) for i in range(1, 11)])  # 이렇게 하나를 박아놓고 돌아가면서 곱함
print('Ex7-5 - ', list(map(five, range(1, 11))))
