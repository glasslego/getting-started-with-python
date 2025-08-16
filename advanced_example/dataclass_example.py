import json
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional


@dataclass
class Student:
    name: str
    age: int
    grades: Dict[str, int]
    subjects: List[str]
    enrollment_date: Optional[str] = None
    student_id: Optional[str] = None
    email: Optional[str] = None

    def to_json(self):
        """객체를 JSON 문자열로 변환"""
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)

    @classmethod
    def from_json(cls, json_str: str):
        """JSON 문자열에서 객체 생성"""
        try:
            data = json.loads(json_str)
            return cls.from_dict(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"유효하지 않은 JSON 형식: {e}")

    @classmethod
    def from_dict(cls, data: dict):
        """딕셔너리에서 객체 생성 (유연한 필드 매핑)"""
        try:
            # 필수 필드 매핑
            mapped_data = {
                "name": data.get("name")
                or data.get("full_name")
                or data.get("student_name"),
                "age": data.get("age") or data.get("student_age"),
                "grades": data.get("grades") or data.get("scores") or {},
                "subjects": data.get("subjects")
                or data.get("courses")
                or data.get("enrolled_subjects")
                or [],
            }

            # 선택적 필드 매핑
            if "enrollment_date" in data or "enroll_date" in data:
                mapped_data["enrollment_date"] = data.get(
                    "enrollment_date"
                ) or data.get("enroll_date")

            if "student_id" in data or "id" in data:
                mapped_data["student_id"] = str(
                    data.get("student_id") or data.get("id")
                )

            if "email" in data or "student_email" in data:
                mapped_data["email"] = data.get("email") or data.get("student_email")

            # None 값 제거
            mapped_data = {k: v for k, v in mapped_data.items() if v is not None}

            return cls(**mapped_data)
        except TypeError as e:
            raise ValueError(f"데이터가 Student 객체와 맞지 않음: {e}")


if __name__ == "__main__":
    student = Student(
        name="박민수",
        age=20,
        grades={"수학": 88, "영어": 92, "과학": 85},
        subjects=["컴퓨터과학", "수학", "물리학"],
    )

    print(student)

    # Dataclass 직렬화
    student_json = student.to_json()
    print("\n📄 Student JSON:")
    print(student_json)

    # Dataclass 역직렬화
    restored_student = Student.from_json(student_json)
    print("\n🔄 복원된 Student:")
    print(restored_student)
    print(f"동일한 객체인가? {student == restored_student}")
