import unittest

# --- 테스트 대상 함수 및 클래스 ---


def add(a, b):
    """두 수를 더합니다."""
    return a + b


def divide(a, b):
    """나눗셈을 수행합니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


def is_even(number):
    """숫자가 짝수인지 확인합니다."""
    return number % 2 == 0


class Calculator:
    """간단한 계산기 클래스"""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def get_history(self):
        return self.history.copy()


# --- 테스트 코드 ---


# 9.1 단위 테스트 (unittest)
def chap9_1_unittest():
    """unittest를 사용한 기본 테스트 예제를 실행하는 함수"""
    print("--- 9.1 단위 테스트 (unittest) ---")

    # 단위 테스트 클래스 정의
    class TestMathFunctions(unittest.TestCase):
        """수학 함수들에 대한 테스트"""

        def test_add_positive_numbers(self):
            self.assertEqual(add(2, 3), 5)

        def test_divide_by_zero(self):
            with self.assertRaises(ValueError):
                divide(10, 0)

    class TestCalculator(unittest.TestCase):
        """계산기 클래스 테스트"""

        def setUp(self):
            self.calc = Calculator()

        def test_calculator_add(self):
            result = self.calc.add(5, 3)
            self.assertEqual(result, 8)

        def test_history_tracking(self):
            self.calc.add(2, 3)
            self.assertIn("2 + 3 = 5", self.calc.get_history())

    # 테스트 실행
    print("TestMathFunctions 실행:")
    suite_math = unittest.TestLoader().loadTestsFromTestCase(TestMathFunctions)
    unittest.TextTestRunner().run(suite_math)

    print("\nTestCalculator 실행:")
    suite_calc = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner().run(suite_calc)


# 9.2 pytest를 사용한 테스트 (개념 설명)
def chap9_2_pytest_concepts():
    """pytest의 주요 개념을 설명하는 함수"""
    print("\n--- 9.2 pytest를 사용한 테스트 (개념) ---")
    print("pytest는 'test_'로 시작하는 함수와 파일을 자동으로 찾아 실행합니다.")
    print(
        "별도의 파일(예: test_chap09.py)에 아래와 같이 작성하고 터미널에서 'pytest'를 실행합니다.\n"
    )

    pytest_code = """
# test_chap09.py
import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
"""
    print("--- pytest 코드 예시 ---")
    print(pytest_code)
    print("----------------------")


# 메인 함수 정의
def main():
    print("### Chap09: 테스트 예제 실행 ###")
    chap9_1_unittest()
    chap9_2_pytest_concepts()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
