# Ryan Reames
# CS-340-T4223
# Project One

from pymongo import MongoClient
from bson.objectid import ObjectId
# Used to format cursor and return JSON instead
from bson.json_util import loads
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        # no authorization
        #self.client = MongoClient('mongodb://localhost:51842')
        # authorization
        self.client = MongoClient('mongodb://%s:%s@localhost:51842/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']

# Create method
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Read method
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data) # returns one document as dictionary
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            return False
    
    def read_all(self, data):
        if data is not None:
            cursor = self.database.animals.find(data, {'_id':False})
            return cursor # returns pointer to list of animals meeting data criteria
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            return False            

# Update method   
    def update(self, criteria, data):
        if data is not None and criteria is not None:
            self.database.animals.update_one(criteria, {"$set": data})
            return self.database.animals.find_one(criteria)
        else:
            raise Exception("Nothing to update, because update criteria or data is empty")
    
    def update_all(self, criteria, data):
        if data is not None and criteria is not None:
            self.database.animals.update_many(criteria, {"$set": data})
            return loads(dumps(self.database.animals.find(criteria))) # returns JSON results, not cursor
        else:
            raise Exception("Nothing to update, because update criteria or data is empty")
            
# Delete method
    def delete(self, data):
        if data is not None:
            deletedData = self.database.animals.find_one(data)
            self.database.animals.delete_one(data)
            return deletedData
        else:
            raise Exception("Nothing to update, because no data passed to delete")
    
    def delete_all(self, data):
        if data is not None:
            deletedData = self.database.animals.find(data)
            self.database.animals.delete_many(data)
            return loads(dumps(deletedData)) # returns JSON results, not cursor
        else:
            raise Exception("Nothing to update, because no data passed to delete")