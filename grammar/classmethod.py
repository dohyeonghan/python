class Car:

    def __init__(self, body_type):
        self.body_type = body_type

    def __repr__(self):
        return f'Car{self.body_type} body type'

    def set_body_type(self, body_type):
        self.body_type = body_type

    @classmethod
    def hyundai(cls):
        return cls("sedan")


"""
    self : instance
    cls : class
"""
c = Car(body_type="sport")
c.body_type = "sedan"
print(c.body_type)
"""
    * Object와 상관없이 새로운 Class를 Object화 시킬 때 사용
    cls <- Car
    cls 파라미터에 클래스 자체
    
    언제 사용할까 
    1. 공통된 데이터 또는 동작 관리 : 클래스 자체 공통된 속성을 관리할 때
    
    2. 객체 생성에 관련된 로직을 캡슐화할때 사용
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person(cls, name, birth_year):
        age = cls.calculate_age(birth_year)
        return cls(name, age)

    @staticmethod
    def calculate_age(birth_year):
        return 2023 - birth_year


# 팩토리 메소드를 사용하여 객체 생성
person = Person.create_person("Alice", 1990)

print(f"Name: {person.name}, Age: {person.age}")  # Name: Alice, Age: 33
