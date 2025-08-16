"""
HTTP/HTTPS 크로스 프로토콜 요청 예시
파이썬에서 requests 라이브러리를 사용한 다양한 시나리오
"""

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# SSL 인증서 경고 비활성화 (테스트 목적)
urllib3.disable_warnings(InsecureRequestWarning)


def http_to_https():
    """
    시나리오 1: HTTP 클라이언트에서 HTTPS 서버로 요청
    결과: ✅ 정상 작동 (대부분의 경우)
    """
    print("=" * 60)
    print("🔓➡️🔒 HTTP 클라이언트에서 HTTPS 서버로 요청")
    print("=" * 60)

    try:
        # HTTPS API에 요청 (GitHub API 예시)
        response = requests.get("https://api.github.com/users/octocat")

        print("✅ 요청 성공!")
        print(f"상태 코드: {response.status_code}")
        print(f"응답 데이터 일부: {response.json()['login']}")
        print(f"요청 URL: {response.url}")
        print("실제 사용된 프로토콜: HTTPS")

    except requests.exceptions.RequestException as e:
        print(f"❌ 요청 실패: {e}")


def https_to_http():
    """
    시나리오 2: HTTPS 환경에서 HTTP 서버로 요청
    결과: ⚠️ 보안 경고가 있지만 파이썬에서는 대부분 작동
    (브라우저에서는 차단될 수 있음)
    """
    print("\n" + "=" * 60)
    print("🔒➡️🔓 HTTPS 환경에서 HTTP 서버로 요청")
    print("=" * 60)

    try:
        # HTTP API에 요청 (HTTPBin 예시)
        response = requests.get("http://httpbin.org/get")

        print("⚠️ 요청 성공하지만 보안 위험!")
        print(f"상태 코드: {response.status_code}")
        print(f"요청 URL: {response.url}")
        print("실제 사용된 프로토콜: HTTP (암호화되지 않음)")
        print("⚠️ 경고: 데이터가 평문으로 전송됨!")

    except requests.exceptions.RequestException as e:
        print(f"❌ 요청 실패: {e}")


def protocol_redirect():
    """
    시나리오 3: HTTP로 요청했지만 HTTPS로 리다이렉트되는 경우
    결과: ✅ 자동으로 HTTPS로 전환됨
    """
    print("\n" + "=" * 60)
    print("🔄 HTTP 요청 → HTTPS 리다이렉트")
    print("=" * 60)

    try:
        # HTTP로 요청하지만 HTTPS로 리다이렉트되는 사이트
        response = requests.get("http://github.com", allow_redirects=True)

        print("✅ 리다이렉트 성공!")
        print(f"최종 상태 코드: {response.status_code}")
        print("요청한 URL: http://github.com")
        print(f"최종 URL: {response.url}")
        print(f"리다이렉트 횟수: {len(response.history)}")

        # 리다이렉트 히스토리 출력
        for i, redirect in enumerate(response.history):
            print(
                f"  리다이렉트 {i + 1}: {redirect.status_code} → {redirect.headers.get('Location', 'N/A')}"  # noqa: E501
            )

    except requests.exceptions.RequestException as e:
        print(f"❌ 요청 실패: {e}")


def mixed_content_simulation():
    """
    시나리오 4: Mixed Content 시뮬레이션
    HTTPS 페이지에서 HTTP 리소스를 로드하는 상황
    """
    print("\n" + "=" * 60)
    print("🚫 Mixed Content 시뮬레이션")
    print("=" * 60)

    # HTTPS 사이트에서 페이지 정보 가져오기
    try:
        https_response = requests.get("https://httpbin.org/get")
        print(f"✅ HTTPS 메인 페이지 로드 성공: {https_response.status_code}")

        # 동일한 세션에서 HTTP 리소스 요청 시도
        session = requests.Session()

        # HTTPS 요청
        https_resp = session.get("https://httpbin.org/get")
        print(f"✅ 세션에서 HTTPS 요청: {https_resp.status_code}")

        # HTTP 요청 (Mixed Content 상황)
        http_resp = session.get("http://httpbin.org/get")
        print(f"⚠️ 세션에서 HTTP 요청: {http_resp.status_code}")
        print("⚠️ 경고: 실제 브라우저에서는 이런 Mixed Content가 차단될 수 있음!")

    except requests.exceptions.RequestException as e:
        print(f"❌ 요청 실패: {e}")


def ssl_verification():
    """
    시나리오 5: SSL 인증서 검증 관련
    """
    print("\n" + "=" * 60)
    print("🔐 SSL 인증서 검증 테스트")
    print("=" * 60)

    # 정상적인 HTTPS 사이트 (인증서 검증 성공)
    try:
        response = requests.get("https://httpbin.org/get", verify=True)
        print(f"✅ SSL 인증서 검증 성공: {response.status_code}")
    except requests.exceptions.SSLError as e:
        print(f"❌ SSL 인증서 검증 실패: {e}")

    # 자체 서명 인증서 사이트 (인증서 검증 실패 예상)
    try:
        # verify=False로 SSL 검증 비활성화
        response = requests.get(
            "https://self-signed.badssl.com/", verify=False, timeout=10
        )
        print(f"⚠️ SSL 검증 비활성화로 요청 성공: {response.status_code}")
        print("⚠️ 경고: 실제 운영환경에서는 verify=False 사용 금지!")
    except requests.exceptions.RequestException as e:
        print(f"❌ 자체 서명 인증서 사이트 요청 실패: {e}")


def different_ports():
    """
    시나리오 6: 다른 포트를 사용하는 경우
    """
    print("\n" + "=" * 60)
    print("🔌 다른 포트 사용 시나리오")
    print("=" * 60)

    # 표준 포트가 아닌 포트 사용
    urls = [
        "https://httpbin.org:443/get",  # HTTPS 표준 포트
        "http://httpbin.org:80/get",  # HTTP 표준 포트
    ]

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            protocol = "HTTPS" if url.startswith("https") else "HTTP"
            port = url.split(":")[2].split("/")[0]
            print(f"✅ {protocol} 포트 {port} 요청 성공: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ {url} 요청 실패: {e}")


def demonstrate_best_practices():
    """
    모범 사례 및 권장사항
    """
    print("\n" + "=" * 60)
    print("💡 모범 사례 및 권장사항")
    print("=" * 60)

    test_url = "https://httpbin.org/json"

    print("1. ✅ 항상 HTTPS 사용:")
    response = requests.get(test_url)
    print(response.status_code)
    print(response.json())

    print("\n2. ✅ SSL 인증서 검증 활성화:")
    response = requests.get(test_url, verify=True)
    print(response.status_code)
    print(response.json())

    print("\n3. ✅ 타임아웃 설정:")
    response = requests.get(test_url, timeout=10)
    print(response.status_code)
    print(response.json())

    print("\n4. ✅ 세션 사용으로 성능 향상:")
    # requests.Session()은 HTTP 연결을 재사용할 수 있게 해주는 객체
    session = requests.Session()
    response = session.get(test_url)
    print(response.status_code)
    print(response.json())

    print("\n5. ❌ 피해야 할 것들:")
    print("   - verify=False 사용 (운영환경에서)")
    print("   - HTTP 사용 (민감한 데이터 전송 시)")
    print("   - Mixed Content (HTTPS 페이지에서 HTTP 리소스 로드)")


if __name__ == "__main__":
    print("HTTP/HTTPS 크로스 프로토콜 요청 테스트")
    print("=" * 60)

    http_to_https()
    https_to_http()
    protocol_redirect()
    mixed_content_simulation()
    ssl_verification()
    different_ports()
    demonstrate_best_practices()
