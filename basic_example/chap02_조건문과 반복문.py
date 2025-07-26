# 2.1 조건문 (if, elif, else)
def chap2_1_conditional_statements():
    """조건문 관련 예제를 실행하는 함수"""
    print("--- 2.1 조건문 (if, elif, else) ---")

    # 2.1.1 기본 if문
    age = 18
    if age >= 18:
        print("성인입니다.")
    else:
        print("미성년자입니다.")

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

    # 2.1.2 체인 비교
    age = 25
    print(f"25세는 18세와 65세 사이인가? {18 <= age <= 65}")

    # 2.1.4 멤버십 연산자
    fruits = ["apple", "banana", "orange"]
    if "apple" in fruits:
        print("사과가 있습니다.")

    # 2.1.5 삼항 연산자
    status = "성인" if age >= 18 else "미성년자"
    print(f"20세는 {status}입니다.")


# 2.2 반복문
def chap2_2_loops():
    """반복문 관련 예제를 실행하는 함수"""
    print("\n--- 2.2 반복문 ---")

    # 2.2.1 for 루프
    fruits = ["apple", "banana", "orange"]
    print("과일 목록:")
    for fruit in fruits:
        print(f"- {fruit}")

    print("range() 함수 사용 (1부터 5까지):")
    for i in range(1, 6):
        print(i, end=" ")
    print()  # 줄바꿈

    # 2.2.2 while 루프
    count = 0
    print("while 루프 (0부터 4까지):")
    while count < 5:
        print(f"카운트: {count}")
        count += 1

    # while-else (break로 중단되지 않을 때 실행)
    num = 3
    print("while-else 카운트다운:")
    while num > 0:
        print(num)
        num -= 1
    else:
        print("카운트다운 완료!")

    # 2.2.3 반복문 제어
    print("break 예제 (5에서 중단):")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()

    print("continue 예제 (짝수 건너뛰기):")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()


# 메인 함수 정의
def main():
    print("### Chap02: 조건문과 반복문 예제 실행 ###")
    chap2_1_conditional_statements()
    chap2_2_loops()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
