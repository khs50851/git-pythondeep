# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)
# Decorator & Closure

# 파이썬 변수 범위(global)

# 예제1
import time
from dis import dis


def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5)


b = 10

# 예제2


def func_v2(a):
    print(a)
    print(b)


func_v2(5)


b = 10

# 예제3


def func_v3(a):
    print(a)
    print(b)
    b = 5  # 이 안에서 b를 찾는데 b가 프린트문보다 뒤에 할당이 되기때문에 b가 없다고 에러남
    # 같은 변수가 있을때 전역변수는 체크되지 않음


# func_v3(10)


print('Ex1-1 - ')
print(dis(func_v3))

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언 된 연결된 정보를 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 도는 메소드에 직접 접근이 가능하다

print()
print()

a = 10

print('Ex2-1 - ', a+10)
print('Ex2-2 - ', a+100)

# 결과를 누적 할 수 없을까?

print('Ex2-3 - ', sum(range(1, 51)))
print('Ex2-4 - ', sum(range(51, 101)))
# 이런 누적되는 함수를 클래스로 만들어본다면?

print()
print()

# 클래스 이용


class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print('Ex3-1 - ', avg_cls(15))
print('Ex3-2 - ', avg_cls(35))
print('Ex3-3 - ', avg_cls(40))

print()
print()

# 클로저(Closure) 사용
# 전역 변수 사용 감소
# 디자인 패턴 적용


def closure_avg1():
    # 파이썬에선 내부함수와 외부함수 사이 즉 이 공간을 뭐라고하냐면 자유 변수 영역이라고 함 (Free variable)
    # 클로저 영역
    # 아래 avg_closure1 = closure_avg1() 이렇게 하면 averager함수가 반환이 되는데 이 함수 안에는 series가 없음
    # 근데 averager 이 안에서 계속 참조를 하고 있음
    # 보통 지역변수는 사용되면 다 소멸되기 마련 근데 이 시리즈를 5번이나 사용했는데도 불구하고 참조하고 있음
    # 특징 -> 반환 당시 (반환한건 averager 요 함수인데) 이거의 유효범위를 벗어난 변수, 메소드에 접근 가능 (벗어난건 series)를 말함

    series = []

    def averager(v):
        # series = [] # 만약 이렇게 선언하면 지역변수에 있는거로 끌어다써서 변수가 유지가 되지 않음
        series.append(v)  # 안에 series가 없으면 밖에서 변수를 찾아오기때문에 사용 가능
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_avg1()

print('Ex4-1 - ', avg_closure1(15))
print('Ex4-2 - ', avg_closure1(35))
print('Ex4-3 - ', avg_closure1(40))

print()
print()

print('Ex5-1 - ', dir(avg_closure1))

print()
print()

print('Ex5-2 - ', dir(avg_closure1.__code__))

print()
print()

# 클로저 영역엔 시리즈가 들어가있음을 알 수 있음
print('Ex5-3 - ', avg_closure1.__code__.co_freevars)

print()
print()

print('Ex5-4 - ', dir(avg_closure1.__closure__[0]))

print()
print()

print('Ex5-4 - ', dir(avg_closure1.__closure__[0].cell_contents))

print()
print()

# 잘못된 클로저 사용 예


def closure_avg2():
    # Free variabel
    cnt = 0
    total = 0
    # 클로저 영역

    def averager(v):
        nonlocal cnt, total  # 아래 지역변수 cnt랑 클로저 변수 cnt랑 같은거라고 알려주는 키워드임
        cnt += 1  # 이 내부 함수이 cnt는 별개로 생각을 해야함 averager 안에 선언이 되었는데 초기화가 안되서 그럼 그래서 클로저한테 둘은 같은거라고 알려줘야함
        total += v
        print('def2 >>> {} / {}'.format(total, cnt))
        return total / cnt
    return averager


avg_closure2 = closure_avg2()

print('Ex5-5 - ', avg_closure2(15))
print('Ex5-6 - ', avg_closure2(35))
print('Ex5-7 - ', avg_closure2(40))

# 데코레이터 실습
# 1. 중복제거, 코드 간결
# 2. 클로저보다 문법 간결
# 3. 조합해서 사용하기 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함

print()
print()


def perf_clock(func1):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func1(*args)
        # 종료시간
        et = time.perf_counter() - st
        # 함수 명
        name = func1.__name__
        # 매개 변수
        arg_str = ','.join(str(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' %
              (et, name, arg_str, result))  # 걸린시간 함수이름 매개변수 결과값
        return result
    return perf_clocked


@perf_clock  # 아래 함수 실행할때 perf_clock 이거 먼저 실행해 라는 뜻임
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)

# 데코레이터 미사용


# non_deco1 = perf_clock(time_func)
# non_deco2 = perf_clock(sum_func)
# non_deco3 = perf_clock(fact_func)

# # perf_clock(func) func 매개변수가 나오는데 이건 내부 함수 안에 저장이 되어있음 스코프에 유지가 되어있음
# print('Ex7-1 - ', non_deco1, non_deco1.__code__.co_freevars)
# # 이 func함수는 time_func 이런 형태로 저장되어있는거임
# print('Ex7-2 - ', non_deco1, non_deco2.__code__.co_freevars)
# print('Ex7-3 - ', non_deco1, non_deco3.__code__.co_freevars)
# print()
# print('*' * 40, ' Called Non Deco -> time_func')
# print('Ex7-4 - ')
# non_deco1(2)

# print('*' * 40, ' Called Non Deco -> sum_func')
# print('Ex7-5 - ')
# non_deco2(100, 200, 300, 400, 500)

# print('*' * 40, ' Called Non Deco -> fact_func')
# print('Ex7-6 - ')
# non_deco3(10)

print()
print()
print()

print('*' * 40, ' Called Deco -> time_func')
print('Ex7-7 - ')
time_func(2)
print('*' * 40, ' Called Deco -> sum_func')
print('Ex7-8 - ')
sum_func(10, 20, 30, 40, 50)
print('*' * 40, ' Called Deco -> fact_func')
print('Ex7-9 - ')
fact_func(5)
