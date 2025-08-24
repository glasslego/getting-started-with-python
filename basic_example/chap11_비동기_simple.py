import asyncio
import time


# 1. 일반 함수 방식 (동기)
def 동기_커피_만들기(이름):
    print(f"☕ {이름} 커피 시작")
    time.sleep(2)  # 실제로 2초 멈춤
    print(f"☕ {이름} 커피 완성")
    return f"{이름} 커피"


def 동기_방식_카페():
    print("=== 동기 방식 카페 (한 번에 하나씩) ===")
    start_time = time.time()

    # 손님들 순서대로 처리
    커피1 = 동기_커피_만들기("아메리카노")
    print(f"수행 시간: {time.time() - start_time} {커피1} 준비 완료")
    커피2 = 동기_커피_만들기("라떼")
    print(f"수행 시간: {time.time() - start_time} {커피2} 준비 완료")
    커피3 = 동기_커피_만들기("카푸치노")
    print(f"수행 시간: {time.time() - start_time} {커피3} 준비 완료")

    총_시간 = time.time() - start_time
    print(f"총 걸린 시간: {총_시간:.1f}초\n")


# 2. 코루틴 방식 (비동기)
async def 비동기_커피_만들기(이름):
    print(f"☕ {이름} 커피 시작")
    await asyncio.sleep(2)  # 다른 작업 가능
    print(f"☕ {이름} 커피 완성")
    return f"{이름} 커피"


async def 비동기_방식_카페():
    print("=== 비동기 방식 카페 (동시에 여러 개) ===")
    start_time = time.time()

    # 여러 커피를 동시에 만들기 시작
    커피들 = await asyncio.gather(
        비동기_커피_만들기("아메리카노"),
        비동기_커피_만들기("라떼"),
        비동기_커피_만들기("카푸치노")
    )

    총_시간 = time.time() - start_time
    print(f"완성된 커피: {커피들}")
    print(f"총 걸린 시간: {총_시간:.1f}초")


# 실행 예제
if __name__ == "__main__":
    # 동기 방식 실행
    동기_방식_카페()

    # 비동기 방식 실행
    asyncio.run(비동기_방식_카페())