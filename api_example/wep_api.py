import requests

# API 기본 URL
BASE_URL = "https://jsonplaceholder.typicode.com"


# GET - 데이터 가져오기
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        print(f"게시글 {len(posts)}개를 가져왔습니다.")
        return posts
    else:
        print(f"오류 발생: {response.status_code}")


# POST - 새 데이터 생성
def create_post(title, body):
    data = {"title": title, "body": body, "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    if response.status_code == 201:
        new_post = response.json()
        print(f"새 게시글이 생성되었습니다. ID: {new_post['id']}")
        return new_post
    else:
        print(f"생성 실패: {response.status_code}")


# PUT - 데이터 수정
def update_post(post_id, title, body):
    data = {"id": post_id, "title": title, "body": body, "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    if response.status_code == 200:
        updated_post = response.json()
        print(f"게시글 {post_id}가 수정되었습니다.")
        return updated_post
    else:
        print(f"수정 실패: {response.status_code}")


# DELETE - 데이터 삭제
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"게시글 {post_id}가 삭제되었습니다.")
    else:
        print(f"삭제 실패: {response.status_code}")


# 사용 예시
if __name__ == "__main__":
    # 1. 게시글 목록 가져오기
    posts = get_posts()

    # 2. 새 게시글 생성
    new_post = create_post("테스트 제목", "테스트 내용입니다.")

    # 3. 게시글 수정
    if new_post:
        update_post(new_post["id"], "수정된 제목", "수정된 내용입니다.")

    # 4. 게시글 삭제
    if new_post:
        delete_post(new_post["id"])
