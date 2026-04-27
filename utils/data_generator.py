import random
import string


def generate_random_string(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_random_email():
    random_part = generate_random_string(5)
    return f"{random_part}@test.com"


def generate_phone_number():
    return "9" + ''.join(random.choice(string.digits) for _ in range(9))