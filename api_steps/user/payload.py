from faker import Faker


class UserPayloads:
    create_user = {
    "email": Faker.free_email(),
    "password": Faker.text(max_nb_chars=10),
    "name": Faker.text(max_nb_chars=10)
    }

    create_user_without_required_field = {
        "password": '12345678',
        "name": 'Alenka'
    }

    user_exist = {
        "email": 'alyonapodgornaia@yandex.ru',
        "password": '12345678',
        "name": 'Alenka'
    }

    user_wrong_password = {
        "email": 'alyonapodgornaia@yandex.ru',
        "password": '11111111',
        "name": 'Alenka'
    }

    user_wrong_email = {
        "email": 'alyonapodgornaia@yandex.ru',
        "password": '12345678',
        "name": 'Alenaka'
    }

    user_data_for_changing_name = {
        "email": 'alyonapodgornaia11@yandex.ru',
        "password": Faker.password(length=8),
        "name": Faker.user_name()
    }

