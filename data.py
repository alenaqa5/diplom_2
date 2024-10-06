class Endpoints:
    BASE_URL ='https://stellarburgers.nomoreparties.site/api/'
    LOGIN = f'{BASE_URL}auth/login'
    REGISTER = f'{BASE_URL}auth/register'
    UPDATE_USER_INFO = f'{BASE_URL}auth/user'
    CREATE_ORDER = f'{BASE_URL}orders'
    USER_ORDERS = f'{BASE_URL}orders'
    DELETE_USER = f'{BASE_URL}auth/user'


class ResponsesErrors:
    USER_ALREADY_EXIST = "User already exists"