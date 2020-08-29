'''
    Define all the Abstract classes as part of this module.
    An Abstract class contains the skeleton alone and not the real implementation.
    An Abstract class contains the sigantures inside the abstract methods.
    It gives clarity to develop and write source-code.
    An Abstract class can contain many abstract methods.
    When a sub-class inherits the Abstract class all the methods that are maked as abstractmethod
    must be implemented in the sub-class.
    If a Sub-Class fails to implement any of the abstract method, then it's not possible
    to create an instance of the sub-class.
'''

# import the abc module
import abc

# Define the abstract class for Person Class
class AbstractPerson(metaclass=abc.ABCMeta):
    '''
        Define all the Abstract methods
    '''

    @abc.abstractmethod
    def check_qualification(self):
        '''
            Method uses 2 arguments , self.age and self.qualify_age
            This method checks for condition on age, return as True/False
        '''

    @abc.abstractmethod
    def about(self):
        '''
            Method used multiple instance variables
            #self.age, self.qualify_age,self.name,self.location,self.profession
            This method displays details of the Person      
        '''

    @abc.abstractmethod
    def process(self):
        '''
            This method displays details of the Person and
            processes the records.
        '''
