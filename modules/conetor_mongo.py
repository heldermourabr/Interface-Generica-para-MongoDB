from pymongo import MongoClient

class Conexao:
    client, database, collection = "","",""

    def __init__(self, database = "teste", collection = "testando"):
        self.client = MongoClient("mongodb>//127.0.0.1:27017")
        self.database = self.cliente[database]
        self.collection = self.database[collection]