from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    GPT4_API_KEY = os.getenv("GPT4_API_KEY")
    DB_URI = os.getenv("DB_URI")
    UAGENT_PRIVATE_KEY = os.getenv("UAGENT_PRIVATE_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")

config = Config()
