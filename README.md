# getting-started-with-python

파이썬 기초 예제를 단계적으로 학습할 수 있도록 구성한 저장소입니다. 각 챕터는 독립적으로 실행 가능하며, 실습 위주로 따라하며 익힐 수 있도록 간단한 예제와 주석을 포함합니다.

## 환경 설정
- Python 3.11 이상
- Poetry 사용 권장 (프로젝트 의존성/실행 관리)

설치:
1) Poetry 설치가 안되어 있다면 https://python-poetry.org/docs/#installation 참고
2) 프로젝트 의존성 설치
```
poetry install
```
3) 가상환경 진입
```
poetry shell
```

의존성은 pyproject.toml에 정의되어 있으며, 예제 실행에 필요한 requests, Flask, pytest, ruff 등 기본 도구가 포함되어 있습니다.

## 예제 실행 방법
- 개별 파일을 직접 실행하거나, 각 챕터 파일의 main()을 실행하세요.
- 모든 예제는 프로젝트 루트에서 실행하는 것을 권장합니다.

예시:
```
# 기본 문법
python basic_example/chap01_variable_type.py
python basic_example/chap02_조건문과 반복문.py
python basic_example/chap03_함수.py
python basic_example/chap04_클래스와 객체지향.py
python basic_example/chap05_모듈과 패키지.py
python basic_example/chap06_파일입출력.py
python basic_example/chap07_내장 함수와 표준 라이브러리.py
python basic_example/chap08_예외처리.py
python basic_example/chap09_테스트.py
python basic_example/chap10_고급자료구조.py
python basic_example/chap11_비동기프로그래밍.py
python basic_example/chap12_제너레이터와이터레이터.py

# 패키지 사용 예시
python my_package/use_calculator.py

# API/JSON 예시
python api_example/json_example.py
python api_example/http_example.py
python api_example/simple_server_example.py  # 로컬 서버 실행 (Flask)
```

Flask 서버 실행 후 테스트:
- 서버: http://127.0.0.1:8000
- 엔드포인트: GET /items, POST /items, GET/PUT/DELETE /items/<id>

## 학습 로드맵 제안
1. 변수/자료형 (basic_example/chap01_variable_type.py) ✓
2. 조건/반복 (chap02) ✓
3. 함수 (chap03) ✓
4. 클래스/객체지향 (chap04) ✓
5. 모듈/패키지 (chap05) ✓
6. 파일 입출력 (chap06) ✓
7. 내장함수/표준라이브러리 (chap07) ✓
8. 예외처리 (chap08) ✓
9. 테스트 (chap09) ✓
10. 고급 자료구조 (chap10) ✓
11. 비동기 프로그래밍 (chap11) ✓
12. 제너레이터/이터레이터 (chap12) ✓
13. 확장 예제 (advanced_example/*, api_example/*) ✓

## 네트워크/보안 주의사항
- api_example/http_example.py는 다양한 HTTP/HTTPS 시나리오를 보여줍니다.
  - 네트워크가 불안정하거나 외부 서비스 접근이 제한된 환경에서는 요청이 실패할 수 있습니다.
  - verify=False는 학습용으로만 사용하고, 운영 환경에서는 사용하지 마세요.
- simple_server_example.py는 로컬에서만 접근되는 학습용 서버입니다.

## 추천 강화 포인트(이미 반영/가이드)
- 주석과 타입 힌트: 예제 전반에 개념 설명 주석 및 일부 타입 힌트가 포함되어 있습니다.
- 예외 안전성: chap01에서 잘못된 타입 변환 사례를 try/except로 안전하게 시연합니다. 자세한 내용은 chap08에서 다룹니다.
- 실행 가이드: 본 README에 실행 순서, 방법, 주의사항을 정리했습니다.

## 테스트 실행
- chap09_테스트.py 또는 pytest를 활용해 간단한 단위 테스트를 시도해보세요.
```
pytest -q
```

## 코드 포맷팅 / 린트(선택)
- 포맷터: black
- 린터: ruff 또는 flake8
```
ruff check .
black .
```

## 문의/개선 제안
학습 중 개선 아이디어가 떠오르면 이슈로 남기거나 PR을 올려주세요. 초심자 관점에서 더 쉬운 설명과 예제가 꾸준히 보강될 예정입니다.
