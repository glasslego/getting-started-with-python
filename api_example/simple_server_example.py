import json

from flask import Flask, Response, jsonify, request

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# 임시 데이터 저장소
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]


# JSON 응답 시 한글 깨짐 방지용 커스텀 함수
def custom_jsonify(data, status=200):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status=status,
        mimetype="application/json; charset=utf-8",
    )


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Item API!"


# GET: 모든 아이템 가져오기
@app.route("/items", methods=["GET"])
def get_items():
    return custom_jsonify(items)


# GET: 특정 아이템 가져오기
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return custom_jsonify({"error": "Item not found"}), 404
    return custom_jsonify(item)


# POST: 아이템 추가하기
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    new_item = {"id": items[-1]["id"] + 1 if items else 1, "name": data["name"]}
    items.append(new_item)
    return custom_jsonify(new_item), 201


# PUT: 특정 아이템 수정하기
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return custom_jsonify({"error": "Item not found"}), 404

    item["name"] = data["name"]
    return jsonify(item)


# DELETE: 특정 아이템 삭제하기
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return custom_jsonify({"result": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
