'''
 Utils file for all reusable operations 
 Mongo -- https://pymongo.readthedocs.io/en/stable/tutorial.html
'''
# Import sys modules
import json

# Import 3rd party modules
import pymongo


# Define class for all mongo operations
class MongoDBRunner:
    '''
        Define methods for all mongo db ops
    '''

    @staticmethod
    def get_mongo_client(mongo_collection_string="mongodb://localhost:27017/"):
        '''
            Create an instance of MongoClient and return
            :param mongo_host: Hostname where mongo service runs
            :param mongo_port : Port for mongo service
        '''
        return pymongo.MongoClient(mongo_collection_string)

    @staticmethod
    def get_mongo_database(mongo_client,mongo_database_name):
        '''
            Create a new database and return
            :param mongo_client: Mongo Client object created using method -- get_mongo_client
            :param mongo_database_name: Name of the database
        '''
        return mongo_client[mongo_database_name]

    @staticmethod
    def get_mongo_database_collection(mongo_database_name,mongo_collection_name):
        '''
            Create a new database and return
            :param mongo_database_name: Name of the database
            :param mongo_collection_name: Collection inside database in which documents will be stored            
        '''
        return mongo_database_name[mongo_collection_name]

    @staticmethod
    def set_collection_records(collection_object,records):
        '''
            Insert records into a collection
            :param collection_object: Database Collection Object
            :param records: Document(s) to be inserted
        '''
        collection_object.insert_one(records)
        return True


    @staticmethod
    def set_collection_records(collection_object,records):
        '''
            Insert records into a collection
            :param collection_object: Database Collection Object
            :param records: Document(s) to be inserted
        '''
        collection_object.insert_one(records)
        return True

    @staticmethod
    def get_collection_records(collection_object):
        '''
            Get records from a collection
            :param collection_object: Database Collection Object
        '''
        return collection_object.find_one()

# Define Class to do all parsing operations..

class Parser:
     
    '''
      Do all File Parsing Operations 
    '''
    
    @staticmethod
    def read_json(file_name):
        '''
            Read the json file and return the contents
            :param file_name: Full Path of the json file
            :return : JSON File contents
            :exception : Raise Error
        '''
        try:
            with open(file_name,'r') as reader:
                 return json.load(reader)
        except Exception as json_file_error:
            raise json_file_error

if __name__ == "__main__":

    mongo_client = MongoDBRunner.get_mongo_client()
    mongo_database = MongoDBRunner.get_mongo_database(mongo_client=mongo_client,mongo_database_name='tests-mongo')
    mongo_database_collection = MongoDBRunner.get_mongo_database_collection(mongo_database_name=mongo_database,
                                mongo_collection_name='tests-mongo-colls')
    
    # Sample test document to be inserted
    members = {
                "data":{

                        "user_id":"001",
                        "user_name":"Arun",
                        "profession":"Programmer",
                        "location":"Chennai"
                }
              }
    MongoDBRunner.set_collection_records(collection_object=mongo_database_collection,records=members)
    print(MongoDBRunner.get_collection_records(collection_object=mongo_database_collection))