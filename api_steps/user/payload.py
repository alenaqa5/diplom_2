from faker import Faker

fake = Faker()
class UserPayloads:
    create_user = {
    "email": fake.free_email(),
    "password": fake.text(max_nb_chars=10),
    "name": fake.text(max_nb_chars=10)
    }

    create_user_without_email = {
        "password": "12345678",
        "name": "Alenka"
    }

    create_user_without_password = {
        "email": fake.free_email(),
        "name": "Alenka"
    }

    create_user_without_name = {
        "email": fake.free_email(),
        "name": "Alenka"
    }

    user_exist = {
        "email": "alyonapodgornaia@yandex.ru",
        "password": "12345678",
        "name": "Alenka"
    }

    user_wrong_password = {
        "email": "alyonapodgornaia@yandex.ru",
        "password": "11111111",
        "name": "Alenka"
    }

    user_wrong_email = {
        "email": "alyona111podgornaia@yandex.ru",
        "password": "12345678",
        "name": "Alenaka"
    }

    user_data_for_changing_name = {
        "email": fake.free_email(),
        "password": "12345678",
        "name": fake.user_name()
    }

    user_data_for_changing_password = {
        "email": fake.free_email(),
        "password": fake.password(length=8)
    }

    user_data_for_changing_email = {
        "email": fake.free_email(),
        "password": "12345678",
        "name": "Alenka"
    }
