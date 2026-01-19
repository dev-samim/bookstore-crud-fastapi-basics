from dotenv import load_dotenv
from os import getenv

load_dotenv()

DB_URL = getenv("DB_URL")
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")