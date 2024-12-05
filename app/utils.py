import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(user_input):
    if not user_input or not isinstance(user_input, str):
        return False, "Invalid input. Please enter a valid string."
    return True, None