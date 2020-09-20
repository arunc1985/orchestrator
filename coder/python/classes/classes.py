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

    Callable & Non-Callable Attributes :
    -----------------------------------

        Callable Attributes -> 
            - Attributes of the class that are actually executed using () braces.
            - Example : Methods of the Class

        Non-Callable Attributes -> 

            - Attributes of the class that are actually not executed using () braces.
            - If you would execute them it would result in TypeError
            - Example : Instance Variables, Class Variables, Properties.

    In this example we will see simple class definitions and create the instances of the class.
'''

                                                # Example 1
#---------------------------------------------------------------------------------------------------------

"""
# Define a Simple Class and create an instance.
# The class below has no body - interpreter will just create the class without body and it will be stored in some memory location.
# To create an instance for this class:
    instance_employee = Employee()# Call the Class using braces - ()
    print(instance_employee) # Prints Instance and it will be stored in some memory location.
# NOTE :: 
    The location of the instance in memory is different from that of the Class itself.
    Get the memory location of the class - print(id(Employee))
    Get the memory location of the instance of the class - print(id(instance_employee))
    ** They both will be different.

Execution ::
    
    # Instance Creation
    instance_employee = Employee()# Call the Class

Importance of instance of the class ::
    - Its created from the class.
    - Instance of the class can have access to the attribute of the class.
    - Instance and Class are both stored in different memory location.
    - Using Instance we can also perform any action inside of the class.
    
"""
class Employee:
    pass


#---------------------------------------------------------------------------------------------------------


                                                # Example 2
#---------------------------------------------------------------------------------------------------------



"""
# Define a Simple Class and create an instance.
# The class below has 1 methods - interpreter will just create the class and it will be stored in some memory location.

Methods ::
    
    def __init__ : Used as a Constructor. For Class initialization.
                   In this case we initialize the class with following attributes:
                    1. name
                    2. location
                    3. profession


# To create an instance for this class:
    instance_employee = Employee(name,location,profession)
    print("Instance is - {} ".format(instance_employee))

# NOTE :: 
    The location of the instance in memory is different from that of the Class itself.
    Get the memory location of the class - print(id(Employee))
    Get the memory location of the instance of the class - print(id(instance_employee))
    ** They both will be different.

Execution ::
    
    # Instance Creation
    Employee(name,location,profession)
    instance_employee = Employee("Arun","Chennai","Programmer")
    print("Instance is - {} ".format(instance_employee))
    print("Name is - {} ".format(instance_employee.name))
    print("Location is - {} ".format(instance_employee.location))
    print("Profession is - {} ".format(instance_employee.profession))
    print("Get the memory location of the class - {} ".format(id(Employee)))
    print("Get the memory location of the instance of the class - {} ".format(id(instance_employee)))

    
"""
class Employee:

    def __init__(self,name,location,profession):
        '''
            This Block is used for initialization.
            It gets called when the instance is created.
            The arguments to this method name,location,profession are all positional arguments and value must be
            passed while creating the instance.

            Example::

                instance_employee = Employee(name,location,profession)
                When we create an instance as above, the first mandate argument self
                becomes the instance of the class.

                * So self becomes instance_employee *

            The argument self defined above is a pre-requisite for instance methods.
            This argument self becomes instance of the class once the class is run and executed.
            There are various types of methods in Class - Refer detailed documentation above.

            The arguments that are set here inside the __init__ constructor can be accessed
            inside of all the instance methods of the class.
        '''
        
        # Set the arguments to the instance of the class to be used inside instance methods.
        # Set the name of the person to the instance of the class
        self.name = name
        # Set the location of the person to the instance of the class
        self.location = location
        # Set the profession of the person to the instance of the class
        self. profession = profession
    
#---------------------------------------------------------------------------------------------------------


                                                # Example 3
#---------------------------------------------------------------------------------------------------------



"""
# Define a Simple Class and create an instance.
# The class below has 2 methods - interpreter will just create the class  and it will be stored in some memory location.

Methods ::
    
    def __init__ : Used as a Constructor. For Class initialization.
                   In this case we initialize the class with following attributes:
                    1. name
                    2. location
                    3. profession

    def about : Display all details about an employee.

# To create an instance for this class:
    instance_employee = Employee(name,location,profession)
    print(instance_employee) # Prints Instance and it will be stored in some memory location.
# NOTE :: 
    The location of the instance in memory is different from that of the Class itself.
    Get the memory location of the class - print(id(Employee))
    Get the memory location of the instance of the class - print(id(instance_employee))
    ** They both will be different.

Execution ::
    
    # Instance Creation
    Employee(name,location,profession)
    instance_employee = Employee("Arun","Chennai","Programmer")
    print("Instance is - {} ".format(instance_employee))
    print("Name is - {} ".format(instance_employee.name))
    print("Location is - {} ".format(instance_employee.location))
    print("Profession is - {} ".format(instance_employee.profession))
    print("Get the memory location of the class - {} ".format(id(Employee)))
    print("Get the memory location of the instance of the class - {} ".format(id(instance_employee)))

    print("Get the Employee Details ..")
    emp_details = instance_employee.about()
    print(emp_details)
    
"""
class Employee:

    def __init__(self,name,location,profession):

        '''
            This Block is used for initialization.

            __init__ is the Constructor. Its a Magic/Special Method.

            It gets called when the instance is created.
            The arguments to this method name,location,profession are all positional arguments and value must be
            passed while creating the instance.

            Example::

                instance_employee = Employee(name,location,profession)
                When we create an instance as above, the first mandate argument self
                becomes the instance of the class.

                * So self becomes instance_employee *

            The argument self defined above is a pre-requisite for instance methods.
            This argument self becomes instance of the class once the class is run and executed.
            There are various types of methods in Class - Refer detailed documentation above.

            The arguments that are set here inside the __init__ constructor can be accessed
            inside of all the instance methods of the class.
        '''
        
        # Set the arguments to the instance of the class to be used inside instance methods.
        # Set the name of the person to the instance of the class
        self.name = name
        # Set the location of the person to the instance of the class
        self.location = location
        # Set the profession of the person to the instance of the class
        self. profession = profession

    
    def about(self):
        '''
            Display details about an Employee.
            Use the instance variables : self.name, self.location, self.profession
        '''
        return "Hello All! My name is {} and I am from {} and I am {}".format(self.name,self.location,self.profession)


#---------------------------------------------------------------------------------------------------------


                                                # Example 4
#---------------------------------------------------------------------------------------------------------

"""
# Define a Simple Class and create an instance.
# The class below has 2 methods - interpreter will just create the class  and it will be stored in some memory location.

Methods ::
    
    def __init__ : Used as a Constructor. For Class initialization.
                   In this case we initialize the class with following attributes:
                    1. name
                    2. location
                    3. profession

    def about : Display all details about an employee.

# The class below has 3 properties

Properties ::
    
    def name: Return the name 
    def location: Return the location
    def profession: Return the profession

    * Properties are used for :
        - Returning the value of an attribute.
        - They are called by the instance of the class.
            - instance_employee = Employee(name,location,profession)
            - print(instance_employee.name)
            - print(instance_employee.location)
            - print(instance_employee.profession)
        - They are not called using braces - ()
        - But methods are called using braces - ()
            - instance_employee.about()

# To create an instance for this class:
    instance_employee = Employee(name,location,profession)
    print(instance_employee) # Prints Instance and it will be stored in some memory location.
# NOTE :: 
    The location of the instance in memory is different from that of the Class itself.
    Get the memory location of the class - print(id(Employee))
    Get the memory location of the instance of the class - print(id(instance_employee))
    ** They both will be different.


Execution ::
    
    # Instance Creation
    Employee(name,location,profession)
    instance_employee = Employee("Arun","Chennai","Programmer")
    print("Instance is - {} ".format(instance_employee))
    print("Name is - {} ".format(instance_employee.name))
    print("Location is - {} ".format(instance_employee.location))
    print("Profession is - {} ".format(instance_employee.profession))
    print("Get the memory location of the class - {} ".format(id(Employee)))
    print("Get the memory location of the instance of the class - {} ".format(id(instance_employee)))

    print("Get the Employee Details ..")
    emp_details = instance_employee.about()
    print(emp_details)

    print("Access the various properties and get details..")
    # Print the properties
    print("Name is - {} ".format(instance_employee.get_name))
    print("Location is - {} ".format(instance_employee.get_location))
    print("Profession is - {} ".format(instance_employee.get_profession))


"""
class Employee:

    #Define a Class Variable here...
    OFFICE_NAME=""

    def __init__(self,name,location,profession):

        '''
            This Block is used for initialization.

            __init__ is the Constructor. Its a Magic/Special Method.

            It gets called when the instance is created.
            The arguments to this method name,location,profession are all positional arguments and value must be
            passed while creating the instance.

            Example::

                instance_employee = Employee(name,location,profession)
                When we create an instance as above, the first mandate argument self
                becomes the instance of the class.

                * So self becomes instance_employee *

            The argument self defined above is a pre-requisite for instance methods.
            This argument self becomes instance of the class once the class is run and executed.
            There are various types of methods in Class - Refer detailed documentation above.

            The arguments that are set here inside the __init__ constructor can be accessed
            inside of all the instance methods of the class.

            The arguments that are set here inside the __init__ constructor are the instance
            Variables of the class.

            The arguments that are set at class level are known as Class Variables.


            The variables that are set at the class level are accessible inside of the
            instance methods of the class. For ex: This variable OFFICE_NAME is 
            accessible inside method about defined below.

            How can we access the class variables inside of the instance method?
            The variables that are defined at the class level such as class variables,
            methods are always accessible to the instance since an instance is a child of
            the class...

        '''
        
        # Set the arguments to the instance of the class to be used inside instance methods.
        # Set the name of the person to the instance of the class
        self.name = name
        # Set the location of the person to the instance of the class
        self.location = location
        # Set the profession of the person to the instance of the class
        self. profession = profession

    
    def about(self):
        '''
            Display details about an Employee
            You can access class variable OFFICE_NAME inside this method
            as self.OFFICE_NAME using the instance self.
        '''
        return "Hello All! My name is {} and I am from {} and I am {}".format(self.name,self.location,self.profession)

    @property
    def get_name(self):
        '''
            Return the name of the employee
        '''
        return self.name


    @property
    def get_location(self):
        '''
            Return the location of the employee
        '''
        return self.location
    

    @property
    def get_profession(self):
        '''
            Return the profession of the employee
        '''
        return self.profession
        

#---------------------------------------------------------------------------------------------------------


                                                # Example 5
#---------------------------------------------------------------------------------------------------------


"""
# Define a Simple Class and create an instance.
# The class below has 3 methods - interpreter will just create the class  and it will be stored in some memory location.

Methods ::
    
    def __init__ : Used as a Constructor. For Class initialization.
                   In this case we initialize the class with following attributes:
                    1. name
                    2. location
                    3. profession

    def about : Display all details about an employee.

    def check_employee_qualification : Check Employee's Qualification based on experience level.

# The class below has 3 properties

Properties ::
    
    def name: Return the name 
    def location: Return the location
    def profession: Return the profession

    * Properties are used for :
        - Returning the value of an attribute.
        - They are called by the instance of the class.
            - instance_employee = Employee(name,location,profession)
            - print(instance_employee.name)
            - print(instance_employee.location)
            - print(instance_employee.profession)
        - They are not called using braces - ()
        - But methods are called using braces - ()
            - instance_employee.about()

# To create an instance for this class:
    instance_employee = Employee(name,location,profession)
    print(instance_employee) # Prints Instance and it will be stored in some memory location.
# NOTE :: 
    The location of the instance in memory is different from that of the Class itself.
    Get the memory location of the class - print(id(Employee))
    Get the memory location of the instance of the class - print(id(instance_employee))
    ** They both will be different.


Execution ::
    
    # Instance Creation
    Employee(name,location,profession)

    print("\n\n")

    instance_employee = Employee("Arun","Chennai","Programmer",15)
    print("Instance is - {} ".format(instance_employee))
    print("Name is - {} ".format(instance_employee.name))
    print("Location is - {} ".format(instance_employee.location))
    print("Profession is - {} ".format(instance_employee.profession))
    print("Experience is - {} ".format(instance_employee.experience))
    print("Get the memory location of the class - {} ".format(id(Employee)))
    print("Get the memory location of the instance of the class - {} ".format(id(instance_employee)))
    
    print("\n\n")

    print("Access the various properties and get details..")
    # Print the properties
    print("Name is - {} ".format(instance_employee.get_name))
    print("Location is - {} ".format(instance_employee.get_location))
    print("Profession is - {} ".format(instance_employee.get_profession))

    print("\n\n")

    print("Get the Employee Details ..")
    emp_details = instance_employee.about()
    print(emp_details)

    print("\n\n")

    print("Check the Employee Qualification ..")
    emp_details = instance_employee.check_employee_qualification()
    print(emp_details)

    print("\n\n")

    print("Access the various properties and get details..")
    # Print the properties
    print("Name is - {} ".format(instance_employee.get_name))
    print("Location is - {} ".format(instance_employee.get_location))
    print("Profession is - {} ".format(instance_employee.get_profession))

"""

class Employee:

    # Define a Class Variable.
    EXPECTED_EXPERIENCE_IN_YEARS=5

    def __init__(self,name,location,profession,experience):

        '''
            This Block is used for initialization.

            __init__ is the Constructor. Its a Magic/Special Method.

            It gets called when the instance is created.
            The arguments to this method name,location,profession are all positional arguments and value must be
            passed while creating the instance.

            Example::

                instance_employee = Employee(name,location,profession)
                When we create an instance as above, the first mandate argument self
                becomes the instance of the class.

                * So self becomes instance_employee *

            The argument self defined above is a pre-requisite for instance methods.
            This argument self becomes instance of the class once the class is run and executed.
            There are various types of methods in Class - Refer detailed documentation above.

            The arguments that are set here inside the __init__ constructor can be accessed
            inside of all the instance methods of the class.

            :param name: Name of the Employee - String
            :param location: Base Location of the Employee - String
            :param profession: Job/Profession of the Employee - String
            :param experience: Experience of the Employee in Years - Integer
        '''
        
        # Set the arguments to the instance of the class to be used inside instance methods.
        # Set the name of the person to the instance of the class
        self.name = name
        # Set the location of the person to the instance of the class
        self.location = location
        # Set the profession of the person to the instance of the class
        self. profession = profession
        # Set the experience of the person to the instance of the class
        self.experience = experience

    
    def about(self):
        '''
            Display details about an Employee
        '''
        return "Hello All! My name is {} and I am from {} and I am {}".format(self.name,self.location,self.profession)


    def check_employee_qualification(self):
        '''
            Check the qualification of an employee based on the years of experience.
            If an employee's years of experience is >= expected experience in years:
                THEN Employee is Qualified!
            else
                Employees is not Qualified!
        '''
        # Add an if-condition to check if an employee is qualified.
        if self.experience >= self.EXPECTED_EXPERIENCE_IN_YEARS:
            return "Employee - {} is Qualified! ".format(self.name)
        else:
            return "Employee - {} is not Qualified! ".format(self.name)


    @property
    def get_name(self):
        '''
            Return the name of the employee
        '''
        return self.name


    @property
    def get_location(self):
        '''
            Return the location of the employee
        '''
        return self.location
    

    @property
    def get_profession(self):
        '''
            Return the profession of the employee
        '''
        return self.profession

    @property
    def get_experience(self):
        '''
            Return the experience of the employee in years
        '''
        return self.experience



#---------------------------------------------------------------------------------------------------------




                                                # Example 6
#---------------------------------------------------------------------------------------------------------


"""
# Define a Simple Class and create an instance.
# The class below has 3 methods - interpreter will just create the class  and it will be stored in some memory location.

Methods ::
    
    def __init__ : Used as a Constructor. For Class initialization.
                   In this case we initialize the class with following attributes:
                    1. name
                    2. location
                    3. profession

    def about : Display all details about an employee.

    def check_employee_qualification : Check Employee's Qualification based on experience level.

# The class below has 3 properties

Properties ::
    
    def name: Return the name 
    def location: Return the location
    def profession: Return the profession

    * Properties are used for :
        - Returning the value of an attribute.
        - They are called by the instance of the class.
            - instance_employee = Employee(name,location,profession)
            - print(instance_employee.name)
            - print(instance_employee.location)
            - print(instance_employee.profession)
        - They are not called using braces - ()
        - But methods are called using braces - ()
            - instance_employee.about()

# To create an instance for this class:
    instance_employee = Employee(name,location,profession)
    print(instance_employee) # Prints Instance and it will be stored in some memory location.
# NOTE :: 
    The location of the instance in memory is different from that of the Class itself.
    Get the memory location of the class - print(id(Employee))
    Get the memory location of the instance of the class - print(id(instance_employee))
    ** They both will be different.


Execution ::
    
    # Instance Creation
    Employee(name,location,profession)

    print("\n\n")

    instance_employee = Employee("Arun","Chennai","Programmer",15)
    print("Instance is - {} ".format(instance_employee))
    print("Name is - {} ".format(instance_employee.name))
    print("Location is - {} ".format(instance_employee.location))
    print("Profession is - {} ".format(instance_employee.profession))
    print("Experience is - {} ".format(instance_employee.experience))
    print("Get the memory location of the class - {} ".format(id(Employee)))
    print("Get the memory location of the instance of the class - {} ".format(id(instance_employee)))
    
    print("\n\n")

    print("Access the various properties and get details..")
    # Print the properties
    print("Name is - {} ".format(instance_employee.get_name))
    print("Location is - {} ".format(instance_employee.get_location))
    print("Profession is - {} ".format(instance_employee.get_profession))

    print("\n\n")

    print("Get the Employee Details ..")
    emp_details = instance_employee.about()
    print(emp_details)

    print("\n\n")

    print("Check the Employee Qualification ..")
    emp_details = instance_employee.check_employee_qualification()
    print(emp_details)

    print("\n\n")

    print("Access the various properties and get details..")
    # Print the properties
    print("Name is - {} ".format(instance_employee.get_name))
    print("Location is - {} ".format(instance_employee.get_location))
    print("Profession is - {} ".format(instance_employee.get_profession))

"""

class Employee:

    """
        Execute this class as shown below,

        if __name__ == "__main__":

            instance_employee = Employee("Arun","Chennai","Mentor",20)

            # Call staticmethod - check_employee_bonus
            '''
                Summary ::

                    A Staticmethod can be called by the class directly and also it can be
                    called by the instance of the class.
            '''
            print("\nCall Staticmethod - check_employee_bonus using the class directly\n")
            print("------------------------------------------------------------------")
            bonus = Employee.check_employee_bonus(90000)
            print("Output :: {} ".format(bonus))
            print("------------------------------------------------------------------\n\n")


            print("\nCall Staticmethod - check_employee_bonus using the instance of the class\n")
            print("------------------------------------------------------------------")
            bonus = instance_employee.check_employee_bonus(90000)
            print("Output :: {} ".format(bonus))
            print("------------------------------------------------------------------\n\n")


            # Call classmethod - check_employee_details
            '''
                Summary ::
                
                    A classmethod can be called by the class directly and also it can be
                    called by the instance of the class.
            '''

            print("\nCall Classmethod - check_employee_details using the class directly\n")
            print("------------------------------------------------------------------")
            details = Employee.check_employee_details(20)
            print("Output :: {} ".format(details))
            print("------------------------------------------------------------------\n\n")


            print("\nCall Classmethod - check_employee_details using the instance of the class\n")
            print("------------------------------------------------------------------")
            details = instance_employee.check_employee_details(20)
            print("Output :: {} ".format(details))
            print("------------------------------------------------------------------\n\n")



            # Call instancemethod - about and check_qualification
            '''
                Summary ::
                
                    An instancemethod can be called only by the instance of the class.
            '''

            print("\nCall instancemethod - check_employee_qualification using the instance of the class\n")
            print("------------------------------------------------------------------")
            details = instance_employee.check_employee_qualification()
            print("Output :: {} ".format(details))
            print("------------------------------------------------------------------\n\n")

            print("\nCall instancemethod - about using the instance of the class\n")
            print("------------------------------------------------------------------")
            details = instance_employee.about()
            print("Output :: {} ".format(details))
            print("------------------------------------------------------------------\n\n")

    """
    # Define a Class Variable.
    EXPECTED_EXPERIENCE_IN_YEARS=20

    def __init__(self,name,location,profession,experience):

        '''
            This Block is used for initialization.

            __init__ is the Constructor. Its a Magic/Special Method.

            It gets called when the instance is created.
            The arguments to this method name,location,profession are all positional arguments and value must be
            passed while creating the instance.

            Example::

                instance_employee = Employee(name,location,profession)
                Example ::
                    instance_employee = Employee("Arun","Chennai","Mentor",20)
                When we create an instance as above, the first mandate argument self
                becomes the instance of the class.

                * So self becomes instance_employee *

            The argument self defined above is a pre-requisite for instance methods.
            This argument self becomes instance of the class once the class is run and executed.
            There are various types of methods in Class - Refer detailed documentation above.

            The arguments that are set here inside the __init__ constructor can be accessed
            inside of all the instance methods of the class.

            :param name: Name of the Employee - String
            :param location: Base Location of the Employee - String
            :param profession: Job/Profession of the Employee - String
            :param experience: Experience of the Employee in Years - Integer
        '''
        
        # Set the arguments to the instance of the class to be used inside instance methods.
        # Set the name of the person to the instance of the class
        self.name = name
        # Set the location of the person to the instance of the class
        self.location = location
        # Set the profession of the person to the instance of the class
        self. profession = profession
        # Set the experience of the person to the instance of the class
        self.experience = experience
    
    def about(self):
        '''
            Display details about an Employee

            Note ::
                At run time the first argument to this method self becomes
                the instance of the class.

                instance_employee = Employee(name,location,profession)

                The first argument self will become as instance_employee

                The instance method must be always executed using the instance of the class.
                The method about must be called as follows;

                instance_employee.about()


            What is a instancemethod ?

             - A Method that has doesn't have any decorator @classmethod or @staticmethod.
             - A Method that has a mandate positional argument like classmethod.
             - The first argument to the method will get converted as the instance of the class itself at run time.
             - A Method that can have any number of arguments.
             - A Method that cannot be called by the class directly. We need to do instance creation.
             - A Method that can be called by the instance of the Class alone.

        '''
        return "Hello All! My name is {} and I am from {} and I am {}".format(self.name,self.location,self.profession)

    def check_employee_qualification(self):
        '''
            Check the qualification of an employee based on the years of experience.
            If an employee's years of experience is >= expected experience in years:
                THEN Employee is Qualified!
            else
                Employee is not Qualified!
        '''
        # Add an if-condition to check if an employee is qualified.
        if self.experience >= self.EXPECTED_EXPERIENCE_IN_YEARS:
            return "Employee - {} is Qualified! ".format(self.name)
        else:
            return "Employee - {} is not Qualified! ".format(self.name)

    @classmethod
    def check_employee_details(cls,employee_curr_experience):
        ''' 
            Return all employee details
            :param experience : Experience in years of an employee

            If an employee's years of experience is >= expected experience in years:
                THEN Employee is Qualified!
            else
                Employee is not Qualified!

            Note ::
                At run time the first argument to this method cls becomes
                the class itself.

                instance_employee = Employee(name,location,profession)

                The first argument cls will become as Employee

                A classmethod can be invoked without creating an instance of the class.
                Which means you can actually call the method check_employee_details as follows;

                Employee.check_employee_details(20)

                You can also call the classmethod using the instance of the class.
                instance_employee.check_employee_details(20)

            What is a Classmethod ?

             - A Method that has a decorator @classmethod.
             - A Method that has a mandate positional argument like instancemethod.
             - The first argument to the method will get converted as the class itself at run time.
             - A Method that can have any number of arguments.
             - A Method that can be called by the class directly. No need to go for instance creation.
             - A Method that can also be called by the instance of the Class.
        '''

        # Check and return as True or False
        print("Total Experience in Years is :: {} ".format(cls.EXPECTED_EXPERIENCE_IN_YEARS))
        return True if employee_curr_experience >= cls.EXPECTED_EXPERIENCE_IN_YEARS else False

    @staticmethod
    def check_employee_bonus(employee_salary):
        '''
            Given the Employee Salary find the Bonus.
            :param employee_salary: Employee's Salary.

            What is a Staticmethod ?

             - A Method that has a decorator @staticmethod.
             - A Method that doesnt have any mandate positional argument like instancemethod or classmethod.
             - A Method that is similar to a python function.
             - A Method that can have any number of arguments.
             - A Method that can be called by the class directly. No need to for instance creation.
             - A Method that can also be called by the instance of the Class.
        '''
        # Add Condition and find Bonus
        if employee_salary > 100000:
            return 10
        elif employee_salary > 70000 and employee_salary < 100000:
            return 12
        elif employee_salary > 50000 and employee_salary < 70000:
            return 14
        elif employee_salary > 30000 and employee_salary < 50000:
            return 16
        else :
            return 20

    @property
    def get_name(self):
        '''
            Return the name of the employee
        '''
        return self.name


    @property
    def get_location(self):
        '''
            Return the location of the employee
        '''
        return self.location
    

    @property
    def get_profession(self):
        '''
            Return the profession of the employee
        '''
        return self.profession

    @property
    def get_experience(self):
        '''
            Return the experience of the employee in years
        '''
        return self.experience

#---------------------------------------------------------------------------------------------------------


                                                # Example 7
#---------------------------------------------------------------------------------------------------------

# Define a Simple Class to test the instance method, class method and staticmethods.

class Tests_Methods_Accessibility:

    # Define Simple class variables
    CLASS_VARIABLE_TESTING=200000
    STATUS = True

    '''
        Define multiple methods to check the attributes among the methods.

        Questions ::
        ------------

        Q: Can I access a Classmethod inside of the instance method?
        A: Yes
            - How ?
            - An instance of the class is actually a child of the class.
            - Example :: instance_tests = Tests_Methods_Accessibility().
            - instance_tests is the child of the class and the class is Tests_Methods_Accessibility.
            - Whatever a class can access the instance of the class can also access it.
            - We can call the classmethod from the instancemethod using self,
              Ex: In this class we can call classmethod: tests_class_method from instancemethod as,
                --- self.tests_class_method()

        Q: Can I access a Class Variable inside of the instance method?
        A: Yes
            - How ?
            - We have 2 Class variables namely ;
                -- CLASS_VARIABLE_TESTING
                -- STATUS
            - An instance of the class is actually a child of the class.
            - Example :: instance_tests = Tests_Methods_Accessibility().
            - instance_tests is the child of the class and the class is Tests_Methods_Accessibility.
            - Whatever a class can access the instance of the class can also access it.
            - We can call the class variable from the instancemethod using self,
              Ex: In this class we can call the class variables as follows;
                --- self.CLASS_VARIABLE_TESTING
                --- self.STATUS

        Q: Can I access a Staticmethod inside of the instance method?
        A: Yes
            - How ?
            - An instance of the class is actually a child of the class.
            - Example :: instance_tests = Tests_Methods_Accessibility().
            - instance_tests is the child of the class and the class is Tests_Methods_Accessibility.
            - Whatever a class can access the instance of the class can also access it.
            - We can call the staticmethod from the instancemethod using self,
              Ex: In this class we can call staticmethod: tests_static_method from instancemethod as,
                --- self.tests_static_method()

        Q: Can I access a Staticmethod inside of the Classmethod?
        A: Yes
            - How ?
            - A Staticmethod is at the class level and can be accessed by the class directly.
            - We can call the staticmethod from the classmethod using cls,
                Ex: In this class we can call staticmethod: tests_static_method from classmethod as,
                --- cls.tests_static_method()
    
        Q: Can I access a Classmethod inside of the Staticmethod?
        A: Yes


    '''

    # Define a Simple Instance method.
    def tests_instance_method(self):
        '''
            A Simple instance method.
            The first positional argument self becomes the instance of the class.            
        '''
        # Accessing a class method inside of the instance method.
        print("\nInvoke classmethod - tests_class_method from the instancemethod tests_instance_method\n")
        result = self.tests_class_method()
        print("Result is - {} ".format(result))

        print("\nInvoke Class Variables: CLASS_VARIABLE_TESTING and STATUS from the instancemethod tests_instance_method\n")
        print("Value of Class Variable CLASS_VARIABLE_TESTING is - {} ".format(self.CLASS_VARIABLE_TESTING))
        print("Value of Class Variable STATUS is - {} ".format(self.STATUS))
        print("\n\n")
        print("-"*100)
        print("\n\n")


        print("\nInvoke staticmethod - tests_static_method from the instancemethod tests_instance_method\n")
        result = self.tests_static_method()
        print("Result is - {} ".format(result))

        print("\n\n")
        print("-"*100)
        print("\n\n")

        return "Hey Guys! I am an instancemethod, my name is tests_instance_method"

    # Define a Simple Class method.
    @classmethod
    def tests_class_method(cls):
        '''
            A Simple Class method.
            The first positional argument cls becomes the class.            
        '''
        print("\nInvoke staticmethod - tests_static_method from the classmethod tests_class_method\n")
        result = cls.tests_static_method()
        print("Result is - {} ".format(result))

        print("\n\n")
        print("-"*100)
        print("\n\n")

        return "Hey Guys! I am a Classmethod, my name is tests_class_method"

    # Define a Simple Static method.
    @staticmethod
    def tests_static_method():
        '''
            A Simple Static method.
            In  case of the staticmethod, its not mandate to pass any positional argument,
            just like instance or class methods.
        '''
        return "Hey Guys! I am a Staticmethod, my name is tests_static_method"

                                                
#---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Create an instance
    instance_tests = Tests_Methods_Accessibility()
    # Call the instancemethod
    instance_tests.tests_instance_method()
    # Call the classmethod using class directly - no need for instance
    Tests_Methods_Accessibility.tests_class_method()