# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python object Reference

import copy
print('Ex1-1 - ')
print(dir())

# id vs __eq__ (==)증명
x = {'name': 'Kim', 'age': 33, 'city': 'Seoul'}
y = x  # 이렇게하고 y값을 수정하면 x값도 같이 수정됨

print('Ex2-1 - ', id(x), id(y))  # 같은 변수로 하나의 집을 보고 있음
print('Ex2-2 - ', x == y)  # 값이 같냐고 물어봄 트루
print('Ex2-3 - ', x is y)  # 같은 객체를 보고있냐 트루
print('Ex2-4 - ', x, y)
x['class'] = 10
print('Ex2-5 - ', x, y)

print()
print()

z = {'name': 'Kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('Ex2-6 - ', x, z)
print('Ex2-7 - ', x is z)  # 아이디 값이 다름 false
print('Ex2-8 - ', x is not z)
print('Ex2-9 - ', x == z)  # 이건 값이 같으니 트루

# 객체 생성 후 완전 불변 -> 즉, is는 id값 객체 주소(정체성)비교, ==(__eq__)는 값 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('Ex3-1 - ', id(tuple1), id(tuple2))
print('Ex3-2 - ', tuple1 is tuple2)
print('Ex3-3 - ', tuple1 == tuple2)
print('Ex3-4 - ', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy (깊은복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)


print('Ex4-1 - ', tl1 == tl2)
print('Ex4-2 - ', tl1 is tl2)
print('Ex4-3 - ', tl1 == tl3)
print('Ex4-4 - ', tl1 is tl3)  # list라는 생성자를 이용해서 복사해서 id값은 다름

# 증명


tl1.append(1000)
tl1[1].remove(105)
print('Ex4-5 - ', tl1)
print('Ex4-6 - ', tl2)
print('Ex4-7 - ', tl3)  # 삭제까지는 되는데 1000이 어펜드가 안됐다

print()
print()

# print(id(tl1[2]))  # 튜플 주소 출력
tl1[1] += [110, 120]
tl2[2] += (110, 120)

print('Ex4-8 - ', tl1)
# 튜플 재 할당 (객체 새로 생성) 원래 (5,10,15) 이부분의 id가 777이었다면 내부적으로 (110,120)를 합산해서 새로운 id를 만듬
print('Ex4-9 - ', tl2)
print('Ex4-10 - ', tl3)
# print(id(tl1[2]))  # 튜플 주소 출력 (tl2[2]+=(110, 120) 이거때문에 바뀜)

print()
print()

# Deep Copy

# 장바구니


class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


basket1 = Basket(['Apple', 'Bag', 'Tv', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)


# 2는 얕은복사 인스턴스는 다른 id가 복사되는데 실제 안에 값은 같은 id값을 가짐
print('Ex5-1 - ', id(basket1), id(basket2), id(basket3))
print('Ex5-2 - ', id(basket1._products), id(basket2._products),
      id(basket3._products))  # 싶은 복사는 인스턴스 안에 있는 속성 값들도 다 다른 id로 복사함

print()
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')
print('Ex5-3 - ', basket1._products)
print('Ex5-4 - ', basket2._products)  # 같은 객체, list를 참조하기 때문에 같이 작업이 이루어짐
print('Ex5-5 - ', basket3._products)  # 깊은복사라 영향을 받지 않음

print()
print()

# 함수 매개변수 전달


def mul(x, y):
    x += y
    return x


x = 10
y = 5

print('Ex6-1 - ', mul(x, y), x, y)  # 원본데이터 x=10은 변경되지 않음
print()

a = [10, 100]
b = [5, 10]

# 가변형 a -> 데이터 변경 , 원본의 주소를 넘겨서 수정되는 값이 원본에도 적용이 되는거
print('Ex6-2 - ', mul(a, b), a, b)  # 리스트끼리 더하면 확장됨 # 원본인 a는 변경됨 (확장됐음)

c = (10, 100)
d = (5, 10)

print('Ex6-3 - ', mul(c, d), c, d)  # 튜플은 불변형이어서 c는 원본이 확장되지 않음

# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본생성 x -> 바로 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('Ex7-1 - ', tt1 is tt2, id(tt1), id(tt2))  # 같은 id 값
print('Ex7-2 - ', tt3 is tt1, id(tt3), id(tt1))  # 같은 id 값 어떻게 복사를 하든 같음

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('Ex7-3 - ', tt4 is tt5, tt4 == tt5,
      id(tt4), id(tt5))  # 다른 변수에 할당했는데도 같은 id
print('Ex7-4 - ', ss1 is ss2, ss1 == ss2, id(ss1),
      id(ss2))  # 이것도 마찬가지 아에 똑같은 값이니 같은 곳을 바라보고 있음
