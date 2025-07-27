# 4.1 클래스 기초
def chap4_1_class_basics():
    """클래스 정의, 객체 생성, 클래스/정적 메서드 예제를 실행하는 함수"""
    print("--- 4.1 클래스 기초 ---")

    # 4.1.1 클래스 정의와 객체 생성
    class Person:
        species = "Homo sapiens"

        def __init__(self, name:str, age:int):
            self.name = name
            self.age = age

        def introduce(self):
            return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."

        def have_birthday(self):
            self.age += 1
            print(f"{self.name}의 나이가 {self.age}세가 되었습니다.")

    person1 = Person("Alice", 25)
    print(person1.introduce())
    print(person1.species)
    person1.have_birthday()
    print(f"종: {Person.species}")

    # 4.1.2 클래스 메서드와 정적 메서드
    class MathUtils:
        pi = 3.14159

        @classmethod
        def circle_area(cls, radius):
            return cls.pi * radius**2

        @staticmethod
        def add(a, b):
            return a + b

    print(f"반지름 5인 원의 넓이: {MathUtils.circle_area(5)}")
    print(f"3 + 4 = {MathUtils.add(3, 4)}")


# 4.2 상속
def chap4_2_inheritance():
    """상속, 다중 상속, 다형성 예제를 실행하는 함수"""
    print("\n--- 4.2 상속 ---")

    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "멍멍!"

    class Cat(Animal):
        def speak(self):
            return "야옹!"

    # 다형성
    animals = [Dog("바둑이"), Cat("나비")]
    for animal in animals:
        print(f"{animal.name}: {animal.speak()}")

    # 다중 상속
    class Flyable:
        def fly(self):
            return "날고 있습니다."

    class Duck(Animal, Flyable):
        def speak(self):
            return "꽥꽥!"

    duck = Duck("도날드")
    print(f"{duck.name}: {duck.speak()}, {duck.fly()}")


# 4.3 캡슐화
def chap4_3_encapsulation():
    """접근 제어자, 프로퍼티 예제를 실행하는 함수"""
    print("\n--- 4.3 캡슐화 ---")

    class BankAccount:
        def __init__(self, owner, initial_balance=0):
            self.owner = owner
            self._balance = initial_balance

        def get_balance(self):
            return self._balance

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount

    account = BankAccount("Alice", 1000)
    account.deposit(500)
    print(f"{account.owner}님의 잔액: {account.get_balance()}")

    # 프로퍼티
    class Temperature:
        def __init__(self):
            self._celsius = 0

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("절대영도보다 낮을 수 없습니다.")
            self._celsius = value

        @property
        def fahrenheit(self):
            return (self._celsius * 9 / 5) + 32

    temp = Temperature()
    temp.celsius = 25
    print(f"섭씨: {temp.celsius}°C, 화씨: {temp.fahrenheit}°F")


# 4.4 특수 메서드 (매직 메서드)
def chap4_4_special_methods():
    """연산자 오버로딩 등 특수 메서드 예제를 실행하는 함수"""
    print("\n--- 4.4 특수 메서드 (매직 메서드) ---")

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Vector({self.x}, {self.y})"

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"{v1} + {v2} = {v1 + v2}")


# 메인 함수 정의
def main():
    print("### Chap04: 클래스와 객체 지향 프로그래밍 예제 실행 ###")
    chap4_1_class_basics()
    chap4_2_inheritance()
    chap4_3_encapsulation()
    chap4_4_special_methods()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
