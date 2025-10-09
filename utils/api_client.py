import requests
from dotenv import load_dotenv
import os

load_dotenv('E:/Alifqapy/tests/.env')

base_url = os.getenv('base_url')
username = 998903574573
password = os.getenv('password')
security_key = os.getenv('security_key')

auth_token = None
cookie = security_key
session = requests.Session()


def set_auth_token(token):
    global auth_token
    auth_token = f"Bearer {token}"


def set_cookie(cookie_value):
    global cookie
    cookie = cookie_value


def get_products(size=20, page=1):
    url = f"{base_url}/market-api/848/collection-products"
    params = {'size': size, 'page': page}
    headers = {'security-key': cookie} if cookie else {}

    response = session.get(url, params=params, headers=headers)
    return response


def search_products(search_term, size=10):
    url = f"{base_url}/market-api/848/collection-products"
    params = {'search': search_term, 'size': size}
    headers = {'security-key': cookie} if cookie else {}

    response = session.get(url, params=params, headers=headers)
    return response


def login(username, password):

    url = f"{base_url}/security/auth_check"
    data = {
        '_username': username,
        '_password': password,
        '_subdomain': 'gshop'
    }

    response = session.post(url, data=data)

    if response.status_code == 200:
        token = response.json().get('token')
        if token:
            set_auth_token(token)

    return response


def get_profile():
    url = f"{base_url}/market-api/profile"
    headers = {}

    if cookie:
        headers['security-key'] = cookie
    if auth_token:
        headers['Authorization'] = auth_token

    response = session.get(url, headers=headers)
    return response

# 401
def get_profile_unauthorized():
    url = f"{base_url}/market-api/profile"
    response = session.get(url)
    return response