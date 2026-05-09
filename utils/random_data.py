
import random
import string
from datetime import datetime


def random_string(length: int = 8) -> str:
    """Generate random alphanumeric string"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def random_email(prefix: str = "test") -> str:
    """Generate unique email address"""
    timestamp = datetime.now().strftime("%H%M%S%f")
    return f"{prefix}_{timestamp}@example.com"


def random_phone() -> str:
    """Generate random 10-digit phone number"""
    return ''.join(random.choices(string.digits, k=10))


def random_name() -> str:
    """Generate random first name"""
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    return random.choice(names) + "_" + random_string(4)