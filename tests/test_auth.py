from utils.api_client import login, get_profile, get_profile_unauthorized
import os
import allure

@allure.parent_suite('Авторизация')
@allure.suite('Проверка доступа без авторизации')
def test_get_profile_unauthorized():
    response = get_profile_unauthorized()
    with allure.step("401"):
        assert response.status_code == 401

@allure.parent_suite('Авторизация')
@allure.suite('Успешный вход в систему')
def test_login_success():
    username = 998903574573
    password = 340340
    response = login(username, password)

    assert response.status_code == 200
    with allure.step("Авторизовано и получен токен"):
        assert 'token' in response.json()

@allure.parent_suite('Авторизация')
@allure.suite('Доступ к профилю после авторизации')
def test_get_profile_authorized():
    username = 998903574573
    password = 340340
    login_response = login(username, password)
    assert login_response.status_code == 200

    profile_response = get_profile()
    with allure.step("200"):
        assert profile_response.status_code == 200
