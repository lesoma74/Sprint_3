
import random
import string
from helpers.data import BASE_NAME, BASE_EMAIL_DOMAIN, BASE_PASSWORD

def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email(length=10, domain=BASE_EMAIL_DOMAIN):
    letters = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    email = f"{username}@{domain}"
    return email

def generate_random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_test_data():
    random_string = generate_random_string()
    name = f"{BASE_NAME}{random_string}"
    email = generate_random_email()
    password = generate_random_password()
    return name, email, password

