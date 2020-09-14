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

    In the following example we shall use 2 special methods __getattr__ and __getattribute__


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

    Method :: __getattribute__
    ----------------------------

    	In this example , we will see a special magic method __getattribute__ 
        This method gets invoked whenever any attribute of the class would get called.

        For example :

            class Person :
                def __init__(self,name,age,location,profession):
                        self.name=name
                        self.age=age
                        self.location=location
                        self.profession=profession

                def method_a(self):
                    return "Hello"
            
            # Instance of Person class
            instance_person = Person("Sherlock",25,"London","Programmer") # Returns an instance of the person class.
            instance_person.name # Special method __getattribute__ gets invoked and value is returned. 
            instance_person.age # Special method __getattribute__ gets invoked and value is returned. 
            instance_person.location # Special method __getattribute__ gets invoked and value is returned. 
            instance_person.profession # Special method __getattribute__ gets invoked and value is returned. 
            instance_person.method_a() # Special method __getattribute__ gets invoked and value is returned. 

    Method :: __getattr__

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

    Order ::

        Any attribute access has to first go via special method - __getattribute__
        If __getattribute__ can find your attribute inside of class/instance:
            Return the value of the attribute
        Else
            Check if there is __getattr__ method to handle AttributeError
            Check if any value is assigned to unknown attribute.
            Else
                Raise AttributeError and BREAK

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

    def __getattribute__(self,attribute):
        '''
            This method gets called for all the attributes of the class.
            Return the value of the attribute.
            :param attribute: The attribute being accessed.

            If you wish to override the way the attributes are returned,
            then this is the right place.
            For ex: Return only the string attributes:
                super(Person,self).__getattribute__(attribute) if attribute.__class__ == str else "NULL"

            For ex: Return only the int attributes:
                super(Person,self).__getattribute__(attribute) if attribute.__class__ == int else "NULL"
        '''
        # Print the attribute details.
        print("GET :: - {} ".format(attribute))
        # Return the value of the attribute.
        return super(Person,self).__getattribute__(attribute)

    def __getattr__(self,attribute):
        '''
            Handle the attribute in case of AttributeError
            :param attribute: The attribute being accessed.
        '''
        # Handle the attribute..

        # Set attribute to the class as NULL for attributes that doesn't exist.
        print("GETATTR :: attribute - {} & value - {} ".format(attribute,"NULL"))
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
    print(instance_person.age) # Returns 25
    print(instance_person.location) # Returns London
    print(instance_person.profession) # Returns Programmer

    # Method process_a doesn't exist in the class Person and method __getattr__ will get invoked...
    print(instance_person.process_a) # Returns NULL since value is set as NULL inside the __getattr__ method.

    # Method process_z doesn't exist in the class Person and method __getattr__ will get invoked...
    print(instance_person.process_z) # Returns NULL since value is set as NULL inside the __getattr__ method.


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