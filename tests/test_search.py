from utils.api_client import search_products
from utils.helpers import get_first_product_name
import allure

@allure.feature("Поиск товаров")
@allure.story("Поиск Varmilo")
def test_search_varmilo_status_code():
    response = search_products('Varmilo')
    with allure.step("200"):
         assert response.status_code == 200

@allure.feature("Поиск товаров")
@allure.story("Проверка результатов поиска")
def test_search_varmilo_contains_term():
    response = search_products('Varmilo')
    data = response.json()

    assert len(data['variations']) > 0
    with allure.step("Проверяем что первый продукт содержит 'Varmilo'"):
        first_product_name = get_first_product_name(data)
        assert 'Varmilo' in first_product_name