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
    instance_employee = Employee()

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
            Display details about an Employee
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
