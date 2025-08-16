# 1.1 변수 선언과 할당
def chap1_1_variables():
    print("--- 1.1 변수 선언과 할당 ---")
    # 변수 선언
    name = "Alice"
    age = 25
    height = 165.5
    is_student = True
    print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

    # 다중 할당
    x, y, z = 1, 2, 3
    a = b = c = 10
    print(f"x, y, z = {x}, {y}, {z}")
    print(f"a, b, c = {a}, {b}, {c}")


# 1.2 기본 자료형
def chap1_2_data_types():
    print("\n--- 1.2 기본 자료형 ---")
    # 숫자형 (Numbers)
    integer_num = 42
    float_num = 3.14
    print(f"정수: {integer_num}, 실수: {float_num}")

    # 문자열 (String)
    text = "Python"
    print(f"첫 글자: {text[0]}, 마지막 글자: {text[-1]}")
    name = "Alice"
    age = 25
    print(f"f-string 포매팅: 이름은 {name}, 나이는 {age}")  # f-string 예시

    # 불린형 (Boolean)
    is_true = True
    print(f"불린 AND 연산: {is_true and False}")
    print(f"불린 OR 연산: {is_true or False}")


# 1.3 컬렉션 자료형
def chap1_3_collections():
    print("\n--- 1.3 컬렉션 자료형 ---")
    # 리스트 (List)
    fruits = ["apple", "banana"]
    fruits.append("orange")
    print(f"리스트: {fruits}")

    # 튜플 (Tuple)
    coordinates = (10, 20)
    print(f"튜플: {coordinates}")

    # 딕셔너리 (Dictionary)
    person = {"name": "Alice", "age": 25}
    person["city"] = "Seoul"
    print(f"딕셔너리: {person}")

    # 집합 (Set)
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(f"집합 합집합: {set1 | set2}")


# 1.4 타입 변환
def chap1_4_type_conversion():
    print("\n--- 1.4 타입 변환 ---")
    str_num = "123"
    int_num = int(str_num)
    print(f"문자열 '{str_num}' -> 정수 {int_num}")

    list_data = [1, 2, 3, 2]
    set_data = set(list_data)
    print(f"리스트 {list_data} -> 집합 {set_data} (중복 제거)")


# 메인 함수 정의
def main():
    print("### Chap01: 변수와 자료형 예제 실행 ###")
    chap1_1_variables()
    chap1_2_data_types()
    chap1_3_collections()
    chap1_4_type_conversion()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    # 이전 예제의 변수를 사용하기 위해 여기서 선언
    # name = "Alice"
    # age = 25
    # main()

    my_name = "Alice"
    my_age = "25A"
    print(f"이름: {my_name}, 나이: {int(my_age)}")
