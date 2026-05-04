import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class DataManager:
    """Manages test data to avoid conflicts in parallel execution"""
    
    def __init__(self):
        pass
    
    def get_unique_username(self):
        """Generate unique username using timestamp"""
        import datetime
        return f"testuser_{datetime.datetime.now().strftime('%H%M%S%f')}"
    
    def get_unique_email(self, base="test"):
        """Generate unique email using timestamp"""
        import datetime
        return f"{base}_{datetime.datetime.now().strftime('%H%M%S%f')}@example.com"

# Singleton instance
data_manager = DataManager()