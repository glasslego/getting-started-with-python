"""
*args와 **kwargs란?
- *args: 여러 개의 값을 한꺼번에 받는 방법 (튜플)
- **kwargs: 이름=값 형태를 여러 개 받는 방법 (딕셔너리)
- 함수에 몇 개의 인수가 올지 모를 때 사용!

호출할 때:
  함수(*리스트)     → 리스트를 풀어서 전달
  함수(**딕셔너리)  → 딕셔너리를 풀어서 전달
"""


def add_two_numbers(a, b):
    """두 숫자만 더할 수 있는 함수"""
    return a + b


def add_many_numbers(*args):
    """몇 개든 숫자를 더할 수 있는 함수"""
    print(f"받은 인수들: {args}")
    print(f"args의 타입: {type(args)}")

    total = 0
    for number in args:
        total += number
    return total


def add_example():
    print(f"add_two_numbers(1, 2) = {add_two_numbers(1, 2)}")
    print()
    print("*args 사용 예제:")
    print(f"add_many_numbers(1) = {add_many_numbers(1)}")
    print(f"add_many_numbers(1, 2) = {add_many_numbers(1, 2)}")
    print(f"add_many_numbers(1, 2, 3) = {add_many_numbers(1, 2, 3)}")
    print(f"add_many_numbers(1, 2, 3, 4, 5) = {add_many_numbers(1, 2, 3, 4, 5)}")
    print()


def introduce_person(**kwargs):
    """사람 소개 함수"""
    print(f"   받은 정보: {kwargs}")
    print(f"   kwargs의 타입: {type(kwargs)}")

    print("   자기소개:")
    for key, value in kwargs.items():
        print(f"     {key}: {value}")


def kwargs_example():
    print("**kwargs 사용 예제:")
    introduce_person(name="홍길동", age=30, job="개발자")
    introduce_person(name="이순신", age=45, job="장군", hobby="낚시")
    introduce_person(name="세종대왕", age=50, job="왕", country="조선")
    print()


def flexible_function(*args, **kwargs):
    """뭐든 받을 수 있는 유연한 함수"""
    print("📦 받은 일반 인수들 (args):")
    for i, arg in enumerate(args):
        print(f"   {i + 1}번째: {arg}")

    print("🏷️  받은 키워드 인수들 (kwargs):")
    for key, value in kwargs.items():
        print(f"   {key} = {value}")

def flexible_example():
    print("유연한 함수 사용 예제:")
    flexible_function(1, 2, 3, name="홍길동", age=30)
    flexible_function("사과", "바나나", fruit="딸기", color="빨강")
    flexible_function(10, 20, 30, 40, 50, key1="value1", key2="value2")
    print()


# 실제 사용 예시
def order_food(customer_name, *foods, **details):
    """음식 주문 함수"""
    print(f"👤 고객: {customer_name}")  # 필수 매개변수

    print("🍽️  주문 음식:")
    for i, food in enumerate(foods, 1):  # *args
        print(f"   {i}. {food}")

    print("📋 주문 정보:")
    for key, value in details.items():  # **kwargs
        print(f"   {key}: {value}")
    print()


if __name__ == '__main__':
    add_example()
    kwargs_example()
    flexible_example()
    order_food("철수", "피자", "치킨", 주소="서울", 전화="010-1234-5678")
