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

    Private and Public Variables
    -----------------------------

    The Private variables are defined as starting with "__"
        
        Example :: self.__back_account_name="CONF"
        
            The variable __back_account_name is private and can be accessed inside of the class.
            The variable __back_account_name is private and cannot be accessed outside of the class.

    The Public variables are not defined as starting with "__"
        
        Example :: self.back_account_name="CONF"

            The variable back_account_name is public and can be accessed inside of the class.
            The variable back_account_name is public and can be accessed outside of the class.



    Private and Public Methods
    ---------------------------

    The Private methods are defined as starting with "__"

        Example :: def __reveal_data_confidential

            The method __reveal_data_confidential is private and can be accessed inside of the class.
            The method __reveal_data_confidential is private and cannot be accessed outside of the class.

        Example :: def reveal_data_confidential

            The method reveal_data_confidential is public and can be accessed inside of the class.
            The method reveal_data_confidential is public and can be accessed outside of the class.

    
    Below Class Person has 1 Private methods namely :

        1. __check_qualification
    
        Creating an instance and calling private methods outside of the class will result in AttributeError
        ---------------------------------------------------------------------------------------------------


            # Create an instance of the class..
            instance_person = Person("Sherlock",35,"London","Programmer")
            # Get the details of the Person
            instance_person.about()
            # Check Qualification
            instance_person.__check_qualification()
            """
                It will result in AttriButeError since private methods cannot be called outside of the class.

                Traceback (most recent call last):
                  File "exercise16.py", line 378, in <module>
                    instance_person.__check_qualification()
                AttributeError: 'Person' object has no attribute '__check_qualification'
                
            """    

        Calling private methods inside of the class will not result in AttributeError
        ---------------------------------------------------------------------------------------------------

            Refer method process defined inside of the Person Class.
            It internally invokes __check_qualification method and it works.
            instance_person = Person("Sherlock","Holmes",35,"London","Programmer")
            # Call the Process method
            instance_person.process()
            # Output works
            My name is Sherlock Holmes and I am 35 , I am From London and I am a Programmer

    Below Class Person has 1 Private variable namely :

        1. __fullname

        # Get the full name of the Person from outside of the class
        -----------------------------------------------------------
            # Create an instance of the class..
            instance_person = Person("Sherlock","Holmes",35,"London","Programmer")
            # Get the full name of the Person from outside of the class
            print(instance_person.__fullname)

            Traceback (most recent call last):
              File "exercise16.py", line 417, in <module>
                print(instance_person.__fullname)
              AttributeError: 'Person' object has no attribute '__fullname'

        # Get the full name of the Person from inside of the class
        -----------------------------------------------------------
        Refer method about defined inside of the Person Class.
        Inside of this method variable self.__fullname is accessed and data is available.

        # Create an instance of the class..
        instance_person = Person("Sherlock","Holmes",35,"London","Programmer")
        # Get the details of the Person
        print(instance_person.about())
        # Output comes and it works
        My name is Sherlock Holmes and I am 35 , I am From London and I am a Programmer

    Writing Optimized if-else conditions
    ------------------------------------

    Refer to following methods in the Person Class.

        1. def calculate_bonus

            This method has complex if-else conditions for finding the bonus.

        2. def return_bonus

            This method replaces complex conditions with a dictionary.
    
    
'''

# Define a Person class and perform related operations

class Person:

    def __init__(self,fname,lname,age,location,profession,income,experience):
        """
            This Constructor takes 4 arguments;
            :param fname: First name of the Person
            :param lname: Last name of the Person
            :param age: Age of the Person
            :param location: Location of the Person
            :param profession: Profession of the Person
            :param income: CTC/Month
            :param experience: Years of experience in Tota;

            Note :: 
                1 . The parameters defined inside the __init__ method are accessible only to the
                instance of the class
                2. Pass values for all parameters while creating an instance of the class
                3. The variables thus assigned below are known as *instance variables*
                4. Example of instance variables are shown below;
                    self.fname=fname
                    self.lname=lname
                    self.age=age
                    self.location=location
                    self.profession=profession
                    self.income=income
                    self.experience=experience
                5. The instance variables are accessible only inside the instance methods of the class
        """
        # Assign the parameters to the instance variables
        self.fname=fname
        self.lname=lname
        self.__full_name = self.fname + " " +self.lname
        self.age=age
        self.location=location
        self.profession=profession
        self.qualify_age=20 # We can also hard-code instance variables
        self.income=income
        self.experience=experience

    def calculate_bonus(self):
        '''
            Define a method to calculate the bonus of a person based on;
            1. Years of Experience.
            2. Income
        '''
        # Write multiple conditions.
        if self.income > 100000:
            return 5

        elif self.income > 90000 and self.income < 100000:
            return 5.5

        elif self.income > 80000 and self.income < 90000:
            return 6

        elif self.income > 60000 and self.income < 80000:
            return 6.5

        elif self.income > 40000 and self.income < 60000:
            return 7

        elif self.income > 30000 and self.income < 40000:
            return 7.5

        elif self.income > 10000 and self.income < 30000:
            return 9

        elif self.income > 5000 and self.income < 10000:
            return 10

        else:
            return 12.5

    def return_bonus(self):
        '''
            Define a method to calculate the bonus of a person based on;
            1. Years of Experience.
            2. Income
        '''
        # Write multiple conditions.
        self.bonus_criteria = {self.income > 100000:5,
        self.income > 90000 and self.income < 100000:5.5,
        self.income > 80000 and self.income < 90000:6,self.income > 60000 and self.income < 80000:6.5,
        self.income > 40000 and self.income < 60000:7,self.income > 30000 and self.income < 40000:7.5,
        self.income > 10000 and self.income < 30000:9,self.income > 5000 and self.income < 10000:10}
        # Find and return the Bonus. Only 1 of above condition and become True.
        # If none of the condition is satisfied return default of 12.5
        # This is similar to Switch Case and more optimal compared to method calculate_bonus defined above.
        return self.bonus_criteria.get(True,12.5)


    def __check_qualification(self):
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

            NOTE ::
                The variable self.__full_name is a private variable and accessible inside
                of the class.

        """
        # Display details
        return "My name is {} and I am {} , I am From {} and I am a {} and my * Halloween * bonus is {}%".format(self.__full_name,
            self.age,self.location,self.profession,self.return_bonus())

    def process(self):
        '''
            Processes the records of the person...
        '''
        # Check a condition and process. Print details of the person if they would be qualified.
        return self.about() if bool(self.__check_qualification()) else "Unqualified!!"

# Execute
if __name__ == "__main__":

    # Create an instance of the class..
    instance_person = Person("Sherlock","Holmes",35,"London","Programmer",1000,15)
    # Get the details of the Person
    print(instance_person.about())