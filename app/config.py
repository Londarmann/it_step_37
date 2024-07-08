import os

from dotenv import load_dotenv

load_dotenv()

TORTOISE_URL = os.getenv("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {
        "default": TORTOISE_URL
    },
    "apps": {
        "models": {

            "models": ["app.models"],
            "default_connection": "default"
        },
        }
    }
