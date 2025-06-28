# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables using os.getenv
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))  # fallback if not found
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
