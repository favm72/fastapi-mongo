from datetime import datetime
from uuid import uuid4

from src.database.idatabase import IDatabase
from src.database.models.account import Account, IAccountSet


class MemoryAccountSet(IAccountSet):
    def __init__(self):
        self._accounts = {}

    def get_by_id(self, id: str) -> Account:
        return self._accounts.get(id)

    def add(self, account: Account) -> None:
        account.id = str(uuid4())
        account.created_at = account.updated_at = datetime.now().isoformat()
        self._accounts[account.id] = account

    def list(self) -> list[Account]:
        return list(self._accounts.values())


class MemoryData(IDatabase):
    def __init__(self):
        self.accounts = MemoryAccountSet()

    def account_set(self) -> IAccountSet:
        return self.accounts
