import requests
import allure
import data
from api_steps.user.payload import UserPayloads

class User:
    @allure.step('Создать пользователя.')
    def create_user(self):
        user = requests.post(url=data.Endpoints.REGISTER, json=UserPayloads.CREATE_USER)
        return user

    @allure.step('Попробовать создать пользователя, с кредами уже существующего')
    def create_user_already_exist(self):
        user = requests.post(url=data.Endpoints.REGISTER, data=UserPayloads.USER_EXIST)
        return user

    @allure.step('Попробовать создать пользователя, не передав обязательное поле')
    def create_user_without_required_data(self, user_data):
        response = requests.post(url=data.Endpoints.REGISTER, data=user_data)
        return response

    @allure.step('Залогиниться пользователем.')
    def login_user(self):
        response = requests.post(url=data.Endpoints.LOGIN, data=UserPayloads.USER_EXIST)
        return response

    @allure.step('Залогиниться пользователем.')
    def login_user_wrong_data(self, user_data):
        response = requests.post(url=data.Endpoints.LOGIN, data=user_data)
        return response

    @allure.step('Обновить информацию о пользователе.')
    def update_user_info(self, payload, token=None):
        headers = {'Authorization': token}
        response = requests.patch(url=data.Endpoints.UPDATE_USER_INFO, json=payload, headers=headers)
        return response

