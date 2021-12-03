from pymongo import MongoClient

class Conexao:
    client, database, collection = "","",""

    def __init__(self, database = "teste", collection = "clientes"):
        self.client = MongoClient("mongodb://127.0.0.1:27017/")
        self.database = self.client[database]
        self.collection = self.database[collection]    

    def set_client(self, client):
        self.client = client
    
    def set_database(self, database):
        self.database = self.cliente[database]

    def set_collection(self, collection):
        self.collection = self.database[collection]