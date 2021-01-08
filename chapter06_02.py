# Chapter06-2
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# yeild
# 코루틴(Coroutine)

# yield : 메인루틴과 서브루틴간에 통신을 가능하게 함
# 코루틴 제어, 코루틴 상태, 양방향 값 전송 가능
# yield from
# 메인 루틴은 위에서부터 아래로 순차적으로 실행 하나의 루트
# 서브 루틴은 원래 리턴을 통해 메인으로 돌아오는데 이런 서브 루틴을 동시에 여러개 실행할수 있게 하는게 yield임

# 서브루틴 : 메인루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스를 시작
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행을 가능하게 함 -> 동시성 사용가능
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소모 증가
# 코루틴 : 코루틴은 스케쥴링 오버헤드가 매우 적다.(하나의 쓰레드에서 실행하기 때문)

# 코루틴 예제1

from functools import wraps
from inspect import getgeneratorstate as gg


def coroutine1():
    print('>>> coroutine started.')
    i = yield  # 오른쪽에 있을땐 반환인데 왼쪽에 있을땐 메인 루틴한테 값을 받을 수 있음(양방향 통신)
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언


c1 = coroutine1()

print('Ex1-1 - ', c1, type(c1))  # 제네레이터 타입

# yield 실행 전까지 진행
# next(c1)  # started 프린트 하고 i=yield에 멈춰있음
# next(c1) # 그냥 또 하면 메인루틴에서 아무것도 받지않음 그래서 에러

# 값 전송
# send라는 메소드로 값을 전달
# c1.send(100)

# 잘못된 사용 방법
# c2 = coroutine1()

# c2.send(100)  # 제네레이터를 실행하고 값을 보내야해서 에러 next(c2)를 먼저 써줘야함

# 코루틴 예제2
# GEN_CREATED : 처음 대기 상태(next 호출 전)
# GEN_RUNNUNG : 한번이라도 next를 실행한 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태, 다시하려면 다시 선언하던지 next를 또 선언해야함


def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x+y
    print('>>> coroutine received : {}'.format(z))


c3 = coroutine2(10)


print('Ex1-2 - ', gg(c3))  # 지금은 만들어진 상태 아직 next메소드를 호출하지 않았음

print(next(c3))  # 첫줄 프린트문 출력하고 yield를 통해 x인 10을 반환을 하고 y값 받을거 대기하는중
# next를 또 그대로 호출하면 y에는 none이 들어감
print('Ex1-3 - ', gg(c3))
print(c3.send(15))  # 15를 받았고 또 yield가 실행되어 25가 반환됨 (x+y)
# print(c3.send(20))  # 마지막에 20받고 스탑이터 에러나옴

# 데코레이터 패턴
print()
print()


def coroutine(func):
    '''Decorator run until yield'''

    @wraps(func)  # 주석이나 기타 내부 어트리뷰드에 있는것을 가지고 가겠다, 싸서 가겠다
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = sumer()
print(gg(su))

print('Ex2-1 - ', su.send(100))
print('Ex2-2 - ', su.send(40))
print('Ex2-6 - ', su.send(60))

# 코루틴 예제3(예외처리)

print()
print()


class SampleException(Exception):
    '''설명에 사용할 예외 유형'''


def coroutine_except():
    print('>> coroutine started.')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing...')
            else:
                print('>>> coroutine received : {}'.format(x))
    finally:
        print('-> coroutine ending')


exe_co = coroutine_except()

print('Ex3-1 - ', next(exe_co))
print()
print('Ex3-2 - ', exe_co.send(10))
print()
print('Ex3-3 - ', exe_co.send(100))
print()
print('Ex3-4 - ', exe_co.throw(SampleException))  # 예외를 던짐
print()
print('Ex3-5 - ', exe_co.send(1009))
print('Ex3-6 - ', exe_co.close())  # GEN_CLOSE
# print('Ex3-7 - ',exe_co.send(12)) # 이미 닫혀서 안됨

print()
print()

# 코루틴 예제4(return)


def average_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total/cnt
    return 'Average : {}'.format(avg)


avger2 = average_re()
next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
    avger2.send(None)
except StopIteration as e:
    # break가 걸려서 while까지 갔다는건 리턴까지 왔다는 뜻임 그럼 더이상 아래로 코드가 없기때문에 스탑 이터레이션이 남
    print('Ex4-1 - ', e.value)
    # 근데 스탑 이터레이션이 온걸 메인루틴에서 캐치를했는데 캐치해서 안에 뭐냐고 보니까 return에 스트링 문구가 있는거임

# 코루틴 예제5(yield from)
# StopIteration 자동 처리(3.7부터 await으로 바뀜)
# 중첩 코루틴 처리


def gen1():
    for x in 'AB':
        yield x  # 처음 실행하면 여기 걸림

    for y in range(1, 4):
        yield y


print()
print()
t1 = gen1()
print(gen1)
print('Ex5-1 - ', next(t1))  # A나옴
print('Ex5-2 - ', next(t1))
print('Ex5-3 - ', next(t1))
print('Ex5-4 - ', next(t1))
print('Ex5-5 - ', next(t1))
# print('Ex5-6 - ',next(t1))

print()
print()
t2 = gen1()

print('Ex5-7 - ', list(t2))  # 이떄는 제네레이터 역할해서 전부 반환 후 리스트로 만듬

print()
print()


def gen2():
    yield from 'AB' # 위에 for문으로 쓴걸 이거 하나로 함
    yield from range(1, 4) # 처음과 끝이 뭔지 자기가 알고 언제 넥스트가 호출, 그리고 다음 문자로 뭐가 나갈지를 yield from에 위임하는거

t3 = gen2()

print('Ex6-1 - ', next(t3))  # A나옴
print('Ex6-2 - ', next(t3))
print('Ex6-3 - ', next(t3))
print('Ex6-4 - ', next(t3))
print('Ex6-5 - ', next(t3))

print()
print()

t4 = gen2()

print('Ex6-7 - ', list(t4))

print()
print()

def gen3_sub():
    print('Sub coroutine')
    x = yield 10
    print('Recv : ',str(x))
    x = yield 100
    print('Recv : ',str(x))

def gen4_sub():
    print('Sub coroutine2')
    x = yield 20
    print('Recv : ',str(x))
    x = yield 200
    print('Recv : ',str(x))

def gen4_main(): # 위임을 함
    yield from gen3_sub() # 서브루틴에 대해 코루틴을 관리하는 메소드를 만들고
    yield from gen4_sub()
    # 여기 여러개 만들고 관리 할 수 있음

t5 = gen4_main()

print('Ex7-1 - ',next(t5))
print('Ex7-2 - ',t5.send(7))
print('Ex7-3 - ',t5.send(77))
print('Ex7-4 - ',t5.send(72))