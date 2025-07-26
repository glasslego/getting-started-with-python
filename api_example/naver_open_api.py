import json
from datetime import datetime

import matplotlib.pyplot as plt
import requests

client_id = "HIejdEkOHKAvx3uuwrVC"
client_secret = "JlloWBOLW9"


def fetch_naver_datalab_data(api_url, headers, body):
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(body))
        response.raise_for_status()  # 200번대 응답이 아닐 경우 예외 발생

        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 오류 발생: {http_err}")
        print(f"응답 내용: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"요청 중 오류 발생: {req_err}")
    return None


# 그래프 그리는 함수
def plot_trend_from_json(json_data):
    data = json.loads(json_data)
    trend_data = data["results"][0]["data"]

    dates = [datetime.strptime(entry["period"], "%Y-%m-%d") for entry in trend_data]
    ratios = [entry["ratio"] for entry in trend_data]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, ratios, marker="o", linestyle="-", color="blue")
    plt.title("Search Trend Over Time (Tech Keywords)")
    plt.xlabel("Date")
    plt.ylabel("Interest (0–100)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    """메인 실행 함수"""

    api_url = "https://openapi.naver.com/v1/datalab/search"

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "Content-Type": "application/json",
    }

    # 키워드 설정 (트렌드 조회할 단어들)
    keywords = ["ChatGPT", "AI", "Python"]

    payload = {
        "startDate": "2025-06-01",
        "endDate": "2025-06-30",
        "timeUnit": "date",  # or 'week', 'month'
        "keywordGroups": [{"groupName": "기술", "keywords": keywords}],
        "device": "",  # "pc" or "mo" or "" for all
        "ages": [],  # 예: ["20", "30"] or [] for all
        "gender": "",  # "m", "f", or "" for all
    }

    result = fetch_naver_datalab_data(api_url, headers, payload)
    json_data = json.dumps(result, indent=2, ensure_ascii=False)

    if result:
        print(type(result))
        print(type(json_data))
        # 보기 좋게 출력하기 위해 json.dumps 사용
        print(json_data)

        # 그래프 그리기
        plot_trend_from_json(json_data)


if __name__ == "__main__":
    main()
