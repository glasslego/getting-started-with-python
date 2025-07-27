from functools import reduce


# 3.1 함수 정의와 호출
def chap3_1_definition_and_call():
    """함수 정의, 매개변수, 인수 관련 예제를 실행하는 함수"""
    print("--- 3.1 함수 정의와 호출 ---")

    # 3.1.1 기본 함수
    def greet():
        print("안녕하세요!")

    greet()

    def greet_person(name:str):
        print(f"안녕하세요, {name}님!")

    greet_person("Alice")

    def add(a:int, b:int) -> int:
        return a + b

    result = add(3, 5)
    print(f"add(3, 5)의 결과: {result}")

    # 3.1.2 매개변수와 인수
    def greet_with_default(name, greeting="안녕하세요"):
        return f"{greeting}, {name}님!"

    print(greet_with_default("Alice"))
    print(greet_with_default("Bob", "반갑습니다"))

    def flexible_func(required, *args, **kwargs):
        print(f"필수: {required}")
        print(f"추가 위치 인수: {args}")
        print(f"키워드 인수: {kwargs}")

    flexible_func("필수값", 1, 2, 3, name="Alice", age=25)


# 3.2 함수의 고급 기능
def chap3_2_advanced_features():
    """람다, 내장 함수, 스코프, 데코레이터 예제를 실행하는 함수"""
    print("\n--- 3.2 함수의 고급 기능 ---")

    # 3.2.1 람다 함수
    square = lambda x: x**2  # noqa: E731
    print(f"람다 함수 square(5): {square(5)}")

    # 3.2.2 내장 함수들
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"map() 결과: {squared}")
    total = reduce(lambda x, y: x + y, numbers)
    print(f"reduce() 결과: {total}")

    # 3.2.3 함수의 스코프
    global_var = "전역 변수"

    def scope_test():
        local_var = "지역 변수"
        print(f"함수 내부에서 전역 변수 접근: {global_var}")
        print(f"함수 내부에서 지역 변수 접근: {local_var}")

    scope_test()

    # 3.2.4 데코레이터
    def my_decorator(func):
        def wrapper():
            print("--- 데코레이터: 함수 실행 전 ---")
            func()
            print("--- 데코레이터: 함수 실행 후 ---")

        return wrapper

    @my_decorator
    def say_hello():
        print("안녕하세요!")

    say_hello()


# 메인 함수 정의
def main():
    print("### Chap03: 함수 예제 실행 ###")
    chap3_1_definition_and_call()
    chap3_2_advanced_features()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
