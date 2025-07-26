import logging
import os


# 8.1 예외의 기본 개념
def chap8_1_exception_basics():
    """try-except, else, finally 예제를 실행하는 함수"""
    print("--- 8.1 예외의 기본 개념 ---")

    # 8.1.1 try-except 기본 구조
    try:
        # number = int(input("숫자를 입력하세요: ")) # 자동 실행을 위해 주석 처리
        number = 0
        result = 10 / number
        print(result)
    except ValueError:
        print("ValueError: 올바른 숫자를 입력해주세요.")
    except ZeroDivisionError:
        print("ZeroDivisionError: 0으로 나눌 수 없습니다.")

    # 8.1.2 else와 finally 절
    def safe_divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("safe_divide: 0으로 나눌 수 없습니다.")
            return None
        else:
            print("safe_divide: 나눗셈이 성공적으로 완료되었습니다.")
            return result
        finally:
            print("safe_divide: 나눗셈 연산을 시도했습니다.")

    print("\n--- else, finally 예제 ---")
    safe_divide(10, 2)
    safe_divide(10, 0)


# 8.2 주요 내장 예외들
def chap8_2_built_in_exceptions():
    """주요 내장 예외 처리 예제를 실행하는 함수"""
    print("\n--- 8.2 주요 내장 예외들 ---")

    try:
        number = int("abc")
        print(number)
    except ValueError as e:
        print(f"ValueError 발생: {e}")

    try:
        result = "hello" + 5
        print(result)
    except TypeError as e:
        print(f"TypeError 발생: {e}")

    try:
        numbers = [1, 2, 3]
        print(numbers[5])
    except IndexError as e:
        print(f"IndexError 발생: {e}")


# 8.3 사용자 정의 예외
def chap8_3_custom_exceptions():
    """사용자 정의 예외 클래스 생성 및 사용 예제를 실행하는 함수"""
    print("\n--- 8.3 사용자 정의 예외 ---")

    class InvalidAgeError(Exception):
        """나이가 유효하지 않을 때 발생하는 예외"""

        def __init__(self, age, message="나이가 유효하지 않습니다"):
            self.age = age
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return f"{self.message}: {self.age}"

    try:
        age = -5
        if not (0 <= age <= 150):
            raise InvalidAgeError(age)
    except InvalidAgeError as e:
        print(f"사용자 정의 예외 발생: {e}")


# 8.4 예외 처리 모범 사례
def chap8_4_best_practices():
    """로깅, 컨텍스트 매니저 등 예외 처리 모범 사례 예제를 실행하는 함수"""
    print("\n--- 8.4 예외 처리 모범 사례 ---")

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    def divide_with_logging(a, b):
        try:
            logger.info(f"나눗셈 시도: {a} / {b}")
            result = a / b
            return result
        except ZeroDivisionError:
            logger.error(f"0으로 나누기 시도: {a} / {b}")
            raise

    try:
        divide_with_logging(10, 0)
    except ZeroDivisionError:
        print("로깅 예제: 0으로 나누기 예외를 처리했습니다.")

    # 컨텍스트 매니저
    class SafeFileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            print(f"파일 열기: {self.filename}")
            self.file = open(self.filename, self.mode, encoding="utf-8")
            return self.file

        def __exit__(self, exc_type, exc_value, traceback):
            if self.file:
                self.file.close()
            print(f"파일 닫기: {self.filename}")
            if exc_type:
                print(f"예외 발생: {exc_type.__name__}")
            return True  # 예외를 처리했음을 알림

    with SafeFileManager("test.txt", "w") as f:
        f.write("컨텍스트 매니저 테스트")
        # 일부러 예외 발생
        # f.write(123) # TypeError 발생

    # 생성된 파일 정리
    if os.path.exists("test.txt"):
        os.remove("test.txt")


# 메인 함수 정의
def main():
    print("### Chap08: 예외 처리 예제 실행 ###")
    chap8_1_exception_basics()
    chap8_2_built_in_exceptions()
    chap8_3_custom_exceptions()
    chap8_4_best_practices()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
