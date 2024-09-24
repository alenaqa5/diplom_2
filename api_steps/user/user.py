from http.client import responses

import requests
import allure
import data
from api_steps.user.payload import UserPayloads

class User:
    @allure.step('Создать пользователя.')
    def create_user(self):
        user = requests.post(url=data.Endpoints.register, json=UserPayloads.create_user)
        return user

    @allure.step('Попробовать создать пользователя, с кредами уже существующего')
    def create_user_already_exist(self):
        user = requests.post(url=data.Endpoints.register, data=UserPayloads.user_exist)
        return user

    @allure.step('Попробовать создать пользователя, не передав обязательное поле')
    def create_user_without_required_data(self, user_data):
        response = requests.post(url=data.Endpoints.register, data=user_data)
        return response

    @allure.step('Залогиниться пользователем.')
    def login_user(self):
        response = requests.post(url=data.Endpoints.login, data=UserPayloads.user_exist)
        return response

    @allure.step('Залогиниться пользователем.')
    def login_user_wrong_data(self, user_data):
        response = requests.post(url=data.Endpoints.login, data=user_data)
        return response

    @allure.step('Обновить информацию о пользователе.')
    def update_user_info(self, payload, token=None):
        headers = {'Authorization': token}
        response = requests.patch(url=data.Endpoints.update_user_info, json=payload, headers=headers)
        return response

