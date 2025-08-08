# Python object 클래스의 구현 위치와 내부 구조 탐구

"""
Python의 object 클래스는 어디서 구현되고 있을까?

답: CPython의 C 코드로 구현되어 있습니다!
주요 파일들:
- Objects/object.c        : object 클래스의 핵심 구현
- Objects/typeobject.c    : 타입 시스템 구현
- Include/object.h        : 헤더 파일 (구조체 정의)
- Include/cpython/object.h: CPython 전용 정의
"""

if __name__ == "__main__":
    print("=== Python object 클래스 구현 위치 탐구 ===\n")

    # 1. object 클래스 기본 정보 확인
    print("1. object 클래스 기본 정보")
    print("-" * 40)

    print(f"object 클래스 타입: {type(object)}")
    print(f"object 클래스 위치: {object}")
    print(f"object 클래스 모듈: {object.__module__}")
    print(f"object 클래스 이름: {object.__name__}")
    print(f"object 클래스 MRO: {object.__mro__}")

    # object가 C로 구현되었다는 증거
    print(f"object는 C 확장인가? {hasattr(object, '__file__')}")  # False면 C 구현
    print()

    # 2. object의 메서드들과 그 구현 위치 추적
    print("2. object 메서드들의 구현 정보")
    print("-" * 40)

    # object의 모든 메서드 분석
    object_methods = {}
    for name in dir(object):
        if not name.startswith("__doc__"):  # __doc__ 제외
            method = getattr(object, name)
            object_methods[name] = method

    print("object 클래스의 메서드들:")
    for name, method in sorted(object_methods.items()):
        method_type = type(method).__name__
        print(f"  {name:15} : {method_type}")

        # 메서드의 구현 위치 정보
        if hasattr(method, "__module__"):
            print(f"                 모듈: {method.__module__}")
        if hasattr(method, "__qualname__"):
            print(f"                 전체이름: {method.__qualname__}")
