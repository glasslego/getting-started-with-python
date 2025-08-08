# 모든 특수 메서드를 포함한 간단한 클래스 예제


class MyWallet(object):
    """지갑 클래스 - 모든 특수 메서드 데모"""

    # 1. 생성/초기화
    def __init__(self, owner, money=0):
        """지갑 생성"""
        self.owner = owner
        self.money = money
        self.items = []  # 지갑 안의 물건들
        print(f"💰 {owner}의 지갑이 만들어졌습니다 (초기 금액: {money}원)")

    # 2. 문자열 표현
    def __str__(self):
        """사용자용 표현"""
        return f"{self.owner}의 지갑 (💰{self.money}원, 📦{len(self.items)}개 물건)"

    def __repr__(self):
        """개발자용 표현"""
        return f"MyWallet(owner='{self.owner}', money={self.money})"

    # 3. 산술 연산 (돈 넣고 빼기)
    def __add__(self, amount):
        """+ 연산자: 돈 넣기"""
        if isinstance(amount, (int, float)) and amount >= 0:
            new_wallet = MyWallet(self.owner, self.money + amount)
            new_wallet.items = self.items.copy()
            print(f"💵 {amount}원 추가!")
            return new_wallet
        return NotImplemented

    def __sub__(self, amount):
        """- 연산자: 돈 빼기"""
        if isinstance(amount, (int, float)) and amount >= 0:
            if self.money >= amount:
                new_wallet = MyWallet(self.owner, self.money - amount)
                new_wallet.items = self.items.copy()
                print(f"💸 {amount}원 사용!")
                return new_wallet
            else:
                print("❌ 돈이 부족해요!")
                return self
        return NotImplemented

    # 4. 비교 연산 (돈 비교)
    def __eq__(self, other):
        """== 연산자"""
        if isinstance(other, MyWallet):
            return self.money == other.money
        return False

    def __lt__(self, other):
        """< 연산자"""
        if isinstance(other, MyWallet):
            return self.money < other.money
        return NotImplemented

    def __gt__(self, other):
        """> 연산자"""
        if isinstance(other, MyWallet):
            return self.money > other.money
        return NotImplemented

    # 5. 컨테이너 기능 (물건 관리)
    def __len__(self):
        """len() 함수"""
        return len(self.items)

    def __getitem__(self, index):
        """[] 접근"""
        return self.items[index]

    def __setitem__(self, index, item):
        """[] 할당"""
        self.items[index] = item

    def __contains__(self, item):
        """in 연산자"""
        return item in self.items

    def __iter__(self):
        """for문 반복"""
        return iter(self.items)

    # 6. 함수처럼 호출
    def __call__(self, action, target=None):
        """지갑을 함수처럼 사용"""
        if action == "돈확인":
            print(f"💰 현재 {self.money}원 있어요!")
            return self.money
        elif action == "물건추가" and target:
            self.items.append(target)
            print(f"📦 {target}를 지갑에 넣었어요!")
        elif action == "물건목록":
            print(f"📦 지갑 안 물건: {', '.join(self.items) if self.items else '없음'}")
            return self.items
        else:
            print("❓ '돈확인', '물건추가', '물건목록' 중 하나를 선택하세요!")

    # 7. 불린 변환
    def __bool__(self):
        """bool() 변환 (돈이 있으면 True)"""
        return self.money > 0

    # 8. 컨텍스트 매니저 (안전한 쇼핑)
    def __enter__(self):
        """쇼핑 시작"""
        print(f"🛍️  {self.owner}님 쇼핑 시작! (현재 {self.money}원)")
        self._original_money = self.money  # 원래 돈 저장
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """쇼핑 끝"""
        spent = self._original_money - self.money
        print(f"🛍️  쇼핑 끝! 총 {spent}원 사용했어요")
        if exc_type:
            print(f"⚠️  쇼핑 중 문제 발생: {exc_value}")
        return False


if __name__ == "__main__":
    # 1. 기본 생성 및 문자열 표현
    print("1. 지갑 생성 및 기본 정보")
    wallet = MyWallet("철수", 10000)
    print(f"str(): {wallet}")
    print(f"repr(): {repr(wallet)}")
    print()

    # 2. 산술 연산
    print("2. 돈 넣고 빼기")
    wallet = wallet + 5000  # 돈 추가
    wallet = wallet - 3000  # 돈 사용
    print(f"결과: {wallet}")
    print()

    # 3. 물건 관리 (컨테이너 기능)
    print("3. 물건 관리")
    wallet.items.append("신용카드")
    wallet.items.append("신분증")
    wallet.items.append("영수증")

    print(f"물건 개수: {len(wallet)}개")  # __len__
    print(f"첫 번째 물건: {wallet[0]}")  # __getitem__
    print(f"신용카드 있나? {'신용카드' in wallet}")  # __contains__

    print("지갑 안 물건들:")
    for item in wallet:  # __iter__
        print(f"  - {item}")

    wallet[2] = "쿠폰"  # __setitem__
    print(f"세 번째 물건 변경: {wallet[2]}")
    print()

    # 4. 비교 연산
    print("4. 다른 지갑과 비교")
    wallet2 = MyWallet("영희", 15000)
    print(f"철수 지갑: {wallet}")
    print(f"영희 지갑: {wallet2}")
    print(f"같은 금액? {wallet == wallet2}")  # __eq__
    print(f"철수가 더 적나? {wallet < wallet2}")  # __lt__
    print(f"영희가 더 많나? {wallet2 > wallet}")  # __gt__
    print()

    # 5. 함수처럼 호출
    print("5. 지갑을 함수처럼 사용")
    wallet("돈확인")  # __call__
    wallet("물건추가", "동전")  # __call__
    wallet("물건목록")  # __call__
    print()

    # 6. 불린 변환
    print("6. 불린 변환")
    empty_wallet = MyWallet("가난한 사람", 0)
    print(f"철수 지갑 활성? {bool(wallet)}")  # __bool__
    print(f"빈 지갑 활성? {bool(empty_wallet)}")  # __bool__
    print()

    # 7. 컨텍스트 매니저 (안전한 쇼핑)
    print("7. 안전한 쇼핑 (컨텍스트 매니저)")
    with wallet as shopping_wallet:  # __enter__
        print("  🛒 과자 구매...")
        shopping_wallet = shopping_wallet - 1500
        print("  🛒 음료 구매...")
        shopping_wallet = shopping_wallet - 2000
        print(f"  💰 남은 돈: {shopping_wallet.money}원")
    # __exit__ 자동 호출

    print(f"쇼핑 후 최종 지갑: {wallet}")
    print()

    # 8. 예외 상황에서도 안전한 컨텍스트 매니저
    print("8. 쇼핑 중 문제 발생 시")
    try:
        with wallet as shopping_wallet2:
            print("  🛒 비싼 물건 구매 시도...")
            shopping_wallet2 = shopping_wallet2 - 50000  # 돈 부족!
            raise Exception("카드가 막혔어요!")  # 의도적 예외
    except Exception as e:
        print(f"  🚨 예외 처리: {e}")

    print()
