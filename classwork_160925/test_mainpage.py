import json
import requests

base_url = "https://gw.alifshop.uz"

active_items_url = f"{base_url}/web/client/events/active"
get_item = f"{base_url}/web/client/moderated-offers"


def url_generator(slug):
    return f"{get_item}/slug"


def test_active_items():
    global item_slug

    response = requests.get(url=f"{active_items_url}")

    assert response.status_code == 200

    # print(f"{response.headers}\n\n")
    # print(f"{response.status_code}\n\n")
    # print(f"{response.content}\n\n")

    response = response.json()
    print(json.dumps(response, indent=2))  # для красоты

    # try:
    # id = response[0]["id"]
    # except KeyError:
    #     raise ValueError("не пришел ключ 'lol'")

    # print(f"id: {id}")

    item_slug = response[0]["offers"][0]["slug"]
    # print(item_slug)


def test_get_item():
    url = url_generator(item_slug)
    response = requests.get(url=url)

    # print(f"{response.json()}checkckeck")
