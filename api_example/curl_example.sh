#!/usr/bin/env bash

curl http://127.0.0.1:8000/items/1

curl -X POST http://127.0.0.1:8000/items \
-H "Content-Type: application/json" \
-d '{"name": "새로운 아이템"}'

curl http://127.0.0.1:8000/items/3

curl -X PUT http://127.0.0.1:8000/items/1 \
-H "Content-Type: application/json" \
-d '{"name": "수정된 아이템"}'

curl -X DELETE http://127.0.0.1:8000/items/1
