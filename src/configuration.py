from os import environ


class Configuration():
    def __init__(self) -> None:
        self.mongoUrl = environ.get("MONGO_URL")
        self.mongoDb = environ.get("MONGO_DB")
