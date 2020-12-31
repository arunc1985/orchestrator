'''
 Utils file for all reusable operations 
'''
# Import sys modules
import json


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
