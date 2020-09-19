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

    Method :: __del__
    -------------------

        In this example , we will a special magic method __del__ for deleting attributes of the class.
        If you define __del__ method, it will get invoked only at the end of all execution of the class.

    Method :: __setattr__
    -----------------------

        In this example , we will a special magic method __setattr__ for setting attributes of the class.
        If you define __setattr__ method, it will get invoked whenever we set attributes to the instance
        of the class.
        
        Use this method only if you would like to customize the way the attributes are set in python.
        ---------------------------------------------------------------------------------------------

        Setting the value of an attribute.
        This method gets invoked whenever a new attribute is set at the instance level.
        For ex: 
            - I have a class named Person
            - I create an instance of Person class as instance_person = Person()
            - When I set some value to the instance:
                - instance_person.account_number = 10AXYZBHEAPRFULL5000
                - account_number is an attribute
                - account_number is set to the instance of the Person Class, thus becomes
                  an instance variable.

            - def __setattr__(self,attr,value):
                """
                    :param self : Instance of the Class
                    :param attr : To which attribute value must be set?
                                  Ex: Attribute is account_number defined above.
                    :param value: Whats the value to be set to the attribute?
                                  Ex: Value 10AXYZBHEAPRFULL5000 set to instance attribute - account_number
                """              
                # Call built-in setattr and set the value to an attribute...  
                setattr(self.__class__,attr,value)


        The above code will set the value to an attribute and it will be accessible to the instance
        of the class.

        This method __setattr__ will get invoked whenever an attribute is set to instance
        of the class, example instance_person.account_number defined above.



        ** Note :: **
        Override this method if you would wish to customize the way the attributes
        are being set default by python.

        For example: You can override this to allow only string attributes
        to be set to the class and its instance.

        Ex: 
            - To allow only attributes of string type to be set.
            if value.__class__ == str:
                setattr(self.__class__,attribute,value)

            - To allow only attributes of integer type to be set.
            if value.__class__ == int:
                setattr(self.__class__,attribute,value)
        Now Remember that if you would override the method as above,
        the attributes of any other types such as lists, dicts, tuples or
        objects of any kind will not be set at the class/instance level.

    Method :: __new__
    -----------------------

        In this example , we will a special magic method __new__ for controlling instances creation.
        If you define __new__ method, it will get invoked whenever we create instance
        of the class.
        
        Use this method only if you would like to customize the way the instances are created in python.
        -------------------------------------------------------------------------------------------------
        
        CASE 1 :: Create and return the instance of the Class.
        --------------------------------------------------------

            def __new__(cls,*args):
                # Creating an instance of the Class.
                # Use the built-in object to create the instance.
                instance = object.__new__(cls)
                # Return the instance
                return instance

        CASE 2 :: Create and return the instance of the Class. Make sure only 1 instance is created.
        --------------------------------------------------------------------------------------------
            # Class Variable to maintain the instance creation
            ---------------------------------------------------

            CLASS_INSTANCE_HOLDER = {}
            
            def __new__(cls,*args):
                # The instance will get created only once. The instance gets stored in class variable CLASS_INSTANCE_HOLDER.

                if not cls.CLASS_INSTANCE_HOLDER.__contains__('instance'):
                    # Creating an instance of the Class.
                    # Use the built-in object to create the instance.
                    instance = object.__new__(cls)
                    cls.CLASS_INSTANCE_HOLDER['instance']=instance
                return cls.CLASS_INSTANCE_HOLDER['instance']

            Note ::

                Create 2 instances and check if both the instances are at same memory location.

                # Returns an instance of the person class.
                instance_person = Person("Sherlock",35,"London","Programmer")

                # Returns an instance of the person class.
                instance_person_b = Person("Tom",30,"Sweden","Programmer")

                # Assert the memory location and they must be same.
                print(id(instance_person) == id(instance_person_b))
                assert id(instance_person) == id(instance_person_b)


        CASE 3 :: Create and return the instance of the Class as None. Instance will not be usable.
        --------------------------------------------------------------------------------------------

            # When returned as None, the instance is not usable by anyone.
            # Methods, Properties nothing will be accessible.
            
            def __new__(cls,*args):
            
                # Creating an instance of the Class.
                # Use the built-in object to create the instance.
                instance = object.__new__(cls)
                return None

            In this case if we would try to access any method of the class when the instance is None,
            we would get AttributeError as below.

            Lets say we have a method called def about(), we try to access it ,

                Traceback (most recent call last):
                  File "exercise10.py", line 310, in <module>
                    instance_person.about()
                AttributeError: 'NoneType' object has no attribute 'about'

            * We get AttributeError since Instance is None and 'NoneType' object has no attribute 'about'.

            * If in case the instance would have got created, it would have worked normally.


        CASE 4 :: Raise Exception during instance creation . Instance will not be usable.
        --------------------------------------------------------------------------------------------

            # When returned as None, the instance is not usable by anyone.
            # Methods, Properties nothing will be accessible.
            
            def __new__(cls,*args):
            
                # Creating an instance of the Class.
                # Use the built-in object to create the instance.
                instance = object.__new__(cls)
                raise Exception("Instance Creation not Permitted. Class is Secured.")
            
            In this case we would get error as follows;

                Traceback (most recent call last):
                  File "exercise10.py", line 380, in <module>
                    instance_person = Person("Sherlock",15,"London","Programmer")
                  File "exercise10.py", line 232, in __new__
                    raise Exception("Instance Creation not Permitted. Class is Secured.")

            Consider this Simple Class

            class Person:

                def __new__(cls,*args):
                
                    # Creating an instance of the Class.
                    # Use the built-in object to create the instance.
                    instance = object.__new__(cls)
                    raise Exception("Instance Creation not Permitted. Class is Secured.")

                def about(self):
                    return 

                def __del__(self):
                    print("__del__ Called...")

            # Create an instance of Person and run

            # Returns an instance of the person class.
            instance_person = Person("Sherlock",15,"London","Programmer")

            In this case we would get error as follows;

                Traceback (most recent call last):
                  File "exercise10.py", line 380, in <module>
                    instance_person = Person("Sherlock",15,"London","Programmer")
                  File "exercise10.py", line 232, in __new__
                    raise Exception("Instance Creation not Permitted. Class is Secured.")

            instance_person.about() # This line will not get executed.
            
            But method __del__ will get called since its a magic method, it will get called at end by default.


    Callable & Non-Callable Attributes :
    -----------------------------------

        Callable Attributes -> 
            - Attributes of the class that are actually executed using () braces.
            - Example : Methods of the Class

        Non-Callable Attributes -> 

            - Attributes of the class that are actually not executed using () braces.
            - If you would execute them it would result in TypeError
            - Example : Instance Variables, Class Variables, Properties.

    __new__ and __init__
    ---------------------

        __new__ : Is for Instance Creation. Can be customized to control the creation of instances.
        __init__ : Is used as a Constructor. It needs the instance that was created by __new__.

        __init__ method gets called only after __new__ because __new__ gives us the instane of the class.
        __init__ method needs an instance to perform any task, it uses the instance created under __new__.

'''

# Define a Person class and perform related operations

class Person:

    def __new__(cls,*args):
        '''
            Create an instance and return.
            __new__ gets invoked before __init__ method.

            Print the Instance and the Arguments

            Note ::

                Create an instance of the Person class and invoke about method.

                # Returns an instance of the person class.
                instance_person = Person("Sherlock",15,"London","Programmer")
                instance_person.about()

                # Returns an instance of the person class.
                instance_person_b = Person("Tom",30,"Sweden","Programmer")
                instance_person_b.about()
        '''
        # Creating an instance of the Class.

        instance = object.__new__(cls)
        print("\n\n From __new__ block!")
        print(object)
        print("Instance is - {} ".format(instance))
        print("Args passed during instance creation - {} \n\n".format(args))
        return instance
    
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

            __init__ method gets called only after __new__ because __new__ gives us the instane of the class.
            __init__ method needs an instance to perform any task, it uses the instance created under __new__.
        """
        print("\nFrom __init__ :: Invoke the Constructor \n")
        # Assign the parameters to the instance variables
        self.name=name
        self.age=age
        self.location=location
        self.profession=profession
        self.qualify_age=20 # We can also hard-code instance variables

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

    def about(self):
        """
            # As you see here - the self at run time becomes instance of the class
            # With self we can thus access the instance variables of the class such as ;
            #self.age, self.qualify_age,self.name,self.location,self.profession
            This method displays details of the Person
        """
        # Display details
        return "My name is {} and I am {} , I am From {} and I am a {}".format(self.name,
            self.age,self.location,self.profession)

    def process(self):
        '''
            Processes the records of the person...
        '''
        # Check a condition and process. Print details of the person if they would be qualified.
        return self.about() if bool(self.check_qualification()) else "Unqualified!!"

    def __call__(self,*arguments):
        '''
            This method is invoked when an instance of the class is called.
            Example:
                instance_person = Person("Sherlock",20,"London","Programmer") # Returns an instance of the person class.
                Calling the instance as instance_person() -> Will invoke this __call__ method.
        '''
        # Execute the process
        return self.process()

    def __setattr__(self,attribute,value):
        '''
            Setting the value of an attribute.
            This method gets invoked whenever a new attribute is set at the instance level.
            For ex: 
                - I have a class named Person
                - I create an instance of Person class as instance_person = Person()
                - When I set some value to the instance:
                    - instance_person.account_number = 10AXYZBHEAPRFULL5000
                    - account_number is an attribute
                    - account_number is set to the instance of the Person Class, thus becomes
                      an instance variable.
            This method __setattr__ will get invoked whenever an attribute is set to instance
            of the class, example instance_person.account_number defined above.

            ** Note :: **
            Override this method if you would wish to customize the way the attributes
            are being set default by python.


            - def __setattr__(self,attr,value):
                """
                    :param self : Instance of the Class
                    :param attr : To which attribute value must be set?
                                  Ex: Attribute is account_number defined above.
                    :param value: Whats the value to be set to the attribute?
                                  Ex: Value 10AXYZBHEAPRFULL5000 set to instance attribute - account_number
                """              
                # Call built-in setattr and set the value to an attribute...  
                setattr(self.__class__,attr,value)


            For example: You can override this to allow only string attributes
            to be set to the class and its instance.

            Ex: 
                - To allow only attributes of string type to be set.
                if value.__class__ == str:
                    setattr(self.__class__,attribute,value)

                - To allow only attributes of integer type to be set.
                if value.__class__ == int:
                    setattr(self.__class__,attribute,value)
            Now Remember that if you would override the method as above,
            the attributes of any other types such as lists, dicts, tuples or
            objects of any kind will not be set at the class/instance level.
        '''
        print("Set value as - {} to the attribute - {} ".format(value,attribute))
        # Set the value of the attribute.
        setattr(self.__class__,attribute,value)

    def __del__(self):
        '''
            This method will be called only at the end.
            Delete the object
            Use this for destructor activities such as deletion or removal of ;
                - DB connection
                - File Operations
                - Huge memory operations
                ~ Similar tasks...
        '''
        print("Memory location of self - {} ".format(id(self)))
        print("Delete the object - {} ".format(self))
        del self

# Execute
if __name__ == "__main__":
     # Returns an instance of the person class.
     # Since __new__ is defined for Person Class. It will get invoked when the instance is created.
    instance_person = Person("Sherlock",15,"London","Programmer")
    instance_person.about()

