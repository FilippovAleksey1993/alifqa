import requests

from avosend import add_to_cart
from configs import base_url

active_items_url = f"{base_url}/web/client/events/active"  # список активных предложений
delivery_info_base_url = f"{base_url}/web/client/catalog/moderated-offers/"
delivery_info_end_url = "/delivery-time-estimation/duplicate"  # информация о доставке товара
get_item_url = (f"{base_url}/web/client/moderated-offers")  # подробная информация о товаре
# review_item_url = f"{base_url}/{id}/reviews"  # отзывы о товаре
popular_items_url = f"{base_url}/web/client/recommend/offers/v2"  # список популярных товаров
add_to_cart_url  = f"{base_url}/web/client/cart/moderated-items"
get_cart_url = f"{base_url}/web/client/cart/view-cart/duplicate"

def get_active_items():
    response = requests.get(url=f"{base_url}/web/client/events/active")

    return response


def get_item(item_slug: str):
    response = requests.get(url=f"{base_url}/web/client/moderated-offers/{item_slug}")

    return response


def search_items(item_name: str):
    body = {
        "query": item_name
    }

    response = requests.post(url=f"{base_url}/web/client/search/full-text", json=body)

    return response

def get_cart(cookie=None):
    if cookie is None:
        response = requests.get(f"{base_url}/web/client/cart/view-cart/duplicate")
    else:
        headers = {
            'Cookie': f"cart={cookie};"
        }

        response = requests.get(
            url=f"{base_url}/web/client/cart/view-cart/duplicate",
            headers=headers
        )

    return response


def add_to_cart(cookie: str, offer_id: str, condition_id: int, quantity=1):
    headers = {
        'Cookie': f"cart={cookie};"
    }

    body = {
        "moderated_offer_id": offer_id,
        "condition_id": condition_id,
        "quantity": quantity
    }

    response = requests.post(
        url=f"{base_url}/web/client/cart/moderated-items",
        json=body,
        headers=headers
    )

    return response

def get_delivery_info_by_id(moderated_offer_id):
    url = f"{base_url}/web/client/catalog/moderated-offers/{moderated_offer_id}/delivery-time-estimation/duplicate"
    return requests.get(url=url)

def get_reviews_by_id(moderated_offer_id):
    url = f"{base_url}/web/client/catalog/moderated-offers/{moderated_offer_id}/reviews"
    return requests.get(url=url)

def get_popular_offers_v2():
    url = f"{base_url}/web/client/recommend/offers/v2"
    body = {
        "FromApp": "WebAndMobile",
        "FromLayer": "offer_page",
        "Limit": 15
    }
    headers = {"Accept": "application/json"}
    return requests.post(url, json=body, headers=headers)



