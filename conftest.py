import pytest
import requests
import data
from api_steps.user.payload import UserPayloads

@pytest.fixture()
def create_user():
    user = requests.post(url=data.Endpoints.REGISTER, json=UserPayloads.CREATE_USER)
    token = user.json().get("accessToken")
    yield token
    requests.delete(url=data.Endpoints.DELETE_USER, headers={'Authorization': f'Bearer{token}'})


@pytest.fixture()
def login_user_get_token():
    response = requests.post(url=data.Endpoints.LOGIN, data=UserPayloads.USER_EXIST)
    token = response.json().get("accessToken")
    return token
