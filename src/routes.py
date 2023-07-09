from fastapi import FastAPI

from src.container import ContainerDI
from src.controllers.account import AccountController


def add_routes(app: FastAPI, container: ContainerDI) -> None:
    app.include_router(AccountController(container).router, prefix="/account")

    @app.get("/")
    def root():
        return {"message": "api is running", "version": "1.0.0"}
