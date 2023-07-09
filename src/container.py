from typing import TypeVar

T = TypeVar('T')


class ContainerDI():
    def __init__(self):
        self._container = {}

    def register(self, name: str, obj: T):
        self._container[name] = obj

    def get(self, name) -> T:
        return self._container.get(name)
