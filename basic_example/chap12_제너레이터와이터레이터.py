from typing import Iterator, Generator, Iterable, Any, List
import itertools
import sys


def chap12_1_iterators():
    """이터레이터 기초 예제"""
    print("--- 12.1 이터레이터 기초 ---")
    
    # 12.1.1 기본 이터레이터 사용
    numbers = [1, 2, 3, 4, 5]
    iterator = iter(numbers)
    
    print("이터레이터 수동 사용:")
    try:
        while True:
            value = next(iterator)
            print(f"값: {value}")
    except StopIteration:
        print("이터레이터 종료")
    
    # 12.1.2 for문과 이터레이터
    print("\nfor문에서 이터레이터 자동 사용:")
    for num in numbers:
        print(f"For문 값: {num}")
    
    # 12.1.3 다양한 이터러블 객체들
    print("\n다양한 이터러블 객체들:")
    
    # 문자열
    text = "Python"
    for char in text:
        print(f"문자: {char}")
    
    # 딕셔너리
    person = {"name": "Alice", "age": 25, "city": "Seoul"}
    for key in person:
        print(f"키: {key}, 값: {person[key]}")
    
    # 딕셔너리의 아이템들
    for key, value in person.items():
        print(f"{key}: {value}")


def chap12_2_custom_iterators():
    """커스텀 이터레이터 예제"""
    print("\n--- 12.2 커스텀 이터레이터 ---")
    
    # 12.2.1 이터레이터 프로토콜 구현
    class NumberRange:
        def __init__(self, start: int, end: int, step: int = 1):
            self.start = start
            self.end = end
            self.step = step
        
        def __iter__(self) -> Iterator[int]:
            return NumberRangeIterator(self.start, self.end, self.step)
    
    class NumberRangeIterator:
        def __init__(self, start: int, end: int, step: int):
            self.current = start
            self.end = end
            self.step = step
        
        def __iter__(self) -> Iterator[int]:
            return self
        
        def __next__(self) -> int:
            if self.current >= self.end:
                raise StopIteration
            
            value = self.current
            self.current += self.step
            return value
    
    # 사용 예제
    print("커스텀 이터레이터 사용:")
    for num in NumberRange(1, 10, 2):
        print(f"홀수: {num}")
    
    # 12.2.2 간단한 이터레이터 (클래스 하나로 구현)
    class Fibonacci:
        def __init__(self, max_count: int):
            self.max_count = max_count
            self.count = 0
            self.a, self.b = 0, 1
        
        def __iter__(self) -> Iterator[int]:
            return self
        
        def __next__(self) -> int:
            if self.count >= self.max_count:
                raise StopIteration
            
            if self.count == 0:
                self.count += 1
                return self.a
            elif self.count == 1:
                self.count += 1
                return self.b
            else:
                self.a, self.b = self.b, self.a + self.b
                self.count += 1
                return self.b
    
    print("\n피보나치 이터레이터:")
    for fib in Fibonacci(10):
        print(f"피보나치: {fib}")


def chap12_3_generators():
    """제너레이터 기초 예제"""
    print("\n--- 12.3 제너레이터 기초 ---")
    
    # 12.3.1 간단한 제너레이터 함수
    def simple_generator() -> Generator[int, None, None]:
        print("제너레이터 시작")
        yield 1
        print("첫 번째 yield 이후")
        yield 2
        print("두 번째 yield 이후")
        yield 3
        print("제너레이터 종료")
    
    print("제너레이터 함수 사용:")
    gen = simple_generator()
    for value in gen:
        print(f"생성된 값: {value}")
    
    # 12.3.2 무한 제너레이터
    def infinite_counter(start: int = 0) -> Generator[int, None, None]:
        current = start
        while True:
            yield current
            current += 1
    
    print("\n무한 제너레이터 (처음 5개만):")
    counter = infinite_counter(10)
    for _ in range(5):
        print(f"카운터: {next(counter)}")
    
    # 12.3.3 피보나치 제너레이터
    def fibonacci_generator(max_count: int) -> Generator[int, None, None]:
        a, b = 0, 1
        count = 0
        while count < max_count:
            yield a
            a, b = b, a + b
            count += 1
    
    print("\n피보나치 제너레이터:")
    fib_gen = fibonacci_generator(8)
    fib_list = list(fib_gen)
    print(f"피보나치 수열: {fib_list}")


def chap12_4_generator_expressions():
    """제너레이터 표현식 예제"""
    print("\n--- 12.4 제너레이터 표현식 ---")
    
    # 12.4.1 기본 제너레이터 표현식
    numbers = range(1, 11)
    
    # 제곱수 제너레이터
    squares_gen = (x**2 for x in numbers)
    print("제곱수 제너레이터:")
    for square in squares_gen:
        print(f"제곱: {square}")
    
    # 12.4.2 조건부 제너레이터 표현식
    even_squares = (x**2 for x in numbers if x % 2 == 0)
    print(f"\n짝수의 제곱: {list(even_squares)}")
    
    # 12.4.3 중첩 제너레이터 표현식
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = (item for row in matrix for item in row)
    print(f"평탄화된 매트릭스: {list(flattened)}")
    
    # 12.4.4 메모리 효율성 비교
    print("\n메모리 사용량 비교:")
    
    # 리스트 컴프리헨션 (모든 값을 메모리에 저장)
    large_list = [x**2 for x in range(1000000)]
    list_size = sys.getsizeof(large_list)
    print(f"리스트 크기: {list_size:,} bytes")
    
    # 제너레이터 표현식 (값을 필요할 때만 생성)
    large_gen = (x**2 for x in range(1000000))
    gen_size = sys.getsizeof(large_gen)
    print(f"제너레이터 크기: {gen_size:,} bytes")
    
    del large_list, large_gen  # 메모리 정리


def chap12_5_advanced_generator_features():
    """제너레이터 고급 기능 예제"""
    print("\n--- 12.5 제너레이터 고급 기능 ---")
    
    # 12.5.1 send() 메서드 사용
    def accumulator() -> Generator[int, int, None]:
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value
    
    print("제너레이터 send() 메서드:")
    acc = accumulator()
    print(f"초기값: {next(acc)}")  # 제너레이터 시작
    print(f"5 추가 후: {acc.send(5)}")
    print(f"10 추가 후: {acc.send(10)}")
    print(f"3 추가 후: {acc.send(3)}")
    
    # 12.5.2 yield from 사용
    def sub_generator() -> Generator[int, None, None]:
        yield 1
        yield 2
        yield 3
    
    def main_generator() -> Generator[int, None, None]:
        yield from sub_generator()
        yield 4
        yield 5
    
    print(f"\nyield from 예제: {list(main_generator())}")
    
    # 12.5.3 제너레이터 체인
    def numbers_generator(n: int) -> Generator[int, None, None]:
        for i in range(n):
            yield i
    
    def square_generator(numbers: Iterable[int]) -> Generator[int, None, None]:
        for num in numbers:
            yield num ** 2
    
    def filter_even(numbers: Iterable[int]) -> Generator[int, None, None]:
        for num in numbers:
            if num % 2 == 0:
                yield num
    
    print("\n제너레이터 체인:")
    chain = filter_even(square_generator(numbers_generator(10)))
    print(f"0~9의 제곱 중 짝수: {list(chain)}")


def chap12_6_itertools_module():
    """itertools 모듈 활용 예제"""
    print("\n--- 12.6 itertools 모듈 ---")
    
    # 12.6.1 무한 이터레이터들
    print("itertools.count() - 무한 카운터:")
    counter = itertools.count(start=10, step=2)
    for _ in range(5):
        print(f"카운트: {next(counter)}")
    
    print("\nitertools.cycle() - 순환:")
    colors = ["red", "green", "blue"]
    color_cycle = itertools.cycle(colors)
    for _ in range(8):
        print(f"색상: {next(color_cycle)}")
    
    print("\nitertools.repeat() - 반복:")
    repeated = itertools.repeat("Python", 3)
    print(f"반복: {list(repeated)}")
    
    # 12.6.2 조합형 이터레이터들
    print("\n조합형 이터레이터들:")
    
    # 조합 (combinations)
    items = ['A', 'B', 'C', 'D']
    combinations = list(itertools.combinations(items, 2))
    print(f"2개 조합: {combinations}")
    
    # 순열 (permutations)
    permutations = list(itertools.permutations(items[:3], 2))
    print(f"2개 순열: {permutations}")
    
    # 중복 조합 (combinations_with_replacement)
    combinations_rep = list(itertools.combinations_with_replacement(['A', 'B'], 2))
    print(f"중복 조합: {combinations_rep}")
    
    # 12.6.3 필터링 이터레이터들
    numbers = range(1, 11)
    
    # takewhile - 조건을 만족하는 동안 가져오기
    take_while_5 = list(itertools.takewhile(lambda x: x < 5, numbers))
    print(f"5 미만까지: {take_while_5}")
    
    # dropwhile - 조건을 만족하는 동안 건너뛰기
    drop_while_5 = list(itertools.dropwhile(lambda x: x < 5, numbers))
    print(f"5 이상부터: {drop_while_5}")
    
    # filterfalse - filter의 반대
    odd_numbers = list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))
    print(f"홀수들: {odd_numbers}")


def chap12_7_practical_applications():
    """실용적인 활용 예제"""
    print("\n--- 12.7 실용적인 활용 ---")
    
    # 12.7.1 대용량 파일 처리 시뮬레이션
    def simulate_large_file_processing() -> Generator[str, None, None]:
        """대용량 파일을 읽는 것처럼 시뮬레이션"""
        for i in range(1000):
            yield f"line_{i}: 이것은 파일의 {i}번째 줄입니다."
    
    def process_lines(lines: Iterable[str]) -> Generator[str, None, None]:
        """각 줄을 처리하는 제너레이터"""
        for line in lines:
            if "500" in line or "999" in line:  # 특정 조건의 라인만
                yield line.upper()
    
    print("대용량 파일 처리 시뮬레이션:")
    file_gen = simulate_large_file_processing()
    processed_gen = process_lines(file_gen)
    
    # 처음 몇 개만 처리 (실제로는 필요한 만큼만)
    for i, line in enumerate(processed_gen):
        if i >= 2:  # 처음 2개만
            break
        print(f"처리된 라인: {line}")
    
    # 12.7.2 배치 처리
    def batch_processor(data: Iterable[Any], batch_size: int) -> Generator[List[Any], None, None]:
        """데이터를 배치 단위로 처리하는 제너레이터"""
        iterator = iter(data)
        while True:
            batch = list(itertools.islice(iterator, batch_size))
            if not batch:
                break
            yield batch
    
    print("\n배치 처리:")
    large_dataset = range(1, 23)  # 22개 데이터
    
    for batch_num, batch in enumerate(batch_processor(large_dataset, 5), 1):
        print(f"배치 {batch_num}: {batch}")
    
    # 12.7.3 윈도우 슬라이딩
    def sliding_window(data: Iterable[Any], window_size: int) -> Generator[List[Any], None, None]:
        """슬라이딩 윈도우 제너레이터"""
        iterator = iter(data)
        window = list(itertools.islice(iterator, window_size))
        
        if len(window) == window_size:
            yield window
        
        for item in iterator:
            window = window[1:] + [item]
            yield window
    
    print("\n슬라이딩 윈도우 (크기 3):")
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    for window in sliding_window(data, 3):
        print(f"윈도우: {window}")


def main():
    print("### Chap12. 제너레이터와 이터레이터 예제 실행 ###")
    chap12_1_iterators()
    chap12_2_custom_iterators()
    chap12_3_generators()
    chap12_4_generator_expressions()
    chap12_5_advanced_generator_features()
    chap12_6_itertools_module()
    chap12_7_practical_applications()
    print("\n### 예제 실행 완료 ###")


if __name__ == "__main__":
    main()