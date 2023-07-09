from src.configuration import Configuration
from src.container import ContainerDI
from src.database.mongo_database import MongoData


def get_container() -> None:
    container = ContainerDI()
    config = Configuration()
    container.register("config", config)
    container.register("db", MongoData(config))
    return container
