from utils.api_client import login, get_profile
from utils.helpers import validate_phone_number
import os


def test_profile_structure():
    username = 998903574573
    password = os.getenv('password')
    login(username, password)

    response = get_profile()
    data = response.json()

    if response.status_code == 200:
        assert 'id' in data
        assert 'username' in data
        assert 'profile' in data
    else:
        assert 'code' in data
        assert 'message' in data


def test_phone_number_format():
    username = 998903574573
    password = os.getenv('password')
    login(username, password)

    response = get_profile()
    data = response.json()

    if response.status_code == 200 and 'profile' in data:
        if data['profile'].get('phoneNumbers') and len(data['profile']['phoneNumbers']) > 0:
            phone_number = data['profile']['phoneNumbers'][0]
            assert validate_phone_number(phone_number)


def test_profile_data_exists():
    username = 998903574573
    password = os.getenv('password')
    login(username, password)

    response = get_profile()
    data = response.json()

    if response.status_code == 200:
        assert data['id'] is not None
        assert data['username'] is not None
        if 'firstName' in data['profile']:
            assert data['profile']['firstName'] is not None