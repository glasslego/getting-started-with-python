# 모듈 변수
PI = 3.14159
VERSION = "1.0"


def add(a, b):
    """덧셈 함수"""
    return a + b


def subtract(a, b):
    """뺄셈 함수"""
    return a - b


def multiply(a, b):
    """곱셈 함수"""
    return a * b


def divide(a, b):
    """나눗셈 함수"""
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다!"


if __name__ == "__main__":
    print("계산기 모듈이 직접 실행되었습니다!")
    print(f"버전: {VERSION}")
    print(f"2 + 3 = {add(2, 3)}")
