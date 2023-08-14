from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        print("Mongo constructor")

    def connection_database(self):
        #client = MongoClient(os.environ["MONGO_CONNECTION"])
        URI = "mongodb://0.0.0.0:27728"
        client = MongoClient(URI)
        print("client: ", client)
        return client

    def create_data_collection(self):
        client = self.connection_database()
        #Creating a collection
        db = client['mydb']
        mongo_collection = db['alumnos']
        #Inserting document into a collection
        doc1 = {"name": "Jose L", "age": "31"}
        mongo_collection.insert_one(doc1)
        
        self.close_database(client)
        
        print("Collection alumnos created")
    
    def find_one_data_value(self):
        client = self.connection_database()
        db = client['mydb']
        mongo_collection =  db['alumnos']
        
        one_value = mongo_collection.find_one()
        
        self.close_database(client)
        
        print("Value",one_value)
        
    
    def close_database(self, mongo_client):
        mongo_client.close()

if __name__ == "__main__":
    obj_mongo = MongoDB()
    
    #create a collection 
    obj_mongo.create_data_collection()
    obj_mongo.find_one_data_value()
    