from utils.api_client import get_products
import allure

@allure.feature("Главная страница")
@allure.story("Получение списка товаров")
def test_get_products_status_code():
    response = get_products()
    with allure.step("200"):
        assert response.status_code == 200

@allure.feature("Главная страница")
@allure.story("Проверка содержимого продуктов")
def test_get_products_not_empty():
    response = get_products()
    data = response.json()
    with allure.step("Проверяем что список товаров не пустой"):
        assert len(data['variations']) > 0

@allure.feature("Главная страница")
@allure.story("Проверка структуры ответа")
def test_get_products_has_correct_structure():
    response = get_products()
    data = response.json()

    with allure.step("Проверяем структуру ответа"):
        assert 'totalCount' in data
        assert 'page' in data
        assert 'variations' in data
        assert isinstance(data['variations'], list)