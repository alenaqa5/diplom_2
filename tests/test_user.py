import allure
import pytest
from api_steps.user.user import User
from api_steps.user.payload import UserPayloads


class TestUser:
    @allure.title('Обновить информацию о пользователе с передачей токена.')
    @pytest.mark.parametrize('payload, expected_status_code, success', [
        (UserPayloads.user_data_for_changing_name, 200, True),
        (UserPayloads.user_data_for_changing_password, 200, True),
        (UserPayloads.user_exist, 403, False)
    ])
    def test_update_user_info_user_authorized(self, payload, expected_status_code, success, create_user):
        user = User()
        token = create_user
        response = user.update_user_info(payload, token)
        assert response.status_code == expected_status_code and response.json().get('success') == success, response.json()

    @allure.title('Создать пользователя')
    def test_create_user(self):
        user = User()
        response = user.create_user()
        assert response.status_code == 200 and response.json().get("success") is True, response.json()
    @allure.title('Создать пользователя, с кредами уже существующего')
    def test_create_user_with_credentials_already_exist(self):
        user = User()
        response = user.create_user_already_exist()
        assert response.status_code == 403 and response.json().get("message") == "User already exists"

    @allure.title('Создать пользователя не заполнив обязательное поле')
    @pytest.mark.parametrize('user_data', [UserPayloads.create_user_without_email,
                                           UserPayloads.create_user_without_password,
                                           UserPayloads.create_user_without_name])
    def test_create_user_without_required_field(self, user_data):
        user = User()
        response = user.create_user_without_required_data(user_data)
        assert response.status_code == 403 and response.json().get("success") is False

    @allure.title('Залогиниться пользователем')
    def test_login_user(self):
        user = User()
        response = user.login_user()
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Залогиниться с некорректными данными')
    @pytest.mark.parametrize('user_data', [UserPayloads.user_wrong_email, UserPayloads.user_wrong_password])
    def test_login_user_wrong_data(self, user_data):
        user = User()
        response = user.login_user_wrong_data(user_data)
        assert response.status_code == 401 and response.json().get("success") is False

    @allure.title('Обновить информацию не передавая токен')
    @pytest.mark.parametrize('payload, expected_status_code, success', [
        (UserPayloads.user_data_for_changing_name, 401, False),
        (UserPayloads.user_data_for_changing_password, 401, False),
        (UserPayloads.user_exist, 401, False)])
    def test_update_user_info_user_not_authorized(self, payload, expected_status_code, success, create_user):
        user = User()
        response = user.update_user_info(payload)
        assert response.status_code == expected_status_code and response.json().get(
            'success') == success, response.json()




