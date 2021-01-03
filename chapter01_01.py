# Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender': 'Male'},
    {'score1': 95},
    {'score2': 88}
]

# 학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender': 'Male'},
    {'score1': 20},
    {'score2': 48}
]

# 학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender': 'FeMale'},
    {'score1': 100},
    {'score2': 55}
]

# 리스트 구조
# 관리 불편
# 데이터의 정확한 위치(인덱스 매핑 필요)
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender': 'Male', 'score1': 95, 'score2': 88},
    {'gender': 'Male', 'score1': 20, 'score2': 48},
    {'gender': 'FeMale', 'score1': 100, 'score2': 55}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()
# 딕셔너리 구조
# 코드 반복 지속, 중첩문제
student_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1,
        'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2,
     'student_detail': {'gender': 'Male', 'score1': 77, 'score2': 92}},
    {'student_name': 'Park', 'student_number': 3, 'student_grade': 4,
     'student_detail': {'gender': 'FeMale', 'score1': 99, 'score2': 100}}
]

del student_dicts[1]
print(student_dicts)
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

print()


class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):  # 개발할때 참고하려고 str 메소드를 오버라이드 (어떤건지 파악하는 용도)
        return 'str : 이름 :  {} 번호 : {}'.format(self._name, self._number)

    def __repr__(self):  # str이 있으면 str을 먼저 호출
        return 'repr : {} - {}'.format(self._name, self._number)


st1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88})
st2 = Student('Lee', 2, 2, {'gender': 'Male', 'score1': 100, 'score2': 38})
st3 = Student('Park', 3, 4, {'gender': 'FeMale', 'score1': 55, 'score2': 78})

print(st1.__dict__)

students_list = []
students_list.append(st1)
students_list.append(st2)
students_list.append(st3)

print()
print(students_list)

print()
print()
for x in students_list:
    print(repr(x))  # 강제로 repr 호출
    print(x)
