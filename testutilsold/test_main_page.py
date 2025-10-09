
import pytest
import requests
import json
from utils.main_page.api import (
    get_cart,
    add_to_cart,
    get_active_items,
    get_item,
    get_delivery_info_by_id,
    get_reviews_by_id,
    get_popular_offers_v2,
)
import allure
from utils.functions import attach_reqres

# хардкод чисто для тестов
offer_id = "262286"
condition_id = "32961"

@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в корзину у неавторизованного пользователя')
@allure.title("Получение session_id из куки")
def test_get_session_id():
    global cookie
    with allure.step('Отправка запроса на получение корзины'):
        response = get_cart()
        attach_reqres(response=response)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

    with allure.step("Получение session_id из куки"):
        cookie = response.cookies.get_dict()['cart']
        assert isinstance(cookie, str), f'Тип куки на самом деле {type(cookie)}'

@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в корзину у неавторизованного пользователя')
@allure.title("Добавление товара в корзину")
def test_add_item():
    response = add_to_cart(cookie=cookie, offer_id=offer_id, condition_id=condition_id)
    # print(cookie)
    attach_reqres(response=response)

    assert response.status_code == 200

    response = response.json()
    print(json.dumps(response, indent=4))

@allure.parent_suite('Каталог')
@allure.suite('Активные офферы')
@allure.title("/events/active - первый offer")
def test_active_items_pick_first():
    global FIRST_ID, FIRST_SLUG

    resp = get_active_items()
    attach_reqres(resp)
    assert resp.status_code == 200

    data = resp.json()
    first_offer = data[0]["offers"][0]

    FIRST_ID = str(first_offer["moderated_offer_id"])
    FIRST_SLUG = first_offer["slug"]

    assert FIRST_ID and FIRST_SLUG
    assert float(first_offer["price"]) > 0


@allure.parent_suite('Каталог')
@allure.suite('Доставка')
@allure.title("/delivery-time-estimation")
def test_delivery_info():
    resp = get_delivery_info_by_id(FIRST_ID)
    attach_reqres(resp)
    assert resp.status_code == 200

    payload = resp.json()
    assert int(payload["days_to_deliver"]) >= 0
    assert str(payload["moderated_offer_id"])
    assert str(payload["delivery_time"]).strip()


@allure.parent_suite('Каталог')
@allure.suite('Карточка товара')
@allure.title("/moderated-offers/{slug}")
def test_moderated_offer_details():
    resp = get_item(FIRST_SLUG)
    attach_reqres(resp)
    assert resp.status_code == 200

    item = resp.json()
    # print(f"Полный ответ: {item}")  # для диагностики

    price = float(item["moderated_offer"]["price"])
    assert price > 0
    assert item["moderated_offer"]["name"]

    old_price = item["moderated_offer"]["old_price"]
    if old_price:
        assert float(old_price) >= price
        discount =item["moderated_offer"]["discount"]
        if discount is not None and float(discount) < 0:
            assert price < float(old_price)


@allure.parent_suite('Каталог')
@allure.suite('Отзывы')
@allure.title("/catalog/moderated-offers/{id}/reviews")
def test_reviews():
    resp = get_reviews_by_id(FIRST_ID)
    attach_reqres(resp)
    assert resp.status_code == 200, "нет отзывов"

    data = resp.json()
    total = data.get("total")
    reviews = data.get("offer_reviews", [])
    if total and total > 0:
        assert len(reviews) > 0


@allure.parent_suite('Каталог')
@allure.suite('Популярные офферы')
@allure.title("/offers/v2")
# def test_popular_offers():
#     resp = get_popular_offers_v2()
#     attach_reqres(resp)
#     assert resp.status_code == 200
#
#     payload = resp.json()
#     offers = payload.get("offers") or payload.get("items") or []
#     assert len(offers) > 0
#
#     o0 = offers[0]
#     partner = o0.get("partner", {})
#     assert partner.get("name")
#     assert "rating" in partner
#
#     conditions = o0.get("conditions") or o0.get("installments") or []
#     assert len(conditions) > 0
#     assert "duration" in conditions[0]
#     assert "commission" in conditions[0]
def test_popular_offers():
    resp = get_popular_offers_v2()

    # Детальная диагностика
    print("=== REQUEST ===")
    print("URL:", resp.request.url)
    print("Method:", resp.request.method)
    print("Headers:", dict(resp.request.headers))
    print("Body:", resp.request.body)




    print("=== RESPONSE ===")
    print("Status Code:", resp.status_code)
    print("Response Headers:", dict(resp.headers))
    print("Response Body:", resp.text)

    attach_reqres(resp)
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}. Response: {resp.text}"








# @pytest.mark.parametrize('item', ['iPhone', 'samsung', '8716248712648712648172648127','xiaomi'])
# def test_search(item):
#     search_body = {
#         "query": item
#     }
#
#     response = requests.post(url=search_url, json=search_body)
#     res_json = response.json()
#
#     items_list = res_json["items"]
#
#     print(f'{items_list}\n\n')
#
#     assert response.status_code == 200
#     assert len(items_list) > 0, "Ничего не нашлось"


# def url_generator(slug):
#     return f'{get_item}/{slug}'


# def test_active_items():
#     global item_slug
#
#     response = requests.get(url=active_items_url)
#
#     assert response.status_code == 200
#
#     response = response.json()
#
#     item_slug = response[0]['offers'][0]['slug']
#     print(item_slug)
#
#
# def test_get_item():
#     url = url_generator(item_slug)
#
#     response = requests.get(url=url)
#
#     print(response.json())

