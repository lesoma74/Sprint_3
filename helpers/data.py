
import random
import string

class TestData:
    REGISTERED_EMAIL = "Antonov18@ya.ru"
    REGISTERED_PASSWORD = "123456"
    BASE_NAME = "TestUser"
    BASE_EMAIL_DOMAIN = "example.com"
    BASE_PASSWORD = "password123"
    EXISTING_USER_EMAIL = "existing_user@example.com"

    @staticmethod
    def generate_random_string(length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def generate_random_email():
        return TestData.generate_random_string() + "@" + TestData.BASE_EMAIL_DOMAIN

    @staticmethod
    def generate_random_password(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_test_data():
        name = TestData.generate_random_string()
        email = TestData.generate_random_email()
        password = TestData.generate_random_password()
        return name, email, password
