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
    -------------------

        In this example , we will a special magic method __call__ for invoking an instance of the class.                    
        After creating an instance of the class, when the instance is called the __call__ method is invoked.

            def __call__(self,*arguments):
                """
                    This method is invoked when an instance of the class is called.

                    Example:
                        instance_person = Person("Sherlock",20,"London","Programmer")
                         # Returns an instance of the person class.
                        Calling the instance as instance_person() -> Will invoke this __call__ method.
                """

        Example : Lets say we have a simple class.

            class Person:
                pass

            Create an instance of the Class:
                
                # Instance creation..
                instance_class = Person() # Instance gets created.

                # Call the instance.
                instance_class() # The __call__ special method will get invoked.

    Method :: __getattr__
    ---------------------

    	In this example , we will see a special magic method __getattr__ 
        This method gets invoked under special conditions when an instance of the class tries to access an atrribute,
        and that the attribute would not be available in this class.

        Example: Let's see a simple class.


            class Person :

                def method_a(self):
                    return "Hello"
            
            # Create an instance of the Person Class
            instance_person = Person()                
            instance_person.method_a # Returns "Hello"
            # The below method method_z is not part of the Person class and __getattr__ will get invoked.
            instance_person.method_z # __getattr__ gets invoked

        Why to use __getattr__ ??

            - If an instance of the class tries to access an attribute that wouldn't be available,
             the method __getattr__ will get invoked and we can handle it and return some values.

             if this method is not defined then it will result in exception : AttributeError

        Inside the __getattr__ method we can also set the values for the class.

            Example :: setattr(self.__class__,attribute,"NULL")

    Analyze the Class and Instance Dictionary :
    
        1. Class Dictionary will contain all the attributes at the class level. 
            * It will not contain the attributes inside of the __init__ method.
     
        2. Class Instance Dictionary will contain all the attributes that are present inside of the 
            __init__ method.

            * It will not contain the attributes at class level such as ;
                1. Class Variables.
                2. Methods of the Class (InstanceMethod, ClassMethod, StaticMethod)
        
    Callable & Non-Callable Attributes :
    -----------------------------------

        Callable Attributes -> 
            - Attributes of the class that are actually executed using () braces.
            - Example : Methods of the Class

        Non-Callable Attributes -> 

            - Attributes of the class that are actually not executed using () braces.
            - If you would execute them it would result in TypeError
            - Example : Instance Variables, Class Variables, Properties.
        
        Refer to the implementation as below.

'''

# Define a Person class and perform related operations
class Person:

    # Define a Simple Class Variable
    TEAM_NAME = "HCL-SON"

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

    def __getattr__(self,attribute):
        '''
            This method will get called for any attribute that is not available in the class/instance.
            
            If an User calls an attribute as instance_class.xyz, if xyz is not available either at
            instance level or class level - then this method will get called.

            Instance level - Refer __init__() method where we create instance variables.
            Class level - Anything and everything at class level. Methods, Class Variables etc..

            In case you dont define __getatrr__ but if you would call an unavailable attribute,
            It will result in AttributeError as shown below as an example :

                Traceback (most recent call last):
                  File "classes/exercise4.py", line 180, in <module>
                    print(instance_person.process_a) # Attribute process_a doesn't exist in the class..
                AttributeError: 'Person' object has no attribute 'process_a'

            Handle the attribute in case of AttributeError
            :param attribute: The attribute being accessed.
        
        Since the Attribute is not part of the class, set the value for the attribute like below;
        setattr(self.__class__,attribute,value)
        setattr - A build-in keyword for setting values to attributes.

        Example:
            instance_person = Person("Sherlock",25,"London","Programmer") 
            In above case self means instance_person
            and self.__class__ means Person class


        self.__class__ - The Class object itself.
        self - Instance of the Class.
        attribute - The attribute that doesnt exist in the class.
        value - The value to be set to the attribute.

        So - This command : 

            Syntax : setattr(self.__class__,attribute,value)
        
            Example :: 
                setattr(self.__class__,count_people,10000)
                Set the value as 10000 for the attribute count_people

            Once it's set here - its avaiable at class and instance level.
            Anything that a class can access can also be accessed by the instance of the class.
            An instance is like a baby to the parent.


        getattr(self.__class__,attribute)

        getattr - Builtin function used for getting the values.
        self.__class__ - Represents the class Person
        attribute - The attribute that we want to get from class Person
        
        Example :
            getattr(self.__class__,"count_items")
            So it would return the attribute by name count_items from the Person Class
        '''
        # Handle the attribute..

        # Set attribute to the class as NULL for attributes that doesn't exist.
        setattr(self.__class__,attribute,"NULL")
        # Return the attribute value
        return getattr(self.__class__,attribute)

# Execute
if __name__ == "__main__":
    instance_person = Person("Sherlock",25,"London","Programmer") # Returns an instance of the person class.
    # Print the instance
    print(instance_person)
    # Display details
    print(instance_person())
    #Select an attribute.
    print(instance_person.name) # Return the name as Sherlock
    # Method process_a doesn't exist in the class Person and method __getattr__ will get invoked...
    print(instance_person.process_a) # Returns NULL since value is set as NULL inside the __getattr__ method.

    # Method process_z doesn't exist in the class Person and method __getattr__ will get invoked...
    print(instance_person.process_z) # Returns NULL since value is set as NULL inside the __getattr__ method.

    # Access the Class and instance dict to know more about the class & instance attributes.
    
    '''
        Class Dictionary will contain all the attributes at the class level. 
        * It will not contain the attributes inside of the __init__ method.
    '''
    print("\n Class Dictionary ::  {} \n ".format(Person.__dict__))
    
    '''
        Class Instance Dictionary will contain all the attributes that are present inside of the 
        __init__ method.

        * It will not contain the attributes at class level such as ;
            1. Class Variables.
            2. Methods of the Class (InstanceMethod, ClassMethod, StaticMethod)
    '''
    print("\n Class Instance Dictionary  ::  {} \n".format(instance_person.__dict__))