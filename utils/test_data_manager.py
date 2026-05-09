import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class DataManager:

    
    def __init__(self):
        pass
    
    def get_unique_username(self):

        import datetime
        return f"testuser_{datetime.datetime.now().strftime('%H%M%S%f')}"
    
    def get_unique_email(self, base="test"):

        import datetime
        return f"{base}_{datetime.datetime.now().strftime('%H%M%S%f')}@example.com"

data_manager = DataManager()