# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class
    Author : Kwon
    Date : 2021-01-03
    """

    # 클래스 변수
    student_count = 0  # 스코프라는건 이 클래스의 위쪽 영역을 말함

    def __init__(self, name, number, grade, details, email=None):
        # 셀프가 붙는것들이 인스턴수 변수임
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str : {}'.format(self._name)

    def __repr__(self):
        return 'repr : {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(
            self._name, self._email, self._details))

    def __del__(self):  # 오버라이딩
        Student.student_count -= 1


# Self 의미
st1 = Student('Cho', 1, 3, {'gender': 'Male',
                            'score1': 12, 'score2': 32}, 'anawq@naver.com')
st2 = Student('Chang', 2, 1, {'gender': 'Male', 'score1': 53, 'score2': 69})

# print(st1.detail_info())
# print(st2.detail_info())

# print(st1._name == st2._name)  # 값을 비교
a = 'ABC'
b = a
# print(st1 is st2)  # id값 비교 레퍼런스 레이블 비교시 사용
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# dir & __dict__ 확인
# print(dir(st1))
# print(st1.__dict__)

# Doctring
# print(Student.__doc__)  # 주석 확인

# 실행
# st1.detail_info()

# 에러
# Student.detail_info()

# 이렇게 직접 객체를 넣어주면 됨
# Student.detail_info(st1)

# 비교
# print(st1.__class__, st2.__class__)  # 원형이 뭐냐, 부모를 알려줌
# print(id(st1.__class__), id(st2.__class__))

# 인스턴수 변수
# 직접 접근(PEP 문법적으로 권장 x)
# 이런식으로 임의로 바꿔버릴수가 있음
# st1._name = 'aaa'
# print(st1._name)

# 클래스변수
# 접근
# print(st1.student_count)
# print(st2.student_count)
# print(Student.student_count)

# 공유 확인
# print(Student.__dict__)
# print(st1.__dict__)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스변수까지 알아서 찾아봄))

del st2
print(st1.student_count)
print(Student.student_count)
