from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        print("Mongo constructor")

    def connection_database(self):
        #client = MongoClient(os.environ["MONGO_CONNECTION"])
        URI = os.environ["MONGO_CONNECTION"]
        client = MongoClient(URI)
        return client

    def create_switch_data_collection(self):
        client = self.connection_database()
        #Creating a collection
        db = client['mydb']
        mongo_collection = db['alumnos']
        
        return mongo_collection,client
    
    
    def insert_one_value(self,name,age):
        mongo_collection,client = self.create_switch_data_collection()
        doc1 = {"name": name, "age": age}
        #Inserting document into a collection
        mongo_collection.insert_one(doc1)
        self.close_database(client)
    
    def find_one_data_value(self,column,value):
        mongo_collection,client = self.create_switch_data_collection()
        one_value = mongo_collection.find_one({column:value})
        self.close_database(client)
        
        return one_value

        
    def find_all_values(self):
        list_values = []
        mongo_collection,client = self.create_switch_data_collection()
        values =  mongo_collection.find()
        for value in values:
            list_values.append(value)
        
        self.close_database(client)
        
        return list_values
    
    def delete_one_value(self):
        mongo_collection,client = self.create_switch_data_collection()
        result_delete = mongo_collection.delete_one({"name":"Mr.Coder"})
        print(result_delete)
        self.close_database(client)
        
        return result_delete
        
    
    def close_database(self, mongo_client):
        mongo_client.close()

if __name__ == "__main__":
    obj_mongo = MongoDB()
    
    #create a collection 
    obj_mongo.create_switch_data_collection()
    #obj_mongo.find_one_data_value("name","Mariana L")
    #obj_mongo.insert_one_value("Elizabeth Garcia",25)
    #obj_mongo.find_all_values()