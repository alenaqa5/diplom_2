import pytest
import requests
import data
from api_steps.user.payload import UserPayloads

@pytest.fixture()
def create_user():
    user = requests.post(url=data.Endpoints.register, json=UserPayloads.create_user)
    token = user.json().get("accessToken")
    yield token
    requests.delete(url=data.Endpoints.delete_user, headers={'Authorization': f'Bearer{token}'})


@pytest.fixture()
def login_user_get_token():
    response = requests.post(url=data.Endpoints.login, data=UserPayloads.user_exist)
    token = response.json().get("accessToken")
    return token
