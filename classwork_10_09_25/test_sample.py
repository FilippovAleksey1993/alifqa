import requests
import json

exp_result = 2

header = {"content-type": "application/json"}
response = requests.get(url="https://jsonplaceholder.typicode.com/posts")


def test_check_iser_id():
    user_id_1 = response.json()[0]["userId"]

    assert user_id_1 == 1
