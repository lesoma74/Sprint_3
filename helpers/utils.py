# helpers/utils.py

import random
import string

def generate_random_email(length=10, domain="example.com"):
    letters = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    email = f"{username}@{domain}"
    return email

def generate_random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
