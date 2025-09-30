import requests
import json

base_url = "https://gw.alifshop.uz"

active_items_url = f"{base_url}/web/client/events/active"  # список активных предложений
delivery_info_base_url = f"{base_url}/web/client/catalog/moderated-offers/"
delivery_info_end_url = "/delivery-time-estimation/duplicate"  # информация о доставке товара
get_item_url = (f"{base_url}/web/client/moderated-offers")  # подробная информация о товаре
# review_item_url = f"{base_url}/{id}/reviews"  # отзывы о товаре
popular_items_url = f"{base_url}/web/client/recommend/offers/v2"  # список популярных товаров

def test_popular_items():
    offers_body = {
        "user_id": None,
        "from_app": "WebAndMobile",
        "from_layer": "offer_page",
        "limit": 10
    }

    response = requests.post(popular_items_url, headers={"Accept": "application/json"}, json=offers_body)
    # print(popular_items_url, response.status_code, response.text)

    assert response.status_code == 200
    response = response.json()
    offers = response["offers"]
    assert len(offers) > 0

    assert offers[0]["partner"]["name"]
    assert "rating" in offers[0]['partner']

    conditions = offers[0]['conditions']
    assert len(conditions) > 0

    for cond in conditions:
        int(cond["duration"])
        int(cond["commission"])

    raznie_variki = {(cond["duration"], cond["commission"]) for cond in conditions}
    assert len(raznie_variki) >= 2

def test_review_item():
    response = requests.get(active_items_url)
    assert response.status_code == 200
    offer_id = response.json()[0]["offers"][0]["moderated_offer_id"]

    response = requests.get(f"{base_url}/web/client/catalog/moderated-offers/{offer_id}/reviews")
    assert response.status_code in (200, 404)

    if response.status_code == 200:
        response = response.json()
        total = int(response["meta"]["total"])
        reviews = response.get("offer_reviews", [])

        if total > 0:
            assert len(reviews) > 0
        else:
            assert isinstance(reviews, list)


def test_get_item_info():
    response = requests.get(url=f"{active_items_url}")
    assert response.status_code == 200
    response = response.json()

    first_offer = response[0]["offers"][0]
    slug = first_offer["slug"]

    response = requests.get(url_generator(slug))
    assert response.status_code == 200
    item = response.json()

    # print(json.dumps(item, indent=2, ensure_ascii=False))

    assert item["moderated_offer"]["name"]
    # print('')
    # print(f'\nNAME - {item["moderated_offer"]["name"]}')
    price = item["moderated_offer"]["price"]
    # print(f'PRICE - {price}')
    assert price > 0
    images = item["moderated_offer"]["images"]
    # print(f'IMAGES - {len(images)}')
    assert len(images) > 0
    discount = item["moderated_offer"].get("discount")
    # print(f'DISCOUNT - {discount}')
    # print('')
    assert discount <= 0
    if discount < 0:
        old_price = item["moderated_offer"]["old_price"]
        assert price < old_price
    # print(f"{price} < {old_price}")

def url_generator(slug):  # url_by_slug(slug):
    return f"{get_item_url}/{slug}"


def test_delivery_info():
    response = requests.get(url=f"{active_items_url}")
    assert response.status_code == 200
    response = response.json()
    global test_id
    test_id = response[0]["offers"][0]["moderated_offer_id"]
    item_id = response[0]["offers"][0]["moderated_offer_id"]
    delivery_url = f"{delivery_info_base_url}{item_id}{delivery_info_end_url}"
    response = requests.get(url=f"{delivery_url}")
    global delivery_info
    delivery_info = response.json()
    # print(f"{response}")
    # delivery_info = ["delivery_time"]
    # print(f"{delivery_info}\n\n")
    # print(delivery_info["delivery_time"])


def test_delivery_id_time_days():
    assert delivery_info["days_to_deliver"] >= 0
    assert len(delivery_info["moderated_offer_id"]) > 0
    assert len(delivery_info["delivery_time"]) > 0


def test_active_items():
    # global item_slug

    response = requests.get(url=f"{active_items_url}")
    assert response.status_code == 200

    # print(f"{response.headers}\n\n")
    # print(f"{response.status_code}\n\n")
    # print(f"{response.content}\n\n")

    response = response.json()
    # print(json.dumps(response, indent=2))  # для красоты

    # try:
    # id = response[0]["id"]
    # except KeyError:
    #     raise ValueError("не пришел ключ 'lol'")

    # print(f"id: {id}")

    # item_slug = response[0]["offers"][0]["name"]
    # print(f"{item_slug}\n\n")

    global offers
    offers = []

    for i in response:
        if "offers" in i:
            for offer in i["offers"]:
                offers.append(offer)

    assert len(offers) > 0, "список активных предложений пустой"
    # print(offers[0])


def test_id_name_price_partner():
    assert len(offers[0]["moderated_offer_id"]) > 0
    assert len(offers[0]["name"]) > 0
    assert offers[0]["price"] > 0
    assert len(offers[0]["partner"]) > 0



# def test_get_item():
#     url = url_generator(item_slug)
#     response = requests.get(url=url)

#     print(f"{response.json()}checkckeck")


# test_active_items()
# # test_get_item()
# test_delivery_info()
