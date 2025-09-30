import json
import pytest
import requests

base_url = "https://gw.alifshop.uz"

active_items_url = f"{base_url}/web/client/events/active"
get_item = f"{base_url}/web/client/moderated-offers"
search_url = f"{base_url}/web/client/search/full-text"
get_cart_url = f"{base_url}/web/client/cart/view-cart/duplicate"
add_cart_url = f"{base_url}/web/client/cart/moderated-items"


def test_get_session_id():

    global cookie

    response = requests.get(url=get_cart_url)

    cookie = response.cookies.get_dict()["cart"]
    # assert isinstance(cookie, str)


def test_add_item():

    header = {"Cookie": f"cart={cookie};"}

    body = {
        "moderated_offer_id": "a57a02e4-cbb0-476b-ab3e-713a1682ef1d",
        "condition_id": 40268,
        "quantity": 1,
    }
    response = requests.post(url=add_cart_url, json=body, headers=header)
    assert response.status_code == 200

    response = response.json()
    print(json.dumps(response, indent=2))

    # print(response.cookies.get_dict()["cart"])  # из дикт взяли данные по ключу карт
    # print(response.headers["Set-Cookie"])  # то же только из хэдэрс
    # print(response.json.get_dict()["cart"])
    # return response.cookies.get_dict()["cart"]


# @pytest.mark.parametrize(
#     "item", ["iphone", "samsung", "8789798798797897987987987", "xiaomi"]
# )
# def test_search(item):
#     search_body = {"query": item}
#     response = requests.post(url=search_url, json=search_body)
#     res_json = response.json()

#     items_list = res_json["items"]  # берем итемс из джейсона

#     print(f"{items_list}\n\n")

#     assert len(items_list) > 0, "no data"

#     # print(json.dumps(res_json, indent=2))


# test_search("item")
test_get_session_id()
test_add_item()
