import json

import requests

# API 기본 URL
BASE_URL = "https://jsonplaceholder.typicode.com"
headers = {"Content-Type": "application/json"}


def print_response(response):
    """응답 정보 출력"""
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response.elapsed.total_seconds():.2f}초")

    try:
        data = response.json()
        print("   Response Data:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"   Response Text: {response.text}")
        print(f"   Response Exception: {e}")
    print("-" * 50)


# GET - 데이터 가져오기
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        all_posts = response.json()
        posts = all_posts[:5]  # 처음 5개 게시글만 가져오기
        for i, post in enumerate(posts, start=1):
            print(f"      {i}. ID: {post['id']}, 제목: {post['title'][:30]}...")
            # print(post)
        return all_posts

    else:
        print(f"오류 발생: {response.status_code}")


def get_post_by_id(post_id):
    print(f"id:{post_id} 게시글 조회")
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print_response(response)


def get_post_by_user_id(user_id):
    print(f"user_id:{user_id} 게시글 조회")
    response = requests.get(f"{BASE_URL}/posts?userId={user_id}")
    if response.status_code == 200:
        print_response(response)


# POST - 새 데이터 생성
def create_new_post():
    """새 게시글 생성"""
    data = {
        "title": "API 연습",
        "body": "JSONPlaceholder를 사용해서 POST 요청을 연습",
        "userId": 1004,
    }
    response = requests.post(f"{BASE_URL}/posts", headers=headers, json=data)
    if response.status_code == 201:
        print_response(response)
        post = response.json()
        print(f"새 게시글이 생성되었습니다. ID: {post['id']}")
        return post
    else:
        print(f"오류 발생: {response.status_code}")


# PUT - 데이터 수정
def update_post():
    data = {
        "id": 1,
        "title": "API PUT 연습",
        "body": "PUT 요청으로 포스트의 모든 내용을 새롭게 바꿨습니다. 제목과 본문이 모두 새로운 내용으로 교체됩니다.",
        "userId": 1005,
    }
    response = requests.put(f"{BASE_URL}/posts/{1}", headers=headers, json=data)
    if response.status_code == 200:
        post = response.json()
        print_response(response)
        return post
    else:
        print(f"수정 실패: {response.status_code}")
        print(f"수정 실패: {response.text}")


# DELETE - 데이터 삭제
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"게시글 {post_id}가 삭제되었습니다.")
    else:
        print(f"삭제 실패: {response.status_code}")


if __name__ == "__main__":
    # 1. 게시글 목록 가져오기
    posts = get_posts()
    get_post_by_id(1)
    get_post_by_user_id(1)

    # 2. 새 게시글 생성
    new_post = create_new_post()
    post_id = new_post["id"]
    user_id = new_post["userId"]
    print(post_id)
    get_post_by_id(post_id)
    get_post_by_user_id(user_id)

    # 3. 게시글 수정
    updated_post = update_post()
    get_post_by_id(1)

    # # 4. 게시글 삭제
    delete_post(post_id)
