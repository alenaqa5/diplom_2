import allure
import pytest
import api_steps.order.payload
from api_steps.order.order import Order


class TestOrder:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize('payload, status_code, field, message', [
        (api_steps.order.payload.OrderPayloads.one_ingredient, 200, 'success', True),
        (api_steps.order.payload.OrderPayloads.create_order_without_ingredients, 400, 'success',  False)])
    def test_create_order_user_authorized(self, payload, login_user_get_token, status_code, field, message):
        order = Order()
        headers = {'Authorization': f'Bearer{login_user_get_token}'}
        response = order.create_order(payload, headers)
        assert response.status_code == status_code and response.json().get(field) == message


    @allure.title('Создание заказа с некорректным хэшем')
    def test_create_order_user_authorized(self, login_user_get_token):
        order = Order()
        headers = {'Authorization': f'Bearer{login_user_get_token}'}
        response = order.create_order(api_steps.order.payload.OrderPayloads.create_order_incorrect_ingredients, headers)
        assert response.status_code == 500

    @allure.title('Создание заказа без токена') # будет падать, тк не соответствует ожидаемому результату, наставник подтвердил.
    def test_create_order_user_unauthorized(self):
        order = Order()
        response = order.create_order(api_steps.order.payload.OrderPayloads.one_ingredient)
        assert response.status_code == 401



    @allure.title('Получение заказов')
    @pytest.mark.parametrize('status_code, field, message, token',
                             [(200, 'success', True, True),
                              (401, 'success', False, False)])
    def test_get_user_order(self, login_user_get_token, status_code, field, message, token):
        order = Order()
        headers = {}
        if token:
            headers['Authorization'] = f'Bearer{login_user_get_token}'
        response = order.get_orders(headers)
        assert response.status_code == status_code and response.json().get(field) == message

