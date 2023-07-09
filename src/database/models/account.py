
from abc import abstractmethod
from dataclasses import dataclass


@dataclass()
class Account():
    id: str = None
    name: str = None
    email: str = None
    phone: str = None
    address: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    country: str = None
    created_at: str = None
    updated_at: str = None


class IAccountSet():
    @abstractmethod
    def get_by_id(self, id: str) -> Account:
        pass

    @abstractmethod
    def list(self) -> list[Account]:
        pass

    @abstractmethod
    def add(self, account: Account) -> None:
        pass
