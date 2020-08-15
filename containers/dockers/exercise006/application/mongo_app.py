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
    def get_mongo_client(mongo_collection_string="mongodb://mongodb:27017/"):
        '''
            Create an instance of MongoClient and return
            :param mongo_host: Hostname where mongo service runs
            :param mongo_port : Port for mongo service
        '''
        print("Create an instance of MongoClient and return")
        return pymongo.MongoClient(mongo_collection_string)

    @staticmethod
    def get_mongo_database(mongo_client,mongo_database_name):
        '''
            Create a new database and return
            :param mongo_client: Mongo Client object created using method -- get_mongo_client
            :param mongo_database_name: Name of the database
        '''
        print("Create a new database and return")
        return mongo_client[mongo_database_name]

    @staticmethod
    def get_mongo_database_collection(mongo_database_name,mongo_collection_name):
        '''
            Create a new database collection and return
            :param mongo_database_name: Name of the database
            :param mongo_collection_name: Collection inside database in which documents will be stored            
        '''
        print("Create a new database collection and return")
        return mongo_database_name[mongo_collection_name]

    @staticmethod
    def set_collection_records(collection_object,records):
        '''
            Insert records into a collection
            :param collection_object: Database Collection Object
            :param records: Document(s) to be inserted
        '''
        print("Insert records into a collection")
        collection_object.insert_one(records)
        return True

    @staticmethod
    def get_collection_records(collection_object):
        '''
            Get records from a collection
            :param collection_object: Database Collection Object
        '''
        print("Get records from a collection")
        return collection_object.find_one()

def driver():

    print("Connect to Mongo and do all operations...")

    mongo_client = MongoDBRunner.get_mongo_client()
    mongo_database = MongoDBRunner.get_mongo_database(mongo_client=mongo_client,mongo_database_name='tests-mongo')
    mongo_database_collection = MongoDBRunner.get_mongo_database_collection(mongo_database_name=mongo_database,
                                mongo_collection_name='tests-mongo-colls')
    
    # Sample test document to be inserted
    members = {
                "data":{

                        "user_id":"007",
                        "user_name":"arunkuch",
                        "profession":"Programmer",
                        "location":"Chennai",
                        "passion":"Coding"
                }
              }
    MongoDBRunner.set_collection_records(collection_object=mongo_database_collection,records=members)
    result = MongoDBRunner.get_collection_records(collection_object=mongo_database_collection)

    print("All Tasks Completed...")
    return {'fin-data':str(result)}


if __name__ == "__main__":
    driver()    