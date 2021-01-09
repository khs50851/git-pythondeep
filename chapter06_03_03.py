# Chapter06-3-1
# 파이썬 심화
# Future 동시성
# 비동기 작업 실행
# 지연시간(Block)(여러쓰레드가 움직이더라도 블럭이 걸리면 운영체제가 관여해서 멈추게됨) CPU 및 리소스 낭비 방지 -> Network I/O 관련 작업 동시성 활용 권장
# 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상


# 실습 대상 3가지 경우

# 순차 실행
# concurrent.futures 방법1
# concurrent.futures 방법2


import os
import time
import sys
import csv
from concurrent import futures

# concurrent.future 방법1(ThreadPoolExecutor, ProcessPoolExecutor)
# map()
# 서로 다른 스레드 또는 프로세스에서 실행 가능
# 내부 과정을 알 필요 없으며, 고수준으로 인터페이스 제공 -> 퓨쳐에서


# 순차 실행 예제

# Google Python GIL(Global Interpareter Lock)
# GIL은 한 번에 하나의 스레드만 수행 할 수 있게 인터프리터 자체에서 LOCK을 거는 것. 이렇게 하는게 안전하기 때문에(스레드간 충돌 방지, 병목현상, 무한루프 등 방지)


# 국가정보
NATION_LS = (
    'Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()

# 초기 CSV 위치
TARGET_CSV = 'C:/python2/resources/nations.csv'

# 저장 폴더 위치
DEST_DIR = 'C:/python2/csvs'

# CSV헤더 기초정보
HEADER = ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority', 'Order Date', 'Order ID',
          'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']

# 국가별 CSV 파일 저장


def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w', newline='') as fp:  # newline은 줄바꿈 방지
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()  # 헤더만 먼저 씀
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)


# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)  # 32만개 파일을 읽음
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # OrderedDIct 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data

# 중간 상황 출력


def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()

# 국가별 분리 함수 실행


def separate_many(nt):
    # 리스트가 하나하나 들어가서 포문 필요없음
    # 분리 데이터
    data = get_sales_data(nt)

    # 상황 출력
    show(nt)
    # 파일 저장
    save_csv(data, nt.lower()+'.csv')
    return len(nt)

# 시간 측정 및 메인 함수


def main(separate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))  # 둘중에 작은 값을 꺼내라 9개 또는 20개중 작은것이 나오니 9 반환

    # 시작 시간
    start_tm = time.time()

    # futures
    futures_list = []  # 일꾼들을 모을리스트

    # 결과 건수 # 지금까진 하나씩 읽고 쓰기했는데 이제 동시에 해보자
    # 첫번째는 몇개의 일꾼을 사용할거야라는 매개변수

    # ThreadPoolExcutor(worker) : GIL에 종속
    # ProcessPoolExcutor(이건 여기 워커 안넣음) : GIL우회 CPU로 작동, 변경 후 -> CPU사용률 엄청 올라감 os.cpu_count() 내부적으로 cpu코어를 가져와서 사용
    with futures.ThreadPoolExecutor(worker) as executor:

        # map -> 작업 순서 유지, 즉시 실행 즉 이 세퍼레이터 함수가 9개가 풀려버리게됨
        # Submit -> Callable 객체 스케쥴링(실행 예약) > Future
        # Future ->result() 각각의 결과값, done() 각각의 일꾼들이 일을 잘 했는지, as_complete() 일꾼들이 일이 끝날때까지 기다림, 주로 사용
        for nt in sorted(NATION_LS):
            # future 반환
            future = executor.submit(separate_many, nt)  # 실행할 함수랑 국가코드 넣으면 됨
            # 스케쥴링
            futures_list.append(future)
            # 출력1
            # print('Scheduled for {} : {}'.format(nt, future))
            # print()

        for future in futures.as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled
            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm

    msg = '\n csv separated in {:.2f}s'

    # 최종 결과 출력
    print(msg.format(end_tm))


# def separate_many()


# 실행
if __name__ == '__main__':
    main(separate_many)
