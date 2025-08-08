"""
컨텍스트 매니저란?
- 쉽게 말해서 "자동으로 정리해주는 도구"입니다
- with 키워드와 함께 사용합니다
- 작업이 끝나면 자동으로 뒷정리를 해줍니다
"""

import os


# bad example
def bad_file_handling():
    """파일을 제대로 닫지 않는 나쁜 예"""
    print("❌ 나쁜 방법:")

    # 파일 열기
    file = open("test1.txt", "w")
    file.write("안녕하세요!")
    # 파일을 닫지 않음! (문제 발생 가능)

    print("파일을 열었지만 닫지 않았습니다 (위험!)")


# good example (수동 관리)
def manual_file_handling():
    """수동으로 파일을 닫는 방법"""
    print("⚠️  수동 방법:")

    file = None
    try:
        file = open("test2.txt", "w")
        file.write("안녕하세요!")
        print("파일 작업 완료")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        if file:
            file.close()
            print("파일을 수동으로 닫았습니다")


# context manager example
# Python의 내장 파일 객체(open()으로 생성)는 이미 __enter__와 __exit__ 메서드를 가지고 있어서 with문과 바로 사용 가능
def context_manager_file_handling():
    """컨텍스트 매니저를 사용한 파일 처리"""
    print("✅ 좋은 방법:")

    with open("test3.txt", "w") as file:
        file.write("안녕하세요!")
        print("파일 작업 완료 (자동으로 닫힘)")

    print("파일이 자동으로 닫혔습니다 (안전!)")


# 1. 파일 객체의 closed 속성 확인
def check_file_closed_attribute():
    """파일 객체의 closed 속성으로 확인"""
    print("1. 파일 객체의 closed 속성 확인")
    print("-" * 40)

    # 나쁜 예시
    print("❌ 나쁜 방법:")
    file1 = open("test1.txt", "w")
    file1.write("테스트")
    print(f"   파일 상태 (닫기 전): closed = {file1.closed}")
    print(f"   파일 객체: {file1}")

    # 파일을 닫지 않고 놔둠 (위험!)

    print("✅ 좋은 방법:")
    file2 = open("test2.txt", "w")
    file2.write("테스트")
    print(f"   파일 상태 (닫기 전): closed = {file2.closed}")
    file2.close()
    print(f"   파일 상태 (닫은 후): closed = {file2.closed}")
    print(f"   파일 객체: {file2}")

    # 정리: file1은 아직 열려있음!
    print(f"⚠️  file1은 여전히 열려있음: closed = {file1.closed}")
    file1.close()  # 수동으로 닫아야 함

    # 생성된 파일들 정리
    for filename in ["test1.txt", "test2.txt", "test3.txt"]:
        if os.path.exists(filename):
            os.remove(filename)

    print()


# 실제 파일 객체의 컨텍스트 매니저 메서드 확인
def inspect_file_object():
    """실제 파일 객체가 컨텍스트 매니저인지 확인"""
    print("1. 파일 객체의 컨텍스트 매니저 메서드 확인")
    print("-" * 50)

    # 파일 객체 생성
    f = open("temp_inspect.txt", "w")

    # 컨텍스트 매니저 메서드가 있는지 확인
    print(f"__enter__ 메서드 존재: {hasattr(f, '__enter__')}")
    print(f"__exit__ 메서드 존재: {hasattr(f, '__exit__')}")

    # 실제 메서드 확인
    print(f"__enter__ 메서드: {f.__enter__}")
    print(f"__exit__ 메서드: {f.__exit__}")

    # 파일 닫기
    f.close()
    if os.path.exists("temp_inspect.txt"):
        os.remove("temp_inspect.txt")


# 파일 객체의 __enter__와 __exit__ 동작 분석
def analyze_file_context_methods():
    """파일 객체의 컨텍스트 매니저 메서드 동작 분석"""
    print("2. 파일 객체의 __enter__와 __exit__ 동작 분석")
    print("-" * 50)

    # 파일 생성
    f = open("test_analysis.txt", "w")

    print(f"파일 생성 직후 - closed 상태: {f.closed}")
    print(f"파일 객체 ID: {id(f)}")

    # __enter__ 메서드 직접 호출
    returned_object = f.__enter__()
    print(f"__enter__() 반환 객체 ID: {id(returned_object)}")
    print(f"같은 객체인가? {f is returned_object}")  # True가 나와야 함

    # 파일에 쓰기
    f.write("테스트 내용")
    print(f"파일 쓰기 후 - closed 상태: {f.closed}")

    # __exit__ 메서드 직접 호출 (정상 종료 시뮬레이션)
    f.__exit__(None, None, None)
    print(f"__exit__ 호출 후 - closed 상태: {f.closed}")

    # 파일 정리
    if os.path.exists("test_analysis.txt"):
        os.remove("test_analysis.txt")


def check_file_status():
    bad_file_handling()
    manual_file_handling()
    context_manager_file_handling()

    print("=== 파일이 안 닫혀서 위험한 상태 체크하는 방법들 ===")
    check_file_closed_attribute()


def analyze_context_manager():
    print("=== 컨텍스트 매니저 분석 ===")
    inspect_file_object()
    analyze_file_context_methods()


if __name__ == "__main__":
    # check_file_status()
    analyze_context_manager()
