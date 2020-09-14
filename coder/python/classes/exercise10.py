'''
    In Python a Class is defined using class keyword.
    A class is used for logical grouping of various methods.
    In simple terms please appreciate the fundamentals of OOPS.
    A Class is needed for various operations and a class can have any number of methods.
    
    # Defining a simple class
    class Person:
        pass

    This is the simplest class and just has pass, the interpreter will create a class named Person.
    To create an instance of class Person:
        instance_person = Person() # Returns an instance of the person class.

    A Class with a Constructor looks as follows;

        class Person:

            def __init__(self,name,age,location,profession):
                """
                    This Constructor takes 4 arguments;
                    :param name: Name of the Person
                    :param age: Age of the Person
                    :param location: Location of the Person
                    :param profession: Profession of the Person
                """

    While creating the instance of the class Person we also need to pass the required constructor arguments.
    instance_person = Person() # Returns an error (Will ask for arguments)
    instance_person = Person("Tom",20,"London","Programmer") # Returns an instance of the person class.


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

    Usage: When to use these methods?
    ------------------------------------

    1. Instance method:
        1. You want all of your methods to be secured at instance level.
        2. You want to follow strict OOPS concept of 'Classes and Objects'.
        3. You want to Use Contructors for processing the instance data.
        4. You want to tie your functionality to the instance of the class.
        5. You want the clients to create an instance of the class and then access the functionality.


    2. Class method:
        1. You want all of your methods to be secured at class level.
        2. You want to tie your functionality directly to the class.
        3. You don't want the clients to create an instance of the class and then access the functionality.
        4. You want to avoid instances creation and clients can call the method directly.
        5. You dont want to prefer using constructors at large for instance variables.
        6. Process all the attributes and variables at class level


    3. Static method:
        1. You want your method to be as good as a plain function.
        2. You dont want to tie the functionality either at class or instance level.
        3. You want to avoid instances creation and clients can call the method directly.
        4. You dont want to prefer using constructors at large for instance variables.
        5. You want to build utilities and reusbale functions.
        6. You want to avoid complexity and keep things very simple.


    Examples with Definitions and Documentations        
    ---------------------------------------------

    Class with instance method
    ----------------------------

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
            """
            # Check condition and return as True/False
            if self.age>self.qualify_age:
                return True
            else False
   

    Class with instance method, class method
    -----------------------------------------

    class Person:

        # Define a Class variable for age qualification
        QUALIFY_AGE=20

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
                    6. Class Variables defined at class level are also accessible inside __init__ 
                       and the instance methods of the class
            """
            # Assign the parameters to the instance variables
            self.name=name
            self.age=age
            self.location=location
            self.profession=profession

        """
            Note :: The method instance_met_check_qualification is an instance method
            We can access the class variable QUALIFY_AGE inside the instance method
        """        

        def instance_met_check_qualification(self):
            # We can access the class variable QUALIFY_AGE inside the instance method
            # ** An instance is a child of the class hence the class variable is accessible via instance of the class **
            # Check the qualification and return as True or False
            return True if self.actual_age>self.QUALIFY_AGE else False


        """
            Note :: The method check_qualification is a classmethod
                1. The class methods have a decorator @classmethod added on a method
                2. The classmethod has a default argument cls
                3. The classmethod can be accessed without creating an instance of the class
                    Example :
                        Person.check_qualification(actual_age)
                4. Inside classmethod we cant access the instance variables defined inside the __init__ constructor
            
            At run time following actions happen;
                1. The method def check_qualification becomes a class method            
                2. The argument cls becomes the class itself
        """

        @classmethod
        def check_qualification(cls,actual_age):
            # The variables declared at class level can be accessed as cls.QUALIFY_AGE
            # Note: ** We cant access instance variable inside the classmethod ** 
            if actual_age>cls.QUALIFY_AGE:
                return True
            else False


    Class with instance method, class method, static method
    --------------------------------------------------------

    class Person:

        # Define a Class variable for age qualification
        QUALIFY_AGE=20

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
                    6. Class Variables defined at class level are also accessible inside __init__ 
                       and the instance methods of the class
            """
            # Assign the parameters to the instance variables
            self.name=name
            self.age=age
            self.location=location
            self.profession=profession

        """
            Note :: The method instance_met_check_qualification is an instance method
            We can access the class variable QUALIFY_AGE inside the instance method
        """        

        def instance_met_check_qualification(self,a,b,c):
            # We can access the class variable QUALIFY_AGE inside the instance method
            # ** An instance is a child of the class hence the class variable is accessible via instance of the class **
            # Check the qualification and return as True or False
            return True if self.actual_age>self.QUALIFY_AGE else False


        """
            Note :: The method check_qualification is a classmethod
                1. The class methods have a decorator @classmethod added on a method
                2. The classmethod has a default argument cls and its mandatory
                3. The classmethod can be accessed without creating an instance of the class
                    Example :
                        Person.check_qualification(actual_age)
                4. Inside classmethod we cant access the instance variables defined inside the __init__ constructor
                    or any of the instance variables
            
            At run time following actions happen;
                1. The method def check_qualification becomes a class method            
                2. The argument cls becomes the class itself
        """

        @classmethod
        def check_qualification(cls,actual_age):
            """
                The variables declared at class level can be accessed as cls.QUALIFY_AGE
                Note: ** We cant access instance variable inside the classmethod ** 
            """

            # Check the condition and return as True/False

            if actual_age>cls.QUALIFY_AGE:
                return True
            else False

        """
            Note:: The method static_met_check_qualification is a staticmethod
            1. The static methods have a decorator @staticmethod added on a method
            2. They dont have any default arguments
            3. The staticmethod can be accessed without creating an instance of the class
                Example:
                    Person.static_met_check_qualification(actual_age,expected_age)
            4. Inside the staticmethod we cant access the instance variables defined inside the __init__ constructor
                or any of the instance variables
            5. Inside the staticmethod we can access the variables declared at class level using class directly;
                Example: Person.QUALIFY_AGE
            6. Static methods are plain function
        """

        @staticmethod
        def static_met_check_qualification(actual_age,expected_age):
            """
                The variables declared at class level can be accessed using class name as Person.QUALIFY_AGE
                Note: ** We cant access any instance variable inside the staticmethod ** 
            """
            # Check the condition and return as True/False
            if actual_age > expected_age:
                return True
            else False
'''

import abstraction
# Define a Person class and perform related operations

class Person(abstraction.AbstractPerson):

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


    def tests(self):
        '''
            Processes the records of the person...
        '''

# Execute
if __name__ == "__main__":
    # Class name is Person ....
    #object_person = Person() # If __init__ has no args..
    instance_person = Person("Sherlock",20,"London","Programmer") # Returns an instance of the person class.
    # Print the instance
    print(instance_person)
    
    # Display details
    print(instance_person.about())
    # Check for Qualification
    print(instance_person.check_qualification())

    # Access the Class and instance dict to know more about the class & instance attributes.
    print("\n Class Dictionary ::  {} \n ".format(Person.__dict__))
    print("\n Class Instance Dictionary  ::  {} \n".format(instance_person.__dict__))