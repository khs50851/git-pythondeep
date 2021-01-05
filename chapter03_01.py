# Chapter03-1
# 파이썬 심화
# 시퀀스형
# 컨테이너(Container) : 서로 다른 자료형을 저장할 수 있는거 -> 리스트, 튜플, collections.deque
# Flat : 한 개의 자료형만 저장할수있음 str,bytes,bytearray,array.array, memoryview 속도는 이게 더 빠름 자료'형'임
# 가변 뮤테이블 list, bytearray, array.array, memoryview, deque
# 불변 임뮤테이블 tuple, str, bytes

# 지능형 리스트(Comprehending Lists)

# Non Comprehending Lists

# 이걸 유니코드로 바꾸는 리스트
import array
chars = '!@#$%^&*()_+'
codes1 = []
for s in chars:
    codes1.append(ord(s))

# Comprehending Lists 일반 리스트보다 약간 속도가 빠름
codes2 = [ord(s) for s in chars]

# 예를들면 40번대 이상의 숫자만 갖다달라할때 원래 포문에 if문 넣어서 40이상숫자만 하게끔 조건 걸어야하는디
# + Map, Filter 함수
codes3 = [ord(s) for s in chars if ord(s) >= 40]
codes4 = list(filter(lambda x: x > 40, map(ord, chars)))

print('Ex1-1 - ', codes1)
print('Ex1-2 - ', codes2)
print('Ex1-3 - ', codes3)
print('Ex1-4 - ', codes4)
print('Ex1-5 - ', [chr(s) for s in codes1])
print('Ex1-5 - ', [chr(s) for s in codes2])
print('Ex1-5 - ', [chr(s) for s in codes3])
print('Ex1-5 - ', [chr(s) for s in codes4])

print()
print()
print()

# Generator 반복은 하는데 값을 생성하는


# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x) 성능이 아주 좋음
tuple_g = (ord(s) for s in chars)

# 괄호 모양이 리스트괄호가 아니라 튜플 괄호일때 안에 반복하는 구문을 쓰면
# 제네레이터가 생성됨 이때는 튜플안에 위에 리스트로 만든 값들을 생성하지 않은거
# 즉 줄만 세워놓고 입장시키지 않음 (메모리를 생성하지 않았음)
# 리스트같은경우엔 100개를 만들면 100개 다 메모리에 올리고 그럼 메모리의 사용량이 높아짐

# Array
array_g = array.array('I', (ord(s) for s in chars))  # 첫번째 인자로 자료형 타입


print('Ex2-1 - ', tuple_g)

# 값이 나오게 하려면 next라는 함수를 써야함
print('Ex2-2 - ', next(tuple_g))  # 첫번째 값인 33나옴
print('Ex2-3 - ', next(tuple_g))  # 두번째 값인 64나옴 한번에 한 개의 항목을 생성하기 때문
print('Ex2-4 - ', array_g)  # 어레이 객체가 그대로 나옴
print('Ex2-5 - ', array_g.tolist())  # 이렇게하면 리스트로 형변환됨

print()
print()
print()

# 제네레이터 예제
print('Ex3-1 - ', ('%s' % c + str(n)
                   for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print('Ex3-2 - ', s)  # next를 계속 호출해주는거

print()
print()

# 리스트 주의 할 점
marks1 = [['~']*3 for n in range(3)]
marks2 = [['~']*3] * 3

print('Ex4-1 - ', marks1)
print('Ex4-1 - ', marks2)

print()
print()
marks1[0][1] = 'X'
marks2[0][1] = 'X'
print('Ex4-3 - ', marks1)
print('Ex4-4 - ', marks2)

# 증명
print('Ex4-5 - ', [id(i) for i in marks1])  # 요소들이 서로 다른 id값을 가지고 있음
print('Ex4-6 - ', [id(i) for i in marks2])  # 요소들이 서로 같은 id값을 가지고 있음

# Tuple Advanced

# a,b = divmod(100,9)
print('Ex5-1 - ', divmod(100, 9))
# 튜플형태로 쓰면 divmod는 원래 인자 2개를 받아야하는데 튜플 하나로만 인식해서
print('Ex5-2 - ', divmod(*(100, 9)))
# 에러가 나는데 그걸 앞에 *를 붙여서 언팩킹해줌으로써 알아서 계산되게함

print('Ex5-3 - ', *(divmod(100, 9)))

print()
print()
x, y, *rest = range(10)
print('Ex5-4 - ', x, y, rest)  # rest는 리스트로 들어옴
x, y, *rest = range(2)
print('Ex5-5 - ', x, y, rest)  # 기본 리스트만 나옴
x, y, *rest = 1, 2, 3, 4, 5
print('Ex5-6 - ', x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)
l = (10, 15, 20)
m = [10, 15, 20]
print('Ex6-1 - ', l, m, id(l), id(m))

l = l*2
m = m*2
print('Ex6-2 - ', l, m, id(l), id(m))  # 저렇게 *2를 하면 변수에 새로 할당하기때문에 id도 새로 받게됨

# l[0] = 3 튜플은 수정이 안됨

l *= 2
m *= 2

# 이때 튜플은 새로 객체를 만들어서 id가 바꼈지만 리스트는 자기 리스트에 재할당
print('Ex6-3 - ', l, m, id(l), id(m))

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango',
          'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체 반환

print('Ex7-1 - ', sorted(f_list))
print('Ex7-2 - ', sorted(f_list, reverse=True))
print('Ex7-3 - ', sorted(f_list, key=len))  # 글자의 길이 순서대로 정렬
print('Ex7-4 - ', sorted(f_list, key=lambda x: x[-1]))  # 단어의 끝글자를 기준으로 정렬
print('Ex7-5 - ', sorted(f_list, key=lambda x: x[-1], reverse=True))
print('Ex7-6 - ', sorted(f_list))

# sort : 정렬 후 객체를 직접 변경
# 반환 값 확인 None -> None이 반환되면 반환되는 값이 없다는거임
a = f_list.sort()
print(a, f_list)

print('Ex7-7 - ', f_list.sort(), f_list)
print('Ex7-8 - ', f_list.sort(reverse=True), f_list)
print('Ex7-9 - ', f_list.sort(key=len), f_list)
print('Ex7-10 - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('Ex7-11 - ', f_list.sort(key=lambda x: x[-1],reverse=True), f_list)
