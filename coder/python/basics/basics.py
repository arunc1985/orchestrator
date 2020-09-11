# Introduction to Python language with multiple examples
'''
  Git Clone Details:

    git clone https://github.com/arunc1985/orchestrator.git
    git checkout programmer
    cd orchestrator/coder/python/basics

    Run as python basics.py

'''

                                        # Example 1 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 1 :: Using Variables in Python
# In python we dont have to declare the type of variable before assigning it any value.
# But in languages like C, C++ or Java etc.. we need define first then assign value...

var_x = 100 # Integer
var_y = 200 # Integer
x=True # Boolean
y=False # Boolean
a=110.50 # Float
b=-200 # Integer 
c={1:10,2:25,3:30,4:50} # Dictionary
d=[1,2,3,4,5] # Lists/Array
e=(1,2,3,4,5) # Tuple
f= -100.125 # Float

'''
# To find the memory location of each object using id(object) - this will give memory location as integer.
'''

print("\n")
print("Example 1 Output :: ")
print("\n")
print(id(var_x)) # Returns Memory location
print(id(var_y)) # Returns Memory location
print(id(x)) # Returns Memory location
print(id(y)) # Returns Memory location
print(id(a)) # Returns Memory location
print(id(b)) # Returns Memory location
print(id(c)) # Returns Memory location
print(id(d)) # Returns Memory location
print(id(e)) # Returns Memory location

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 2 :: Using Variables in Python

'''
    The below definition means that var_x is a variable and it points/references a memory location
    that has value as 500 ~

    In python when we assign a variable like var_x = 500, Whatever is there to the left side of the
    " = " symbol represents the stack memory and that to the right represents the heap memory.

    Which means , when var_x = 500
    var_x - > Stack Memory
    500 -> Heap Memory

    * Python Stores all the objects in the heap memory only.

    What's stack memory and heap memory ?

    https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html

    # Note: In Python its not needed to pre-define a variable type before assigning values.
    We can dynamically assign values to any variables.

    In python we find the family/type of object using __class__ or type() built-in function.

'''

print("\n")
print("Example 2 Output :: ")
print("\n")


var_x = 500 # Type is integer
print(var_x) # 500
# In python we find the family/type of object using __class__ or type() built-in function.
print(var_x.__class__) # Returns type of object
print(type(var_x)) # Returns type of object

# Same variable can be reassigned to another value.
# Note: In Python its not needed to pre-define a variable type before assigning values.
var_x = "Arun Chandramouli"
print(var_x) # Arun Chandramouli
print(var_x.__class__) # Returns type of object
print(type(var_x)) # Returns type of object



var_x = True
print(var_x) # Arun Chandramouli
print(var_x.__class__) # Returns type of object
print(type(var_x)) # Returns type of object


var_x = 100.150
print(var_x) # Arun Chandramouli
print(var_x.__class__) # Returns type of object
print(type(var_x)) # Returns type of object

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 3 :: Using Variables in Python - We try to delete the variable and access it.


"""
    # All vars in stack memory will point to the objects in the heap.
    #When we assign a variable such as x=100,this var x is from stack and value 100 is from heap memory .
    # Now when i delete the variable x ... it gets dereferenced.
    # Once its deleted- it cant be accessed..all

    # variable some_var is pointing to a memory location that has value as 100.50 ~ As simple as that.
    # This creates a reference to an object in a memory location.

    What happens when we set: 
     some_var = 100.50
      - A Variable named some_var is created in stack memory *
      - A Reference is made from stack memory variable some_var
        to a memory location on the heap that has value as 100.50
      - It looks like this ;
          Stack    -> HEAP
          -----       -----
          some_var -> 100.50

    What happens when the variable is deleted ?

      Before Deletion :
        - It looks like this ;
          Stack    -> HEAP
          -----       -----
          some_var -> 100.50

      After deletion, the reference is removed.
      The variable is removed from the stack memory .

      So, when we do del some_var  :
        - The variable some_var is deleted.
        - The reference it had to that heap memory location is removed.
        - But the original object 100.50 is still heap memory ***
"""

print("\n")
print("Example 3 Output :: ")
print("\n")

some_var = 100.50 # Float variable.
print(some_var)
del some_var # Reference is deleted.
#print(some_var) # Will result in an exception since the variable is deleted.
#NameError: name 'some_var' is not defined -> NameError is a type of exception in Python *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 4 :: Using simple functions in python for getting variable details.

# Write a simple function to find memory location and type of given variable.

'''
    # Simple function without any arguments
    def function_hello():
      return "Hello World!"
    # Get function object
    print(function_hello)
    # We call function using () as function_hello()
    print(function_hello())

    # Simple function with 1 argument...
    def function_hello(name):
      return "Hello World! {} ".format(name)
      
    # Get function object
    print(function_hello)
    # We call function using () as function_hello()
    print(function_hello(name="Python"))
'''

def print_mem_location_type_of_variable(variable):
    '''
        Find memory location and type of variable
        :param variable: Variable to be explained.  
        The class of the variable can be found in 2 ways:
            print(variable.__class__)   
            print(type(variable))
    '''
    print("Memory location of variable {} is {} ".format(variable,id(variable)))
    print("Variable {} belongs to class {} ".format(variable,type(variable)))
    print("\n\n")

print("\n")
print("Example 4 Output Part - 1 :: ")
print("\n")

# Test the function with various objects.
print_mem_location_type_of_variable("Arun")
print("\n")
print_mem_location_type_of_variable("Chandramouli")
print("\n")
print_mem_location_type_of_variable(100)
print("\n")
print_mem_location_type_of_variable(100.100)
print("\n")
print_mem_location_type_of_variable(True)
print("\n")
print_mem_location_type_of_variable([100,200,300,400,500])
print("\n")

print_mem_location_type_of_variable("Binita")
print_mem_location_type_of_variable(True)
print_mem_location_type_of_variable(100.135)
print_mem_location_type_of_variable([10,20,30])
print_mem_location_type_of_variable((1,2,3))
print_mem_location_type_of_variable({1:1,2:2,3:3})
print_mem_location_type_of_variable({1,2,3,4,5})


def return_mem_location_type_of_variable(variable):
    '''
        Find memory location and type of variable
        :param variable: Variable to be explained.  

        The class of the variable can be found in 2 ways:
            print(variable.__class__)   
            print(type(variable))
            variable.__class__ is same as type(variable)
        
        *** 
            NOTE::
                id(object) -> Gives the location of an object in memory.
                type(object) or object.__class__ -> Gives the family/class of object
        ***

        This function is used to return the memory location of the variable & the class
        of the variable.
      
      Execute the function as:
        result = return_mem_location_type_of_variable(variable=100)
      # Unpack the tuple and get the specific values..
      memory_location, class_variable = result

    '''
    # Returns the memory location and type of the object as a tuple.
    return id(variable),variable.__class__

"""
 The result of execution is stored in a variable result.
 The function return_mem_location_type_of_variable returns a tuple.
"""
print("\n")
print("Example 4 Output Part - 2 :: ")
print("\n")


result = return_mem_location_type_of_variable(variable=100)
print("Result of execution is - {} ".format(result))
print("Type of result is - {} ".format(result.__class__))

# Unpack the tuple and get the specific values..
memory_location, class_variable = result
print("Memory location is - {} ".format(memory_location))
print("Class of the variable is - {} ".format(class_variable))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 4 - PART 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''
  Define a function to find the memory location and type of object.
  Return the values as Tuple.
  Execute the function and store the result in a variable.
  Unpack the tuple and print all the values.

  Note :
    Q: What is a tuple?
    A: Comma Seperated values..Ex: (1,2,3,4,5,)

    Q: How do you unpack the tuple?
    A: Based on the number of values we need to unpack.
      Ex: def hello():
            return 1,2,3,4,5
      result = hello()
      # Unpack
      a,b,c,d,e = result # The value of result is (1,2,3,4,5)

    Q: While i do unpacking, Can i do with lesser or greater values?
    A : NO
        Invalid:
        ---------
        Ex: def hello():
              return 1,2,3,4,5
        result = hello()
        # Unpack - ERROR . Since the result has 5 values and we unpack as 4.
        a,b,c,d = result # The value of result is (1,2,3,4,5)

        Invalid:
        ---------
        Ex: def hello():
              return 1,2,3,4,5
        result = hello()
        # Unpack - ERROR . Since the result has 5 values and we unpack as 6.
        a,b,c,d,e,f, = result # The value of result is (1,2,3,4,5)

'''
# Write a simple function to find memory location and type of given variable.
def return_mem_location_type_of_variable(variable):
    '''
        Find memory location and type of variable. This param variable is a position argument .
        In python its mandate to pass value for all the positional arguments, 
        if we dont pass for any of the argument: 
        Then it would result in an Exception
        
        :param variable: Variable to be explained.  
        The class of the variable can be found in 2 ways:
            print(variable.__class__)   
            print(type(variable))
    '''
    # Return the memory location and type of object as a tuple..
    return id(variable),variable.__class__,True

# Execute the function and store the result in a variable...
result = return_mem_location_type_of_variable(variable=100)
print("Original Result : {} ".format(result))


# Tuple unpack to know memory location and type of object...
memory_id,class_of_object,status = result
print("\n")
print("Result after tuple unpack...")
print("\n")
print("Memory Location is - {} ".format(memory_id))
print("Type of Object is - {} ".format(class_of_object))
print("Status is = {} ".format(status))
print("\n")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 5
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 5 :: Using simple functions in python for getting variable details.
# In Python we can store the function is a variable.

# Write a simple function to find memory location and type of given variable.
def return_mem_location_type_of_variable(variable):
    '''
        Find memory location and type of variable
        :param variable: Variable to be explained.  
        The class of the variable can be found in 2 ways:
            print(variable.__class__)   
            print(type(variable))
    '''
    return id(variable),variable.__class__

print("\n")
print("Example 5 Output :: ")
print("\n")

# Test the function with various objects.
result = return_mem_location_type_of_variable("Arun")
print(result)
result = return_mem_location_type_of_variable(100)
print(result)
result = return_mem_location_type_of_variable(100.50)
print(result)

result = return_mem_location_type_of_variable(True)
print(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 6
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 6 :: Using simple functions in python for printing hello world
# In Python we can store the function is a variable. 
# Even if the function is deleted, the variable will still work and produce results.


# Write a simple function to print hello world with a name.
def hello_world(name):
    '''
        :param name: Name to the printed.   
        return Hello World with name..
    '''
    return "Hello World ! {} ".format(name)

'''
  Points :
    
    Q: What's the name of the function ?
    A: hello_world

    Q: What is the name argument?
    A: Argument name is a positional argument. There are various types of arguments in python.
       - For positional arguments if we dont pass any value it will result in an exception.
       - We must values to exact number of positional args, passing lesser or more will still result
         in an exception.
       - For Example:
          - To run function hello_world, I call as : hello_world("Arun")# It will take only 1 Argument.
          - Giving lesser or more arguments will raise an exception.
          - hello_world() # No args - hence error.
          - hello_world("Arun","Kumar")# 2 args - hence error.
    
    Q: How many arguments does the function hello_world have?
    A: 1
    
    Q: How many arguments can we pass to the function hello_world?
    A: 1

    Q: How to execute the function hello_world ?
    A: In python functions are executed by calling them using braces... ()
        - Function hello_world must be called using ()
        - Inside the () we must pass all the required arguments.
        - Ex: hello_world("Arun")
    
    Q: What does function hello_world return ?
    A: It returns a String Hello World ! Arun... Ex: If name is Arun.
    
    Q: What String it returns?
    A: "Hello World ! {} ".format(name).Where name is the argument that I pass.
    
    Q: What is the function object here?
    A: Function object is <hello_world at some mem_location>. It is an object
    that is created by python at run time, when i run the module the name hello_world gets transformed as an object and that object is
    safely stored at some memory location.
    
    Q: Do I execute the function name or function object ?
    A: I execute the function object by passing all the required arguments.
       Python transforms the function name into object and I am executing the
       object in the heap memory *  

    Q: What happens internally when this file is run ?
    A: Python runs the module line by line. 
       At first it sees the function definition : def hello_world(name)
       It sees the def keyword and identifies the function.
       It sees the function name as hello_world that has an argument. 
       It creates a function object hello_world that takes 1 argument
       It thus creates an object and stores in the heap memory. 
       The object once stored in the heap memory is available for execution. 
       So the function name gets transformed as function object at run-time.

    Q: What happens if I execute function hello_world with more than 1 argument ?
        - print(hello_world("Arun","Binita")) # 2 Args
    A: It will result in an exception - TypeError
        TypeError: hello_world() takes 1 positional argument but 2 were given

    Q: What happens if I execute function hello_world with no argument ?
        - print(hello_world() # 0 Args
    A: It will result in an exception - TypeError
        TypeError: hello_world() missing 1 required positional argument: 'name'

    Q: Can I access the result of the function once I delete the function object?
    A: Yes

      Explanation
      ------------

      Python creates the function object hello_world and places it in some location X in memory ....

      This function hello_world can take 1 argument .
      This function hello_world will return a string ..
      
      Python allocates memory for various objects based on their type...which means allocation differs 
      between string, int, float, boolean, function etc...
      Now as we see the output of function hello_world is of
      String type....

      This statement:
        result = hello_world(name="Maria")
        ------------------------------------

       means result will point to a memory location that has the 
       execution result of the function .
       Which means it will hold the result of hello_world(name="Maria")

       So the function object hello_world is at some memory location X. . it is an object...

       The result obtained by execution of the function hello_world(name="Maria") is a String ...

       Hence the result will be stored in a nearby memory location...such as Y , Z etc...

       The result will not be stored in the same place.
       If we would store in the same place, the original function object would not exist..

       Is simple terms we need to remember whenever we execute the function - 
       it will never get stored in the memory location of the function object...

       So when I run result = hello_world(name="Maria") it stores result in some memory location .

       If I delete function object hello_world :
        - del hello_world

       The result was stored in a different memory location hence it will be still accessible ..
       print(result) # Will print the output ...

'''


'''
  Lets say func object hello_world is at loc: 100
  the result of function execution is at loc: 200
  When we delete the func object, the result will not get affected.
  The result will be safe still in the same heap memory ...
  and the variable result is pointing that location in heap..
'''


# Print the function object
print("Function object is {} ".format(hello_world))
# Store the execution result of function in a variable..
result = hello_world("Maria!")
# Print the result of the function 
print("Execution result is - {} ".format(result))
# Print the memory location of the execution result 
print("Memory location of the execution result is - {}".format(id(result)))
# Print the memory location of the function object
print("Memory location of the function object is - {}".format(id(hello_world)))
# Note: The memory location of function object is diff from that of execution result


# Delete the function object - hello_world and the result will still print as Arun Chandramouli *
# It prints even after deletion of function object.
# Bcoz...Function object and result are stored in diff memory location.


'''
Note: The memory location of function object is diff from that of execution result
Ex: 
  Function object hello_world is at memory location: 10000XTY
  Result of execution is at memory location: 50000XAB
  If I delete the function object hello_world at memory location: 10000XTY
  It will not affect the result of execution which is stored at: 50000XAB
  That is because they are in different memory location .
'''
# Delete the function object
del hello_world
print("\n Result after deletion of function object ... ")
# It will still print the result...
print(result)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                      
                                        # Example 7
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 7 :: Define variables with values, find the reference count of the variables.

'''
    Q: What is reference count ?
    A: The Reference Count denotes the n.o. variables pointing at a given object.

    Q: How do I get the reference count of an object?
    A: Reference count of an object can be found out by using sys module.
        - import sys
        - sys.getrefcount(<object>)
        - Example : 
            - x = 1
            - y = 1

        print(sys.getrefcount(1))
        
        - The variable names are x and y.
        - x has a value of 1 i.e. it refers to a memory location that has value as 1
        - y has a value of 1 i.e. it refers to a memory location that has value as 1
        - Here there are 2 variables pointing to a memory location that has value as 1.
        - So the result with be 3.

    Q: In previous step there are only 2 variables pointing to a memory location that has value as 1.
       Why the reference count of 1 is 3 ?
    A: By default python adds a reference count to an object in memory.

    Open python shell and try this.

        arunkuch@ARUNKUCH-9NCZB MINGW64 ~/Documents/Programs/orchestrator/coder/python (programmer)
        $ python
        Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import sys
        >>> x = 100000
        >>> x1 = 100000
        >>> print(sys.getrefcount(100000))
        3

    Q: Will the reference count decrease if I delete a variable?
    A: Yes

       Refer to the example below,
       Open python shell and try this.

       x = 100
       y = 100
       import sys
       print("Reference Count of int object 100 before deleting variables x & y is {} ".format(sys.getrefcount(100)))
       del x
       del y
       print("Reference Count of int object 100 after deleting variables x & y is {} ".format(sys.getrefcount(100)))
        -- After deleting the variables x & y , the reference count of int object has thus reduced by 2.
       
       Output from Python Shell ::
       -------------------------

        arunkuch@ARUNKUCH-9NCZB MINGW64 ~/Documents/Programs/orchestrator/coder/python/basics (programmer)
        $ python
        Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> x = 10000.250
        >>> y = 10000.250
        >>> import sys
        >>> print("Reference Count of int object 100 before deleting variables x & y is {} ".format(sys.getrefcount(10000.250)))
        Reference Count of int object 100 before deleting variables x & y is 6
        >>> del x
        >>> del y
        >>> print("Reference Count of int object 100 after deleting variables x & y is {} ".format(sys.getrefcount(10000.250)))
        Reference Count of int object 100 after deleting variables x & y is 4
        -- After deleting the variables x & y , the reference count of int object has thus reduced by 2.

'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Import the module sys
import sys
x = 100.125
y = 100.125

print("\n")
print("Example 7 Output :: ")
print("\n")
# Print the reference count of an object before deleting references.
print(sys.getrefcount(100.125))
del x,y
# Print the reference count of an object after deleting references.
# After deleting the variables x & y , the reference count of int object has thus reduced by 2.
print(sys.getrefcount(100.125))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 8
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 8 :: Using simple functions in python to explain del keyword and reference count .
# In Python we can store the function is a variable. 
# Even if the function is deleted, the variable will still work and produce results.

'''
    1. Define a function as def hello_world(name) -> A function that takes 1 Argument .

        def hello_world(name):
            return "Hello World ! {} ".format(name)

    2. Assign the function object to a variable
        - Ex: execution_func_var = hello_world
        - The variable execution_func_var is a reference to object hello_world
        - As stated previously, the variable execution_func_var is at the stack memory
          and the object hello_world is at heap memory
        - So, variable execution_func_var now references function object hello_world
        - Find out the count of refrences for object hello_world using sys module.
            - import sys
            - print(sys.getrefcount(hello_world))
    3. Execute the function using the variable execution_func_var :
        - execution_func_var("Arun") # Output is Hello World ! Arun
    4. Delete the function object
        - del hello_world
    5. Now again execute the function using the variable execution_func_var :
        - execution_func_var("Arun") # Output is Hello World ! Arun
    6. Eventhough the function object hello_world is deleted ,
        - The variable execution_func_var can be still invoked and results obtained.
        - This is because once we run statement del hello_world
            - The object would thus show as deleted.
            - But it wont be immediately garbage collected.
            - Python does garbage collection based on reference count.
            - As seen in previous step, we obtained reference count of object hello_world as,
                - import sys
                - print(sys.getrefcount(hello_world))
            - The object will be garbage collected and deleted from memory only if the
              reference count will be 0.
            - Until it's collected it would be hanging around in memory.

'''

# Write a simple function to print hello world.
def hello_world(name):
    '''
        Find memory location and type of variable
        :param name: Name to the printed.   
        The class of the variable can be found in 2 ways:
            print(variable.__class__)   
            print(type(variable))
    '''
    return "Hello World ! {} ".format(name)

print("\n")
print("Example 8 Output :: ")
print("\n")

# Store the function object in a variable and delete the original function object.
# The variable can still give results...

"""
 Assigning the function object hello_world to a variable .
 The variable test_result is from the stack memory .
 The function object hello_world is from the heap memory .
 Once we assing like this:
  test_result = hello_world 
 The variable test_result would now point to a memory location that
 has the object hello_world .
 It is just referencing the function hello_world  

 So now test_result is also a function object and it can be
 executed the same way as hello_world

 Example:
 --------
  print(hello_world("Arun"))
  print(test_result("Arun!!"))
  
"""
test_result = hello_world 

# Now test_result also became a function object...
print(hello_world)
print(test_result)
# Execute the function
print(hello_world("Arun"))
print(test_result("Arun!!"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 9
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''
    Mutables and Immutable Objects
    
    At a higher level we can classify the objects as mutable & im-mutable.
    "Arun", 100, False,{},[],()

    Mutables: 
        - Once a mutable object is created:

            - Can be modified after creation.
            - Memory address of the object remains the same after modification.
            - Examples:
                ~ Lists - append, insert, extend etc..
                ~ Dictionary - update, set...
                ~ Set - add...
        - We can modify/customize a mutable object.
        - After modification the memory location will remain the same.
        
    ImMutables: 
        - Once an im-mutable object is created:

            - Cannot be modified after creation.
            - Only a new object at a different memory location can be created.
            - Memory address of the object is modified.
            - Examples:
                ~ Tuples
                ~ String
        - We cannot modify/customize a mutable object.
'''

# Define a mutable object
test_array = [100,200,300,400,500]
print("Original Array is - {} ".format(test_array))
print("Memory location of original array is - {} ".format(id(test_array)))
print("\n")

"""
  ~ I want to modify the contents inside test_array
      1. Add one more element - append or extend
      2. Change the value of an element in a given index - insert
      3. Delete an element - remove or pop
"""

# Add 1 or more elements using append function
test_array.append(1000)
print("Add 1 or more elements using append function")
print("New Array is - {} ".format(test_array))
print("Memory location after append is - {} ".format(id(test_array)))

"""
  Q: Memory location of the object test_array after using append/extend/remove or any operation on the list to
  add a new value/remove a value is same as the original memory location. Why?

  A: Python internally stores the list test_array as a mutable object and lists have methods to modify it. 
  To find all the methods applicable for lists...run ... dir(test_array)

  So when the test_array is modified python refers to the same memory location and adds a 
  new value to the existing array.
  This is something similar to pass by reference programming paradigm...
"""
print("\n")
# Add 1 or more elements using extend function
test_array.extend([1500,2000,2500,3000])
print("Add 1 or more elements using extend function")
print("New Array is - {} ".format(test_array))
print("Memory location after extend is - {} ".format(id(test_array)))
print("\n")

# Delete an element from a list
test_array.remove(100)
print("Remove an item using remove function")
print("New Array is - {} ".format(test_array))
print("Memory location after remove is - {} ".format(id(test_array)))
print("\n")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 10
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Simple function for arrays
def func_array(original_array):
  """
    Take an array as an input and multiply each number by 2.
    Define an empty array - result_array
    Add the multipled number to the new array result_array.
    Return the new array - result_array

    In this program there are 2 different arrays
      1. original_array -> Passed by the User
      2. result_array -> Contains final result
    
    The memory location of the original_array will be different from
    that the new array result_array since they are 2 different lists
    entirely.
  """
  # New Array to store the result...
  result_array = []
  # Iterate the original_array and multiply each number by 2...
  for each_val in original_array:
    # multiply by 2 and append to new array
    result_array.append(each_val*2)
  # Return the new modified array
  return result_array


"""
 Execution :
  1. Define an input array
      input_array = [1,2,3,4,5,6]
  2. Execute the function and store the result in a variable      
     final_result_array .
      
      final_result_array = func_array(input_array)
  3. The contents of original input_array will be different
     from the new array final_result_array
"""

# Define an input array
input_array = [1,2,3,4,5,6]
# Execute the function
final_result_array = func_array(input_array)
print("Original Array is - {} ".format(input_array))
print("Final Result is - {} ".format(final_result_array))
print("Memory loc of input array - {} ".format(id(input_array)))
print("Memory loc of new array - {} ".format(id(final_result_array)))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 11
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''
  Define a simple function for manipulating the Arrays.
  Pass an empty list as a default argument and manipulate the empty list in the array.
  Example:
    def func_array(original_array,result_array = [])

  # Define an input array
  input_array = [1,2,3,4,5,6]
  
  # Execute the function
  final_result_array = func_array(input_array)

'''


# Simple function for arrays
def func_array(original_array,result_array = []):
  """
    
    Aim:
      Take an array as an input and multiply each number by 2,
      add to new array and return the new array.
    
    Steps:

      Iterate the original_array, multiply each number by 2. 

      Add each of the multipled number to the new array result_array.
      Return the new array - result_array

    In this program there are 2 different arrays
      1. original_array -> Passed by the User
      2. result_array -> Contains final result
    
    Explanation of Arguments ::

     1. original_array: Positional Argument and value must be passed. 
          --  If the value is not passed it will raise an error.

     2. result_array: It is a default argument. This takes a default value at function
        creation time. In this case the default value will be an empty list - []
        
        If we pass any value to the default argument it will still take the new value.

        For ex:
          The above function can be executed either with existing default value or passing new value.
          Let's say original_array = [1,2,3,4,5]

          Case 1 :: Default argument is not altered, it remains as []

            result = func_array(original_array,result_array = [])
            
            When its not altered, the final array - result_array will contain the product of numbers
            added to the result_array

            i.e. result_array.append(each_val*2)

            If i would pass the original_array as [1,2,3,4,5,6]
            The output would be [2,4,6,8,10,12]
          
          Case 2 :: Default argument is altered, it is passed as [100,200]

            result = func_array(original_array,result_array = [100,200])

            When it is altered, the final array - result_array will contain the product of numbers
            added to the result_array. And it will also take the values that I passed while execution.

            i.e. result_array.append(each_val*2)

            While executing I modified the default argument and passed with values [100,200]

            Like this : func_array(original_array,result_array = [100,200])

            So which means that the final array - result_array will contain the product of the numbers +
            the values i Pass - [100,200]

            If i would pass the original_array as [1,2,3,4,5,6]
            The output would be [100,200,2,4,6,8,10,12]
            IT contains two more values 100,200 since while executing the function i had passed
            the result_array as result_array=[100,200]
    
    Memory Location ::
      
      The memory location of the original_array will be different from that the new array result_array 
      since they are 2 different lists entirely.
  """

  # Iterate the original_array and multiply each number by 2...
  for each_val in original_array:
    # multiply by 2 and append to new array
    result_array.append(each_val*2)
  # Return the new modified array
  return result_array


# Define an input array
input_array = [1,2,3,4,5,6]
# Execute the function
final_result_array = func_array(input_array)
print("Original Array is - {} ".format(input_array))
# The new array will now have values as [2, 4, 6, 8, 10, 12]
print("Final Result is - {} ".format(final_result_array))


# Define an input array
input_array = [1,2,3,4,5,6]


# Run the function with new values for result_array
# Execute the function
# The new array will now have values as [100, 200, 2, 4, 6, 8, 10, 12]
final_result_array = func_array(input_array,result_array=[100,200])
print("Original Array is - {} ".format(input_array))
print("Final Result is - {} ".format(final_result_array))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 12
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a dictionary and iterate it to print the values.

'''
 Q: Is dict mutable or im-mutable?
 A: Its mutable, do dir({}) to know available options to modify a dict after creation.
'''

# Define a simple dictionary..
empty_dict = {} # This an empty dictionary.
# Define dict with value.
simple_dict = {1:1,2:4,3:9,4:16} # Dict with values.
# Iterate on the dict and get all the values. To iterate use the .items() method for the dict.

'''
 Q: What is {}.items() mean ?
 A: Its a method to get the data from the dict.

 Q: How does dict store the data?
 A: It stores in key:value pair. Ex: simple_dict = {1:1,2:4,3:9,4:16} # Dict with values.

 Q: Can there be multiple keys with same name?
 A: No - keys cannot be repeated. If you define multiple keys then values will get updated.
  Ex:
    simple_dict = {1:1,2:4,3:9,4:16,2:20} # Dict with values.
    Now Python will not take 2:4, but it will take 2:20 since key 2 is getting repeated.
    It will take the latest occurrence of the key.
'''
print("\n Example 12 output  :: \n")

# Iterate on the dict.
for _key,_value in simple_dict.items():
  print("Key is - {} and Value is - {}".format(_key,_value))

# ReDefine dict with value.
# The Keys cannot be repeated. If you define multiple keys the latest values will get updated.
new_simple_dict = {1:1,2:4,3:9,4:16,2:20} # Dict with values.

print("\n Print new dictionary \n ")
# Iterate on the dict.
for _key,_value in new_simple_dict.items():
  print("Key is - {} and Value is - {}".format(_key,_value))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 13
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a function to handle the dictionary operations.
# Use simple if-else condition...

print("\n Example 13 output  :: \n")

def dict_print_values(int_var,dictionary):
  '''
    :param int_var: An integer
    :param dictionary is a positional arg of type {}
    Print the key-value pairs
  '''
  # Iterate on the dict & print. Apply an if-condition and filter the data.
  # Filter and print only values that are divisible by int_var
  for _key,_value in dictionary.items():
    # Check if the Value - _value is divisible by int_var
    # if _value%int_var == 0 : Print.. Ex: 10//5==0 has 0 as Reminder..
    if _value%int_var == 0 :
      print("Key is - {} and Value is - {} - *Success* ".format(_key,_value))
    else :
      print("Key is - {} and Value is - {} - not divisible by {}".format(_key,_value,int_var))

# Call the function and print the data
dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50})

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 14
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Define a function to handle the dictionary operations.
# Use simple if-else condition...if the condition satisfies - add data to new dictionary.

print("\n Example 14 output  :: \n")

def dict_print_values(int_var,dictionary):
  '''
    :param int_var: An integer
    :param dictionary is a positional arg of type {}
    Print the key-value pairs
  '''
  # Define an Empty dictionary inside the function. Add key:value if the condition satisfies...
  result_dict = {}
  # Iterate on the dict & print. Apply an if-condition and filter the data.
  # Filter and print only values that are divisible by int_var
  for _key,_value in dictionary.items():
    # Check if the Value - _value is divisible by int_var
    # if _value%int_var == 0 : Print.. Ex: 10//5==0 has 0 as Reminder..
    if _value%int_var == 0 :
      # Add Value to the dictionary only if the condition is satisfied...
      '''
        Adding key:value pair :
          result_dict[_key] = _value
          result_dict is the dictionary
          _key is the current key in the iteration.
          _value is the current value in the iteration.
          When we write result_dict[_key] = _value
            - The key _key gets mapped to value _value
          For example if dictionary is {1:1,2:20,3:9,4:16,5:50}
          When we iterate we get key:value pair as follows;
            1:1
            2:20
            3:9
            4:16
            5:50
          Which means :
            result_dict[1] = 1
            result_dict[2] = 20
            result_dict[3] = 9
            result_dict[4] = 16
            result_dict[5] = 50

      Finally return the new dictionary result_dict
      '''
      result_dict[_key]=_value
  # Return the new dict using return keyword
  return result_dict

# Call the function and print the data
result = dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50})
print("New & modified dictionary = {} ".format(result))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 15
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a function to handle the dictionary operations.
# Use simple if-else condition with AND...if the condition satisfies - add data to new dictionary.

print("\n Example 15 output  :: \n")

def dict_print_values(int_var,dictionary):
  '''
    :param int_var: An integer
    :param dictionary is a positional arg of type {}
    Print the key-value pairs
  '''
  # Define an Empty dictionary inside the function. Add key:value if the condition satisfies...
  result_dict = {}
  # Iterate on the dict & print. Apply an if-condition and filter the data.
  # Filter and print only values that are divisible by int_var
  for _key,_value in dictionary.items():
    # Check if the Value - _value is divisible by int_var
    # If both _key and _value are divisible by int_var - add to result_dict.
    if _value%int_var == 0 and _key%int_var == 0:
      # Add Value to the dictionary only if the condition is satisfied...
      '''
        Adding key:value pair :
          result_dict[_key] = _value
          result_dict is the dictionary
          _key is the current key in the iteration.
          _value is the current value in the iteration.
          When we write result_dict[_key] = _value
            - The key _key gets mapped to value _value
          For example if dictionary is {1:1,2:20,3:9,4:16,5:50}
          When we iterate we get key:value pair as follows;
            1:1
            2:20
            3:9
            4:16
            5:50
          Which means :
            result_dict[1] = 1
            result_dict[2] = 20
            result_dict[3] = 9
            result_dict[4] = 16
            result_dict[5] = 50

      Finally return the new dictionary result_dict
      '''
      result_dict[_key]=_value
  # Return the new dict using return keyword
  return result_dict

# Call the function and print the data
result = dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50})
print("New & modified dictionary = {} ".format(result))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 16
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a function to handle the dictionary operations.
# Use simple if-else condition with AND...if the condition satisfies - add data to new dictionary.

print("\n Example 16 output  :: \n")

# During function creation time - the argument result_dict = {} will be stored as empty dict in memory.
def dict_print_values(int_var,dictionary,result_dict={}):
  '''
    :param int_var: An integer
    :param dictionary is a positional arg of type {}
    :param result_dict: Its of type {} and it's a default argument.

    Q: What's a default argument?
    A: In python we have multiple argument types such as ;
      - Positional Args
      - Tuple Args
      - Keyword Args
      - Default Args
      
      So in case of default args:
        - The value is available by default during function creation time.Ex: result_dict = {} .
        - Python will not raise an exception - if the value is not passed for default arg during
          function execution.
          For ex: This function can be executed as result = dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50})
          It will not raise even if we dont pass value for result_dict dictionary.

          But if you pass values to default arg during function execution, it will get overwritten.
          For ex: dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50},result_dict={100:1000})
          The result of the function will contain also the value you pass.
            CASE 1 ::
              - Run as dict_print_values(int_var=10,dictionary={1:1,20:40,3:9,4:16,2:20,5:50})
                You would get {20:40}
            CASE 2 ::
              - Run as dict_print_values(int_var=10,dictionary={1:1,20:40,3:9,4:16,2:20,5:50},result_dict={100:1000})
                You would get {100:1000,20:40}
                The result_dict is actually a default argument which got initialized at function creation time.
                But while executing function as above in CASE 2, we are reinitializing it as {100:1000}
                So the final result will also contain {100:1000}
  '''
  # Iterate on the dict & print. Apply an if-condition and filter the data.
  # Filter and print only values that are divisible by int_var
  for _key,_value in dictionary.items():
    # Check if the Value - _value is divisible by int_var
    # If both _key and _value are divisible by int_var - add to result_dict.
    if _value%int_var == 0 and _key%int_var == 0:
      # Add Value to the dictionary only if the condition is satisfied...
      '''
        Adding key:value pair :
          result_dict[_key] = _value
          result_dict is the dictionary
          _key is the current key in the iteration.
          _value is the current value in the iteration.
          When we write result_dict[_key] = _value
            - The key _key gets mapped to value _value
          For example if dictionary is {1:1,2:20,3:9,4:16,5:50}
          When we iterate we get key:value pair as follows;
            1:1
            2:20
            3:9
            4:16
            5:50
          Which means :
            result_dict[1] = 1
            result_dict[2] = 20
            result_dict[3] = 9
            result_dict[4] = 16
            result_dict[5] = 50

      Finally return the new dictionary result_dict
      '''
      result_dict[_key]=_value
  # Return the new dict using return keyword
  return result_dict

# CASE 1 :: Dont pass values for result_dict default argument .
# Call the function and print the data without passing values for result_dict
print("Call the function and print the data without passing values for result_dict default argument.")
result = dict_print_values(int_var=10,dictionary={1:1,20:40,3:9,4:16,2:20,5:50})
print("New & modified dictionary = {} ".format(result))

# CASE 2 :: Pass values for result_dict default argument .
# Call the function and print the data by passing values for result_dict
print("Call the function and print the data by passing values for result_dict default argument.")
# Reinitialize the argument result_dict as {100:1000}
result = dict_print_values(int_var=10,dictionary={1:1,20:40,3:9,4:16,2:20,5:50},result_dict={100:1000})
print("New & modified dictionary = {} ".format(result))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 17
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a function to handle the dictionary operations.
# Use simple if-else condition with AND...if the condition satisfies - add data to new dictionary.

print("\n Example 17 output  :: \n")

# During function creation time - the argument result_dict = {} will be stored as empty dict in memory.
def dict_print_values(int_var,dictionary,result_dict={}):
  '''
    :param int_var: An integer
    :param dictionary is a positional arg of type {}
    :param result_dict: Its of type {} and it's a default argument.

    Q: What's a default argument?
    A: In python we have multiple argument types such as ;
      - Positional Args
      - Tuple Args
      - Keyword Args
      - Default Args
      
      So in case of default args:
        - The value is available by default during function creation time.Ex: result_dict = {} .
        - Python will not raise an exception - if the value is not passed for default arg during
          function execution.
          For ex: This function can be executed as result = dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50})
          It will not raise even if we dont pass value for result_dict dictionary.

          But if you pass values to default arg during function execution, it will get overwritten.
          For ex: dict_print_values(int_var=10,dictionary={1:1,2:4,3:9,4:16,2:20,5:50},result_dict={100:1000})
          The result of the function will contain also the value you pass.
            CASE 1 ::
              - Run as dict_print_values(int_var=10,dictionary={1:1,20:40,3:9,4:16,2:20,5:50})
                You would get {20:40}
            CASE 2 ::
              - Run as dict_print_values(int_var=10,dictionary={1:1,20:40,3:9,4:16,2:20,5:50},result_dict={100:1000})
                You would get {100:1000,20:40}
                The result_dict is actually a default argument which got initialized at function creation time.
                But while executing function as above in CASE 2, we are reinitializing it as {100:1000}
                So the final result will also contain {100:1000}
  '''
  # Iterate on the dict & print. Apply an if-condition and filter the data.
  # Filter and print only values that are divisible by int_var
  for _key,_value in dictionary.items():
    # Check if the Value - _value is divisible by int_var
    # If both _key and _value are divisible by int_var - add to result_dict.
    if _value%int_var == 0 and _key%int_var == 0:
      # Add Value to the dictionary only if the condition is satisfied...
      '''
        Adding key:value pair :
          result_dict[_key] = _value
          result_dict is the dictionary
          _key is the current key in the iteration.
          _value is the current value in the iteration.
          When we write result_dict[_key] = _value
            - The key _key gets mapped to value _value
          For example if dictionary is {1:1,2:20,3:9,4:16,5:50}
          When we iterate we get key:value pair as follows;
            1:1
            2:20
            3:9
            4:16
            5:50
          Which means :
            result_dict[1] = 1
            result_dict[2] = 20
            result_dict[3] = 9
            result_dict[4] = 16
            result_dict[5] = 50

      Finally return the new dictionary result_dict
      '''
      result_dict[_key]=_value
  # Return the new dict using return keyword
  return result_dict

# Define the result dict as result_dict = {1000:2000}
result_dict = {1000:2000}

# STEP 1 ::
# Call the function and print the data by passing values for result_dict
print("Call the function and print the data without passing values for result_dict default argument.")
result = dict_print_values(int_var=10,dictionary={1:1,20:40,30:90,4:16,2:20,5:50},result_dict=result_dict)
print("New & modified dictionary = {} ".format(result))
'''
  # After execution of STEP 1 in above function result_dict is as follows;
  # {1000: 2000, 20: 40, 30: 90}
'''
# STEP 2 ::
# Call the function and print the data by passing values for result_dict
print("Call the function and print the data by passing values for result_dict default argument.")
# Reinitialize the argument result_dict as {100:1000}
result = dict_print_values(int_var=5,dictionary={1:1,200:400,3:90,4:160,2000:2000,15:500},result_dict=result_dict)
print("New & modified dictionary = {} ".format(result))

'''
  # After execution of STEP 2 in above function result_dict is as follows;
  # {1000: 2000, 20: 40, 30: 90, 200: 400, 2000: 2000, 15: 500}.
  Q: So as you see clearly the execution result of STEP 2 also contains execution result of STEP 1 ?
  A: The variable result_dict is a dictionary and a mutable data type.
      A mutable data-type is ;
        - It can be modified after creation.
        - Even after modification, the memory location remains the same.
      So for result_dict lets say it was in memory location X100 during creation.
      Now after STEP 1 it got modified and would still remain in memory location X100.
      So later when we use result_dict in STEP 2, it would still refer to same memory location X100
      and it gets updated again for 2nd time.

      * Hence we find that the final result of STEP 2 contains the result from STEP 1 also.
      So the final result of STEP 2 is result of STEP 1 + STEP 2, I mean the dictionary
      in the same memory location has been officially modified twice * 

'''


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 18
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 19
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 20
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 