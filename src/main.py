from fastapi import FastAPI

from src.cors import add_cors
from src.injections import get_container
from src.routes import add_routes


def create_app() -> FastAPI:
    app = FastAPI()
    add_cors(app)
    container = get_container()
    add_routes(app, container)
    return app
