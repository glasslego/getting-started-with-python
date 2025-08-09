"""
🔹 모듈 = 하나의 .py 파일
🔹 패키지 = 여러 모듈을 담은 폴더 (__init__.py 필요)
🔹 import로 모듈/패키지 가져오기
🔹 from ... import ...로 특정 함수만 가져오기
🔹 as로 별명 사용 가능
"""

from my_package.calculator import multiply


def my_multiply(a, b):
    """곱셈 함수"""
    return multiply(a, b)


if __name__ == "__main__":
    print("계산기 모듈을 사용합니다.")
    result = my_multiply(5, 10)
    print(f"5 * 10 = {result}")
