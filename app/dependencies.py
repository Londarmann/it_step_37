from fastapi import Depends

from tortoise.contrib.fastapi import register_tortoise

from app.config import TORTOISE_ORM


def get_database(app):
    return register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True
    )
