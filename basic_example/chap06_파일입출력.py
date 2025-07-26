import csv
import json
import os
import shutil
from pathlib import Path


# 6.1 파일 읽기와 쓰기
def chap6_1_file_io():
    """기본 파일 조작, CSV, JSON 파일 처리 예제를 실행하는 함수"""
    print("--- 6.1 파일 읽기와 쓰기 ---")

    # 6.1.1 기본 파일 조작
    print("\n--- 6.1.1 기본 파일 조작 ---")
    file_name = "example.txt"
    # 파일 쓰기
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("안녕하세요!\n")
        f.write("Python 파일 입출력 예시입니다.\n")
    # 파일 읽기
    with open(file_name, "r", encoding="utf-8") as f:
        print(f.read())
    # 파일 추가 모드
    with open(file_name, "a", encoding="utf-8") as f:
        f.write("추가된 내용입니다.\n")
    with open(file_name, "r", encoding="utf-8") as f:
        print("--- 추가 후 내용 ---")
        print(f.read())

    # 6.1.3 CSV 파일 처리
    print("\n--- 6.1.3 CSV 파일 처리 ---")
    students = [["이름", "나이", "성적"], ["Alice", 20, 85], ["Bob", 22, 92]]
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(students)
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    # 6.1.4 JSON 파일 처리
    print("\n--- 6.1.4 JSON 파일 처리 ---")
    data = {"students": [{"name": "Alice", "age": 20}]}
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open("students.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        print("JSON 파일에서 읽은 데이터:", loaded_data)


# 6.2 디렉토리와 경로 조작
def chap6_2_directory_and_path():
    """os 모듈과 pathlib를 사용한 디렉토리/경로 조작 예제를 실행하는 함수"""
    print("\n--- 6.2 디렉토리와 경로 조작 ---")

    # os 모듈 사용
    test_dir = "test_dir_os"
    os.makedirs(test_dir, exist_ok=True)
    print(f"os.getcwd(): {os.getcwd()}")
    print(f"os.listdir('.'): {os.listdir('.')[:5]}...")  # 일부만 출력

    # pathlib 사용
    path_obj = Path("test_dir_pathlib") / "sub_dir"
    path_obj.mkdir(parents=True, exist_ok=True)
    test_file = path_obj / "test.txt"
    test_file.write_text("pathlib 테스트", encoding="utf-8")
    print(f"pathlib 경로: {test_file}")
    print(f"파일 존재 여부: {test_file.exists()}")


def cleanup():
    """예제 실행 후 생성된 파일과 디렉토리를 정리하는 함수"""
    print("\n--- 생성된 파일 및 디렉토리 정리 ---")
    files_to_remove = ["example.txt", "students.csv", "students.json"]
    dirs_to_remove = ["test_dir_os", "test_dir_pathlib"]

    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"파일 삭제: {file}")

    for directory in dirs_to_remove:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"디렉토리 삭제: {directory}")


# 메인 함수 정의
def main():
    print("### Chap06: 파일 입출력 예제 실행 ###")
    chap6_1_file_io()
    chap6_2_directory_and_path()
    cleanup()
    print("\n### 예제 실행 완료 ###")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main()
