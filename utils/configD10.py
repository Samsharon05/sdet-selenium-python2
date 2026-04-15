import os

class Configdata:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://www.saucedemo.com/")