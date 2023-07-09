from fastapi import APIRouter

from src.container import ContainerDI
from src.database.idatabase import IDatabase
from src.database.models.account import Account


class AccountController():

    def __init__(self, container: ContainerDI) -> None:
        self.router = APIRouter()
        self.db: IDatabase = container.get("db")

        @self.router.get("/find/{id}")
        def get_by_id(id: str) -> Account:
            return self.db.account_set().get_by_id(id)

        @self.router.get("/list")
        def list_all() -> list[Account]:
            return self.db.account_set().list()

        @self.router.post("/create")
        def create_account(account: Account) -> dict:
            self.db.account_set().add(account)
            return {"message": "account created", "id": account.id}
