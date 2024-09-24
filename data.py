class Endpoints:
    base_url ='https://stellarburgers.nomoreparties.site/api/'
    login = f'{base_url}auth/login'
    register = f'{base_url}auth/register'
    update_user_info = f'{base_url}auth/user'
    create_order = f'{base_url}orders'
    user_orders = f'{base_url}orders'
    delete_user = f'{base_url}auth/user'