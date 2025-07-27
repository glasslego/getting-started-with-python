# import datetime
import importlib
import os
import random

import math_utils

from datetime import datetime


# 5.1 모듈
def chap5_1_modules():
    """모듈 생성, import, 내장 모듈 사용 예제를 실행하는 함수"""
    print("--- 5.1 모듈 ---")

    # 5.1.1 모듈 생성과 import (가상으로 math_utils.py 파일 생성)
    # 실제로는 별도의 파일로 존재해야 합니다.
    math_utils_code = """
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
PI = 3.14159
"""
    with open("math_utils.py", "w", encoding="utf-8") as f:
        f.write(math_utils_code)

    # 1. 전체 모듈 import

    print(f"import math_utils -> math_utils.add(3, 4) = {math_utils.add(3, 4)}")

    # 2. 특정 함수만 import
    from math_utils import PI, multiply

    print(
        f"from math_utils import multiply, PI -> multiply(5, 6) = {multiply(5, 6)}, PI = {PI}"  # noqa: E501
    )

    # 5.1.2 내장 모듈 사용
    print("\n--- 내장 모듈 사용 ---")
    # datetime 모듈
    now = datetime.datetime.now()
    print(f"datetime.now(): {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # random 모듈
    print(f"random.randint(1, 10): {random.randint(1, 10)}")

    # os 모듈
    print(f"os.getcwd(): {os.getcwd()}")

    # 생성했던 가상 모듈 파일 삭제
    os.remove("math_utils.py")


# 5.3 모듈과 패키지 고급 활용
def chap5_3_advanced_usage():
    """동적 import 등 고급 활용 예제를 실행하는 함수"""
    print("\n--- 5.3 모듈과 패키지 고급 활용 ---")

    # 5.3.1 동적 import
    module_name = "math"
    math_module = importlib.import_module(module_name)
    print(f"importlib.import_module('math') -> math.sqrt(16) = {math_module.sqrt(16)}")

    # 5.3.2 __all__ 사용 (개념 설명)
    # 실제로는 module_with_all.py 파일이 있어야 합니다.
    # from module_with_all import * 를 실행하면
    # __all__ = ['public_function', 'PublicClass'] 에 정의된 것만 import 됩니다.
    print("\n__all__은 from ... import * 사용 시 import될 대상을 지정합니다.")


# 메인 함수 정의
def main():
    print("### Chap05: 모듈과 패키지 예제 실행 ###")
    chap5_1_modules()
    chap5_3_advanced_usage()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    # main()
    # print(datetime.now())
    print(datetime.now())