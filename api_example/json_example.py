import json
import os

"""

Serialization(직렬화): Python 객체 → JSON 문자열
Deserialization(역직렬화): JSON 문자열 → Python 객체
"""


def chap2_1_json_basics():
    """Python 객체와 JSON 문자열 간의 변환(직렬화/역직렬화) 예제를 실행합니다."""
    print("--- 2.1 JSON 모듈 기본 사용법 ---")

    # 1. Python 객체를 JSON 문자열로 변환 (직렬화)
    data = {"name": "Alice", "age": 25, "is_student": False, "grades": [85, 92, 78]}
    json_string = json.dumps(data, indent=2, ensure_ascii=False)
    print("Python dict를 JSON 문자열로 변환:")
    print(json_string)

    # 2. JSON 문자열을 Python 객체로 변환 (역직렬화)
    json_text = '{"name": "Bob", "age": 30, "hobbies": ["music", "sports"]}'
    python_obj = json.loads(json_text)
    print("\nJSON 문자열을 Python dict로 변환:")
    print(python_obj)
    print(f"이름: {python_obj['name']}")


def chap2_2_json_file_io():
    """JSON 파일을 읽고 쓰는 예제를 실행합니다."""
    print("\n--- 2.2 JSON 파일 읽기와 쓰기 ---")

    students_data = {
        "course": "Python Programming",
        "students": [
            {
                "id": 1,
                "name": "Alice",
                "grades": {"midterm": 85, "final": 92},
                "active": True,
            },
            {
                "id": 2,
                "name": "Bob",
                "grades": {"midterm": 78, "final": 88},
                "active": False,
            },
        ],
    }

    # 파일에 JSON 데이터 쓰기
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students_data, f, ensure_ascii=False, indent=2)
    print("students.json 파일이 생성되었습니다.")

    # 파일에서 JSON 데이터 읽기
    with open("students.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    print("\n파일에서 읽어온 학생 목록:")
    for student in loaded_data["students"]:
        status = "재학" if student["active"] else "휴학"
        print(f"  - {student['name']} ({status})")


def cleanup_files():
    """예제 실행으로 생성된 파일을 정리합니다."""
    print("\n--- 생성된 파일 정리 ---")
    files_to_remove = ["students.json", "students_updated.json", "config.json"]
    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"'{filename}' 파일이 삭제되었습니다.")


def main():
    """메인 실행 함수"""
    print("### JSON 모듈 예제 실행 ###")
    chap2_1_json_basics()
    chap2_2_json_file_io()
    cleanup_files()
    print("\n### 모든 예제 실행 완료 ###")


if __name__ == "__main__":
    main()
