'''
    In Python a Class is defined using class keyword.
    A class is used for logical grouping of various methods.
    A Class is needed for various operations and a class can have any number of methods.


    A Class can have any number of methods and there are 3 kinds of methods.
        1. Instance Method
        2. Class Method
        3. Static Method

    A Class can be designed with combination of methods or any of the method types.

        i.e. A Class can have all the 3 types of methods, 
            it can have any of these method types or
            it can have any 2 of these method types also....

    Also There can be ;
        - any number of instance methods
        - any number of class methods
        - any number of static methods
        
        * No limitations

    ** Refer to README file for detailed documentation on the Classes.

    Method :: __call__

    	In this example , we will see a special magic method __call__ for invoking an instance of the class.                    
    	After creating an instance of the class, when the instance is called the __call__ method is invoked.

    	Example : Lets say we have a simple class.

    		class Person:
    			pass

    		Create an instance of the Class:
				
				# Instance creation..
    			instance_class = Person() # Instance gets created.

    			# Call the instance.
    			instance_class() # The __call__ special method will get invoked.
    
    Note :: This example is same as exercise2.py the only difference is the method check_qualification is rewritten;

        Method check_qualification in exercise2.py

        def check_qualification(self):
            """
                # As you see here - the self at run time becomes instance of the class
                # With self we can thus access the instance variables of the class such as ;
                #self.age and qualify_age
                This method checks for condition on age, return as True/False
            """
            # Check condition and return as True/False
            if self.age>self.qualify_age:
                return True
            return False
        
        Method check_qualification in exercise3.py -> Written using lambdas.

        Rewritten as follows using lambdas;
            
            # Write a lambda function to check for qualification
            # The below lambda function has to be invoked as self.check_qualification(self)
            self.check_qualification = lambda self : True if self.age>self.qualify_age else False
'''

# Define a Person class and perform related operations
class Person:

    def __init__(self,name,age,location,profession):
        """
            This Constructor takes 4 arguments;
            :param name: Name of the Person
            :param age: Age of the Person
            :param location: Location of the Person
            :param profession: Profession of the Person

            Note :: 
                1 . The parameters defined inside the __init__ method are accessible only to the
                instance of the class
                2. Pass values for all parameters while creating an instance of the class
                3. The variables thus assigned below are known as *instance variables*
                4. Example of instance variables are shown below;
                    self.name=name
                    self.age=age
                    self.location=location
                    self.profession=profession
                5. The instance variables are accessible only inside the instance methods of the class
        """
        # Assign the parameters to the instance variables
        self.name=name
        self.age=age
        self.location=location
        self.profession=profession
        self.qualify_age=20 # We can also hard-code instance variables

        # Write a lambda function to check for qualification
        # The below lambda function has to be invoked as self.check_qualification(self)
        self.check_qualification = lambda self : True if self.age>self.qualify_age else False

    """
        The below method is an example of an instance method
        It accesss instance variable self.age ,self.qualify_age and returns True or False
        Note: 
            1. The instance method of the class has a default parameter called "self" and its mandatory
            2. At run time when the classes and it's methods are created the default parameter "self"
                becomes the * instance * of the class.
            3. We must create an instance of class to access the instance method.
                Example:
                    instance_person.check_qualification()
    """

    def about(self):
        """
            # As you see here - the self at run time becomes instance of the class
            # With self we can thus access the instance variables of the class such as ;
            #self.age, self.qualify_age,self.name,self.location,self.profession
            This method displays details of the Person
        """
        # Display details
        return "My name is {} and I am {} , I am From {} and I am a {} and I am qualified!!".format(self.name,
            self.age,self.location,self.profession)


    def process(self):
        '''
            Processes the records of the person...
        '''
        # Check a condition and process. Print details of the person if they would be qualified.
        return self.about() if bool(self.check_qualification(self)) else "{} is Unqualified! for the Club".format(self.name)

    def __call__(self,*arguments):
    	'''
    		This method is invoked when an instance of the class is called.
    		Example:
    			instance_person = Person("Sherlock",20,"London","Programmer") # Returns an instance of the person class.
    			Calling the instance as instance_person() -> Will invoke this __call__ method.
    	'''
    	# Execute the process
    	return self.process()

# Execute
if __name__ == "__main__":
    instance_person = Person("Sherlock",25,"London","Programmer") # Returns an instance of the person class.
    # Print the instance
    print(instance_person)
    # Display details
    print(instance_person())
