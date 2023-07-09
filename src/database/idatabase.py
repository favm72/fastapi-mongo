from abc import abstractmethod

from src.database.models.account import IAccountSet


class IDatabase():
    @abstractmethod
    def account_set(self) -> IAccountSet:
        pass
