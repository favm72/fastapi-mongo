from dataclasses import asdict
from datetime import datetime
from uuid import uuid4

from pymongo import MongoClient
from pymongo.database import Database

from src.configuration import Configuration
from src.database.idatabase import IDatabase
from src.database.models.account import Account, IAccountSet


class MongoAccountSet(IAccountSet):
    def __init__(self, db: Database):
        self._db = db
        self._collection = self._db["account"]

    def get_by_id(self, id: str) -> Account:
        return self._collection.find_one({"id": id})

    def add(self, account: Account) -> None:
        account.id = str(uuid4())
        account.created_at = account.updated_at = datetime.now().isoformat()
        self._collection.insert_one(asdict(account))

    def list(self) -> list[Account]:
        def mapitem(item: dict):
            return Account(
                id=item.get("id"),
                name=item.get("name"),
                created_at=item.get("created_at"),
                updated_at=item.get("updated_at"),
                address=item.get("address", None),
                city=item.get("city", None),
                country=item.get("country", None),
                email=item.get("email", None),
                phone=item.get("phone", None),
                state=item.get("state", None),
                zip_code=item.get("zip_code", None),
            )
        return list(map(mapitem, list(self._collection.find())))


class MongoData(IDatabase):
    def __init__(self, config: Configuration):
        self.client = MongoClient(config.mongoUrl)
        self.db = self.client[config.mongoDb]
        self.accounts = MongoAccountSet(self.db)

    def account_set(self) -> IAccountSet:
        return self.accounts
