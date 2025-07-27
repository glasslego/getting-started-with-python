# control_flow_examples.py


def demonstrate_conditionals():
    """2.1 조건문 (if, elif, else) 예제를 실행하는 함수"""
    print("=" * 20)
    print(" 2.1 조건문 예제 시작 ")
    print("=" * 20)

    # 2.1.1 기본 if문
    print("\n--- 2.1.1 기본 if문 ---")
    age = 18
    if age >= 18:
        print("성인입니다.")
    else:
        print("미성년자입니다.")

    # 다중 조건
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"점수: {score}, 등급: {grade}")

    # 2.1.2 비교 연산자
    print("\n--- 2.1.2 비교 연산자 ---")
    x = 10
    y = 20
    print(f"{x} == {y} : {x == y}")
    print(f"{x} != {y} : {x != y}")
    print(f"{x} < {y} : {x < y}")
    print(f"{x} <= {y} : {x <= y}")
    print(f"{x} > {y} : {x > y}")
    print(f"{x} >= {y} : {x >= y}")

    # 체인 비교
    age_check = 25
    print(f"18 <= {age_check} <= 65 : {18 <= age_check <= 65}")

    # 2.1.3 논리 연산자
    print("\n--- 2.1.3 논리 연산자 ---")
    age = 25
    has_license = True
    # and: 둘 다 True여야 True
    if age >= 18 and has_license:
        print("운전 가능")

    # or: 하나라도 True면 True
    weekend = True
    holiday = False
    if weekend or holiday:
        print("쉬는 날")

    # not: 반대
    is_working = False
    if not is_working:
        print("일하지 않는 중")

    # 2.1.4 멤버십 연산자
    print("\n--- 2.1.4 멤버십 연산자 ---")
    fruits = ["apple", "banana", "orange"]
    if "apple" in fruits:
        print("사과가 있습니다.")
    if "grape" not in fruits:
        print("포도가 없습니다.")

    text = "Python Programming"
    if "Python" in text:
        print("Python이 포함되어 있습니다.")

    # 2.1.5 삼항 연산자 (조건부 표현식)
    print("\n--- 2.1.5 삼항 연산자 ---")
    age = 20
    status = "성인" if age >= 18 else "미성년자"
    print(f"age가 {age}일 때, status는? {status}")

    def get_abs(x):
        return x if x >= 0 else -x

    print(f"get_abs(-5)의 결과: {get_abs(-5)}")
    print("-" * 20 + "\n")


def demonstrate_loops():
    """2.2 반복문 예제를 실행하는 함수"""
    print("=" * 20)
    print(" 2.2 반복문 예제 시작 ")
    print("=" * 20)

    # 2.2.1 for 루프
    print("\n--- 2.2.1 for 루프 ---")
    fruits = ["apple", "banana", "orange"]
    print("리스트 반복:")
    for fruit in fruits:
        print(f"과일: {fruit}")

    print("\nrange() 함수 사용:")
    for i in range(5):
        print(i, end=" ")
    print()

    print("\nenumerate() 사용 (인덱스와 값):")
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")

    print("\n딕셔셔리 반복:")
    person = {"name": "Alice", "age": 25, "city": "Seoul"}
    for key, value in person.items():
        print(f"{key}: {value}")

    print("\nzip() 함수 (여러 리스트 동시 반복):")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name}: {age}세")

    # 2.2.2 while 루프
    print("\n--- 2.2.2 while 루프 ---")
    print("기본 while문:")
    count = 0
    while count < 5:
        print(f"카운트: {count}")
        count += 1

    print("\n무한 루프 (주석 처리됨):")
    # 아래 코드는 사용자의 입력을 기다리므로 자동 실행을 위해 주석 처리합니다.
    # while True:
    #     user_input = input("종료하려면 'quit' 입력: ")
    #     if user_input == "quit":
    #         break
    #     print(f"입력값: {user_input}")

    print("while-else:")
    num = 5
    while num > 0:
        print(num, end=" ")
        num -= 1
    else:
        print("\n카운트다운 완료!")

    # 2.2.3 반복문 제어 (break, continue)
    print("\n--- 2.2.3 반복문 제어 ---")
    print("break 예제 (0~4 출력):")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()

    print("continue 예제 (홀수만 출력):")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    print("중첩 루프에서 break:")
    for i in range(3):
        for j in range(3):
            if j == 1:
                break  # 안쪽 루프만 종료
            print(f"i: {i}, j: {j}")

    # 2.2.4 리스트 컴프리헨션
    print("\n--- 2.2.4 리스트 컴프리헨션 ---")
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"제곱 결과: {squares}")

    evens = [x for x in range(10) if x % 2 == 0]
    print(f"짝수 리스트: {evens}")

    matrix = [[i * j for j in range(3)] for i in range(3)]
    print(f"중첩 루프 행렬: {matrix}")

    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(i * j)
        matrix.append(row)
    print(f"중첩 루프 행렬: {matrix}")

    word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
    print(f"딕셔너리 컴프리헨션: {word_lengths}")

    unique_lengths = {len(word) for word in ["apple", "banana", "orange", "grape"]}
    print(f"집합 컴프리헨션: {unique_lengths}")
    print("-" * 20 + "\n")


def main():
    """메인 함수: 모든 예제 함수를 순차적으로 호출"""
    demonstrate_conditionals()
    demonstrate_loops()
    print("모든 예제 실행 완료.")


# 이 파일이 직접 실행될 때만 main() 함수를 호출
if __name__ == "__main__":
    main()
