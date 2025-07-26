import itertools
import random
import re
import shutil
from collections import Counter, namedtuple
from datetime import datetime, timedelta
from pathlib import Path


# 7.1 주요 내장 함수
def chap7_1_built_in_functions():
    """주요 내장 함수 예제를 실행하는 함수"""
    print("--- 7.1 주요 내장 함수 ---")

    # 7.1.1 기본 내장 함수
    print("\n--- 7.1.1 기본 내장 함수 ---")
    numbers = [1, 2, 3, 4, 5]
    print(f"abs(-5) = {abs(-5)}")
    print(f"round(3.14159, 2) = {round(3.14159, 2)}")
    print(f"len({numbers}) = {len(numbers)}")
    print(f"sum({numbers}) = {sum(numbers)}")
    print(f"sorted({numbers}, reverse=True) = {sorted(numbers, reverse=True)}")

    # 7.1.2 고급 내장 함수
    print("\n--- 7.1.2 고급 내장 함수 ---")
    squares = list(map(lambda x: x**2, numbers))
    print(f"map 결과: {squares}")
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter 결과: {evens}")


# 7.2 중요한 표준 라이브러리
def chap7_2_standard_libraries():
    """중요한 표준 라이브러리 예제를 실행하는 함수"""
    print("\n--- 7.2 중요한 표준 라이브러리 ---")

    # 7.2.1 collections 모듈
    print("\n--- 7.2.1 collections 모듈 ---")
    word_count = Counter(["apple", "banana", "apple"])
    print(f"Counter('apple'): {word_count['apple']}")
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print(f"namedtuple Point: x={p.x}, y={p.y}")

    # 7.2.2 itertools 모듈
    print("\n--- 7.2.2 itertools 모듈 ---")
    items = ["A", "B", "C"]
    combos = list(itertools.combinations(items, 2))
    print(f"itertools combinations: {combos}")
    perms = list(itertools.permutations(items, 2))
    print(f"itertools permutations: {perms}")

    # 7.2.3 datetime 모듈
    print("\n--- 7.2.3 datetime 모듈 ---")
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    print(f"오늘: {now.strftime('%Y-%m-%d')}")
    print(f"내일: {tomorrow.strftime('%Y-%m-%d')}")

    # 7.2.4 re 모듈 (정규표현식)
    print("\n--- 7.2.4 re 모듈 ---")
    text = "전화번호: 010-1234-5678"
    phone_match = re.search(r"\d{3}-\d{4}-\d{4}", text)
    if phone_match:
        print(f"찾은 전화번호: {phone_match.group()}")

    # 7.2.5 random 모듈
    print("\n--- 7.2.5 random 모듈 ---")
    fruits = ["apple", "banana", "orange"]
    print(f"랜덤 선택: {random.choice(fruits)}")
    random.shuffle(fruits)
    print(f"섞인 후: {fruits}")

    # 7.2.6 pathlib 모듈
    print("\n--- 7.2.6 pathlib 모듈 ---")
    path = Path("test_dir") / "test_file.txt"
    path.parent.mkdir(exist_ok=True)
    path.write_text("pathlib 테스트", encoding="utf-8")
    print(f"파일 생성: {path}, 내용: '{path.read_text(encoding='utf-8')}'")
    # 생성된 파일 및 디렉토리 정리
    shutil.rmtree(path.parent)
    print(f"디렉토리 삭제: {path.parent}")


# 메인 함수 정의
def main():
    print("### Chap07: 내장 함수와 표준 라이브러리 예제 실행 ###")
    chap7_1_built_in_functions()
    chap7_2_standard_libraries()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
