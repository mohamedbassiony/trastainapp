from helpers import get_settings, Settings
import os
import random
import string
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseController:
    
    def __init__(self):

        self.app_settings = get_settings()
        
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )

        self.destination_dir = os.path.join(
            self.base_dir,
            "assets/DestinationData"
        )

        logger.info("BaseController initialized")
        
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    

    
