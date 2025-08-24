from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap
from typing import Dict, List, Tuple, Optional
import heapq


def chap10_1_collections_module():
    """collections 모듈의 고급 자료구조 예제"""
    print("--- 10.1 collections 모듈 ---")
    
    # 10.1.1 Counter - 요소의 개수를 세는 딕셔너리
    print("\n--- Counter ---")
    text = "hello world"
    char_count = Counter(text)
    print(f"문자 개수: {char_count}")
    
    numbers = [1, 2, 3, 1, 2, 1, 1, 4, 5, 2]
    num_count = Counter(numbers)
    print(f"숫자 개수: {num_count}")
    print(f"가장 많은 2개: {num_count.most_common(2)}")
    
    # 10.1.2 defaultdict - 기본값을 가지는 딕셔너리
    print("\n--- defaultdict ---")
    dd = defaultdict(list)
    dd['fruits'].append('apple')
    dd['fruits'].append('banana')
    dd['colors'].append('red')
    print(f"defaultdict: {dict(dd)}")
    
    # 그룹화 예제
    students = [('Alice', 'Math'), ('Bob', 'Science'), ('Alice', 'English'), ('Bob', 'Math')]
    grouped = defaultdict(list)
    for name, subject in students:
        grouped[name].append(subject)
    print(f"학생별 과목: {dict(grouped)}")
    
    # 10.1.3 deque - 양쪽 끝에서 빠른 추가/제거가 가능한 큐
    print("\n--- deque ---")
    dq = deque([1, 2, 3])
    dq.appendleft(0)  # 왼쪽 끝에 추가
    dq.append(4)      # 오른쪽 끝에 추가
    print(f"deque: {dq}")
    
    print(f"왼쪽에서 제거: {dq.popleft()}")
    print(f"오른쪽에서 제거: {dq.pop()}")
    print(f"deque 결과: {dq}")
    
    # 10.1.4 namedtuple - 이름이 있는 튜플
    print("\n--- namedtuple ---")
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(3, 4)
    print(f"점: ({p1.x}, {p1.y})")
    
    Person = namedtuple('Person', ['name', 'age', 'city'])
    alice = Person('Alice', 25, 'Seoul')
    print(f"사람: {alice.name}, {alice.age}세, {alice.city}")
    
    # 10.1.5 OrderedDict - 순서가 보장되는 딕셔너리 (Python 3.7+ 일반 dict도 순서 보장)
    print("\n--- OrderedDict ---")
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3
    print(f"OrderedDict: {od}")
    
    # 10.1.6 ChainMap - 여러 딕셔너리를 하나로 연결
    print("\n--- ChainMap ---")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'e': 5, 'a': 10}  # 'a'는 중복
    
    chain = ChainMap(dict1, dict2, dict3)
    print(f"ChainMap: {chain}")
    print(f"'a' 값: {chain['a']}")  # 첫 번째 dict의 값이 우선


def chap10_2_heapq():
    """heapq 모듈을 사용한 힙 자료구조 예제"""
    print("\n--- 10.2 heapq (힙 자료구조) ---")
    
    # 최소 힙
    heap = []
    numbers = [5, 3, 8, 1, 9, 2, 7]
    
    for num in numbers:
        heapq.heappush(heap, num)
    print(f"힙에 추가 후: {heap}")
    
    # 가장 작은 값들 추출
    smallest = []
    for _ in range(3):
        smallest.append(heapq.heappop(heap))
    print(f"가장 작은 3개 값: {smallest}")
    print(f"남은 힙: {heap}")
    
    # 최대 힙 구현 (음수 사용)
    max_heap = []
    for num in numbers:
        heapq.heappush(max_heap, -num)
    
    largest = []
    for _ in range(3):
        largest.append(-heapq.heappop(max_heap))
    print(f"가장 큰 3개 값: {largest}")


def chap10_3_advanced_data_structures():
    """고급 자료구조 활용 예제"""
    print("\n--- 10.3 고급 자료구조 활용 ---")
    
    # 10.3.1 LRU 캐시 구현
    class LRUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = OrderedDict()
        
        def get(self, key: str) -> Optional[int]:
            if key in self.cache:
                # 최근 사용한 항목을 맨 끝으로 이동
                self.cache.move_to_end(key)
                return self.cache[key]
            return None
        
        def put(self, key: str, value: int) -> None:
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            
            if len(self.cache) > self.capacity:
                # 가장 오래된 항목 제거
                self.cache.popitem(last=False)
    
    # LRU 캐시 테스트
    cache = LRUCache(3)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    print(f"캐시 상태: {list(cache.cache.items())}")
    
    print(f"'a' 조회: {cache.get('a')}")
    print(f"캐시 상태: {list(cache.cache.items())}")
    
    cache.put('d', 4)  # 'b'가 제거됨
    print(f"'d' 추가 후: {list(cache.cache.items())}")
    
    # 10.3.2 그래프 자료구조
    class Graph:
        def __init__(self):
            self.graph = defaultdict(list)
        
        def add_edge(self, u: str, v: str):
            self.graph[u].append(v)
            self.graph[v].append(u)  # 무방향 그래프
        
        def bfs(self, start: str) -> List[str]:
            visited = set()
            queue = deque([start])
            result = []
            
            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    result.append(vertex)
                    
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            
            return result
    
    # 그래프 테스트
    g = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for u, v in edges:
        g.add_edge(u, v)
    
    print(f"BFS 순회 (A부터): {g.bfs('A')}")


def main():
    print("### Chap10: 고급 자료구조 예제 실행 ###")
    chap10_1_collections_module()
    chap10_2_heapq()
    chap10_3_advanced_data_structures()
    print("\n### 예제 실행 완료 ###")


if __name__ == "__main__":
    main()