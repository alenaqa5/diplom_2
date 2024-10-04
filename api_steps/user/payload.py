from faker import Faker

fake = Faker()
class UserPayloads:
    CREATE_USER = {
    "email": fake.free_email(),
    "password": fake.text(max_nb_chars=10),
    "name": fake.text(max_nb_chars=10)
    }

    CREATE_USER_WITHOUT_EMAIL = {
        "password": "12345678",
        "name": "Alenka"
    }

    CREATE_USER_WITHOUT_PASSWORD = {
        "email": fake.free_email(),
        "name": "Alenka"
    }

    CREATE_USER_WITHOUT_NAME = {
        "email": fake.free_email(),
        "name": "Alenka"
    }

    USER_EXIST = {
        "email": "alyonapodgornaia@yandex.ru",
        "password": "12345678",
        "name": "Alenka"
    }

    USER_WRONG_PASSWORD = {
        "email": "alyonapodgornaia@yandex.ru",
        "password": "11111111",
        "name": "Alenka"
    }

    USER_WRONG_EMAIL = {
        "email": "alyona111podgornaia@yandex.ru",
        "password": "12345678",
        "name": "Alenaka"
    }

    USER_DATA_FOR_CHANGING_NAME = {
        "email": fake.free_email(),
        "password": "12345678",
        "name": fake.user_name()
    }

    USER_DATA_FOR_CHANGING_PASSWORD = {
        "email": fake.free_email(),
        "password": fake.password(length=8)
    }

    USER_DATA_FOR_CHANGING_EMAIL = {
        "email": fake.free_email(),
        "password": "12345678",
        "name": "Alenka"
    }
