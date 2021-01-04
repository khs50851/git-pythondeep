# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 기본 인스턴스 메소드

class Student(object):
    """
    Student Class
    Author : Kwon
    Date : 2021-01-04
    Description : Class,Static, Instance Method
    """

    # Class Variable
    tuition = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    # self라는 인자를 통해 어떤 결과를 리턴하는걸 인스턴스 메소드라고 함

    def full_name(self):
        return '{},{}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa
                                                                     )

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition)

    # Instance Method
    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)

    # Class Methid
    @classmethod  # 데코레이터로써 @로 파이썬 엔진한테 알려줌(클래스 메소드야라는 뜻으로)
    def raise_fee(cls, per):  # 클래스 메소드는 공용임(자바로 치면 static)
        if per <= 1:
            print('Please Enter 1 or More')
            return
        # cls는 Student랑 똑같음
        cls.tuition = per
        print('Succeed! tuition increased')

    # Class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, Student.tuition*tuition, gpa)

    # Static method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a Scholarship recipient.'


st1 = Student(1, 'Kim', 'Sarang', 'st1@naver.com', '1', 400, 3.5)
st2 = Student(2, 'Lee', 'Jungho', 'st2@daum.net', '2', 500, 4.3)

# str 메소드 만들어놓으면 이렇게만 해도 간단하게 정보 출력
print(st1)
print(st2)
# print(st1.__dict__)
# print(st2.__dict__)

print()

# 전체 정보
print(st1.detail_info())
print(st2.detail_info())

# 학비 정보(인상 전)
print(st1.get_fee())
print(st2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
# Student.tuition = 1.2

Student.raise_fee(1.2)  # 메소드를 통해 호출

# 학비 정보 (인상 후)
print(st1.get_fee_culc())
print(st2.get_fee_culc())

# 모든 인스턴스가 공통으로 접근하는 클래스 객체를 활용해 사용하는 메소드들은
# 클래스 데코레이터를 붙여주고 메소드를 정의하면됨(첫번째 인자로는 클래스 자체가 넘어옴)

print()
# 클래스 메소드 인스턴스 생성 실습
st3 = Student.student_const(3, 'Park', 'Minji', 'st3@gmail.com', '3', 550, 4.5)
st4 = Student.student_const(4, 'Cho', 'Sujin', 'st4@gmail', '4', 600, 4.1)
print(st3.detail_info())
print(st4.detail_info())
print()

# 학생 학비 변경
print(st3._tuition)
print(st4._tuition)
print()

# 장학금 혜택 여부(스태틱 메소드 미사용)


def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'


print(is_scholarship(st1))
print(is_scholarship(st2))
print(is_scholarship(st3))
print(is_scholarship(st4))

print('-------')
# 장학금 혜택 여부(스태틱 메소드 호출)
print(Student.is_scholarship_st(st1))
print(Student.is_scholarship_st(st2))
print(Student.is_scholarship_st(st3))
print(Student.is_scholarship_st(st4))

print('-------')
print('-------')
print(st3.is_scholarship_st(st3))  # 이렇게도 가능
