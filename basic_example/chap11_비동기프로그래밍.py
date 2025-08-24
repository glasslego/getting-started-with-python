import asyncio
import aiohttp
import time
from typing import List, Optional


async def chap11_1_async_basics():
    """비동기 프로그래밍 기초 예제"""
    print("--- 11.1 비동기 프로그래밍 기초 ---")
    
    # 11.1.1 간단한 비동기 함수
    async def say_hello(name: str, delay: float):
        await asyncio.sleep(delay)
        print(f"안녕하세요, {name}!")
        return f"Hello {name}"
    
    # 단일 비동기 함수 실행
    result = await say_hello("Alice", 1)
    print(f"결과: {result}")
    
    # 11.1.2 여러 비동기 작업 동시 실행
    print("\n--- 여러 작업 동시 실행 ---")
    start_time = time.time()
    
    # 순차 실행 (비효율적)
    print("순차 실행:")
    await say_hello("Bob", 1)
    await say_hello("Charlie", 1)
    await say_hello("David", 1)
    
    sequential_time = time.time() - start_time
    print(f"순차 실행 시간: {sequential_time:.2f}초")
    
    # 동시 실행 (효율적)
    print("\n동시 실행:")
    start_time = time.time()
    
    tasks = [
        say_hello("Eve", 1),
        say_hello("Frank", 1),
        say_hello("Grace", 1)
    ]
    
    results = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start_time
    print(f"동시 실행 시간: {concurrent_time:.2f}초")
    print(f"결과: {results}")


async def chap11_2_async_patterns():
    """비동기 프로그래밍 패턴 예제"""
    print("\n--- 11.2 비동기 프로그래밍 패턴 ---")
    
    # 11.2.1 asyncio.wait_for - 타임아웃 설정
    async def slow_operation():
        await asyncio.sleep(3)
        return "완료!"
    
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
        print(f"결과: {result}")
    except asyncio.TimeoutError:
        print("작업이 타임아웃되었습니다.")
    
    # 11.2.2 asyncio.as_completed - 완료되는 순서대로 처리
    async def task_with_delay(name: str, delay: float):
        await asyncio.sleep(delay)
        return f"작업 {name} 완료 (지연: {delay}초)"
    
    print("\n--- 완료 순서대로 처리 ---")
    tasks = [
        task_with_delay("A", 2),
        task_with_delay("B", 1),
        task_with_delay("C", 3)
    ]
    
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(result)
    
    # 11.2.3 Producer-Consumer 패턴
    print("\n--- Producer-Consumer 패턴 ---")
    
    async def producer(queue: asyncio.Queue, name: str):
        for i in range(3):
            item = f"{name}-item-{i}"
            await queue.put(item)
            print(f"생산자 {name}: {item} 생산")
            await asyncio.sleep(0.5)
        await queue.put(None)  # 종료 신호
    
    async def consumer(queue: asyncio.Queue, name: str):
        while True:
            item = await queue.get()
            if item is None:
                break
            print(f"소비자 {name}: {item} 처리")
            await asyncio.sleep(1)
            queue.task_done()
    
    queue = asyncio.Queue(maxsize=2)
    
    producer_task = asyncio.create_task(producer(queue, "P1"))
    consumer_task = asyncio.create_task(consumer(queue, "C1"))
    
    await producer_task
    await consumer_task


async def chap11_3_async_context_manager():
    """비동기 컨텍스트 매니저 예제"""
    print("\n--- 11.3 비동기 컨텍스트 매니저 ---")
    
    class AsyncResource:
        def __init__(self, name: str):
            self.name = name
        
        async def __aenter__(self):
            print(f"{self.name} 리소스 획득 중...")
            await asyncio.sleep(0.5)
            print(f"{self.name} 리소스 획득 완료")
            return self
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print(f"{self.name} 리소스 정리 중...")
            await asyncio.sleep(0.3)
            print(f"{self.name} 리소스 정리 완료")
        
        async def do_work(self):
            print(f"{self.name}에서 작업 수행 중...")
            await asyncio.sleep(1)
            return f"{self.name} 작업 완료"
    
    # 비동기 컨텍스트 매니저 사용
    async with AsyncResource("데이터베이스") as resource:
        result = await resource.do_work()
        print(result)


async def chap11_4_async_iteration():
    """비동기 이터레이터 예제"""
    print("\n--- 11.4 비동기 이터레이터 ---")
    
    class AsyncRange:
        def __init__(self, start: int, end: int):
            self.start = start
            self.end = end
        
        def __aiter__(self):
            return self
        
        async def __anext__(self):
            if self.start >= self.end:
                raise StopAsyncIteration
            
            current = self.start
            self.start += 1
            await asyncio.sleep(0.2)  # 비동기 작업 시뮬레이션
            return current
    
    print("비동기 이터레이터 사용:")
    async for num in AsyncRange(1, 5):
        print(f"숫자: {num}")
    
    # 비동기 제너레이터
    async def async_fibonacci(n: int):
        a, b = 0, 1
        for _ in range(n):
            yield a
            await asyncio.sleep(0.1)
            a, b = b, a + b
    
    print("\n비동기 제너레이터:")
    async for fib in async_fibonacci(8):
        print(f"피보나치: {fib}")


async def chap11_5_real_world_example():
    """실제 활용 예제 - HTTP 요청"""
    print("\n--- 11.5 실제 활용 예제 ---")
    
    # HTTP 요청 시뮬레이션 (aiohttp 없이)
    async def fetch_data(url: str, delay: float) -> dict:
        print(f"데이터 가져오는 중: {url}")
        await asyncio.sleep(delay)  # 네트워크 지연 시뮬레이션
        return {
            "url": url,
            "status": 200,
            "data": f"데이터 from {url}",
            "delay": delay
        }
    
    # 여러 API 동시 호출
    urls_and_delays = [
        ("https://api1.example.com", 1.0),
        ("https://api2.example.com", 1.5),
        ("https://api3.example.com", 0.8),
    ]
    
    start_time = time.time()
    
    # 동시 호출
    tasks = [fetch_data(url, delay) for url, delay in urls_and_delays]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    end_time = time.time()
    
    print("API 호출 결과:")
    for result in results:
        if isinstance(result, Exception):
            print(f"오류: {result}")
        else:
            print(f"URL: {result['url']}, 지연: {result['delay']}초")
    
    print(f"총 소요 시간: {end_time - start_time:.2f}초")


async def main():
    print("### Chap11: 비동기 프로그래밍 예제 실행 ###")
    await chap11_1_async_basics()
    await chap11_2_async_patterns()
    await chap11_3_async_context_manager()
    await chap11_4_async_iteration()
    await chap11_5_real_world_example()
    print("\n### 예제 실행 완료 ###")


if __name__ == "__main__":
    # 비동기 함수 실행
    asyncio.run(main())