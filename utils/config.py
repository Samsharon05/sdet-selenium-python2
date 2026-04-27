from dotenv import load_dotenv
import os

load_dotenv()

class Configdata:
    def __init__(self):
        self.login_username=os.getenv("USERNAME")
        self.login_password=os.getenv("PASSWORD")
        self.link=os.getenv("URL_LINK")
        
        
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://www.saucedemo.com/")
        
    
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_FILE = os.path.join(BASE_DIR, "data", "test_data.json")
