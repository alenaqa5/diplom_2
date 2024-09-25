import requests
import allure
import data


class Order:
    @allure.step('Создать заказ')
    def create_order(self, payload, headers=None):
         response = requests.post(url=data.Endpoints.create_order, data=payload, headers=headers)
         return response

    @allure.step('Запросить заказы')
    def get_orders(self, headers=None):
        response = requests.get(url=data.Endpoints.user_orders, headers=headers)
        return response

