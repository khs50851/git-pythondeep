# Chapter06-4-1
# 파이썬 심화
# Asyncio
# 비동기는 기다리지 않고 바로 실행 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 후 그 지점부터 재실행 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO -> Thread
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결
# aiohttp 사용 가능(Asyncio 지원)
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio

urls = ['http://daum.net', 'https://google.com', 'https://apple.com',
        'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()


async def fetch(url,executor): # 요청도 여러번 일어나니 이렇게 바꿈
    print('Thread Name : ', threading.current_thread().getName(),
          'Start', url)  # 현재 쓰레드가 누군지

    # 일꾼 하나,처리할 url
    res = await loop.run_in_executor(executor,urlopen,url) # url 오픈자체가 블록임 동기 방식이라 응답이 올때까지 블럭됨

    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)
    return res.read()[0:5]

async def main(): # 이 메인함수가 여러번 실행되는데 이걸 비동기 처리하겠다는거
    # 쓰레기 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)


    # asyncio.ensure_future 하나의 일, 테스크를 만들어주는 함수를 씀
    futures = [asyncio.ensure_future(fetch(url,executor)) for url in urls] # 안에는 반복해서 쓸 함수를 넣음

    rst = await asyncio.gather(*futures) # 결과값을 모음

    # 결과 확인
    print()
    print('Result : ',rst)

if __name__ == '__main__':
    # 루프 생성
    loop = asyncio.get_event_loop() # 여러개의 제네레이터 함수가 있으면 지금 일하고 있는애가 일을 못하면 다음애한테 넘기고 이럼
    # 루프 대기
    loop.run_until_complete(main()) # 모든 제네레이터 함수들이 끝날때까지 기다림

    # 함수 실행
    main()

    # 완료시간 - 시작시간
    duration = timeit.default_timer()-start

    #  총 실행 시간
    print('Total Time', duration)
