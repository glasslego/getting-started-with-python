class SimpleContext:
    """가장 기본적인 컨텍스트 매니저"""

    def __enter__(self):
        """with문이 시작될 때 실행"""
        print("   🚪 들어옵니다 (__enter__)")
        return "안녕하세요!"  # 이 값이 as 뒤의 변수에 할당됨

    def __exit__(self, exc_type, exc_value, traceback):
        """with문이 끝날 때 실행"""
        print("   🚪 나갑니다 (__exit__)")
        return False  # 예외를 다시 발생시킴


if __name__ == '__main__':
    print("사용법:")
    with SimpleContext() as message:
        print(f"메시지: {message}")
        print("작업을 합니다")

    print("✨ with문이 끝났습니다\n")
