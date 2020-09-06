# Introduction to Python language with multiple examples

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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 3 :: Using Variables in Python - We try to delete the variable and access it.

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

def return_mem_location_type_of_variable(variable):
    '''
        Find memory location and type of variable
        :param variable: Variable to be explained.  
        The class of the variable can be found in 2 ways:
            print(variable.__class__)   
            print(type(variable))
        Return the memory location of the variable & the class
        of the variable.
    '''
    # Return the memory location and type of the object.
    return id(variable),variable.__class__

print("\n")
print("Example 4 Output :: ")
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

# Execute the function return_mem_location_type_of_variable
print(return_mem_location_type_of_variable(variable=100000))
print(return_mem_location_type_of_variable(variable=100.100))
final_result = return_mem_location_type_of_variable("Arun Chandramouli")
print(final_result)
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
    
    Q: How many arguments does the function hello_world have?
    A: 1
    
    Q: Q: How many arguments can we pass to the function hello_world?
    A: 1
    
    Q: What does function hello_world return ?
    A: It returns a String. 
    
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
'''

# Print the function object
print("Function object is {} ".format(hello_world))
# Store the execution result of function in a variable..
result = hello_world("Karthik!")
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
print(result)# ?????


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

test_result = hello_world # Store the function object hello_world in variable test_result.
print(test_result("Arun"))
del hello_world #  Delete the function object.
print(test_result("Arun !!"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 9
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''
    Mutables and Immutable Object
    Mutables: 
        - Can be modified after creation.
        - Memory address of the object remains the same after modification.
        - Examples:
            ~ Lists
            ~ Dictionary
            ~ Set
    ImMutables: 
        - Cannot be modified after creation.
        - Only a new object at a different memory location can be created.
        - Memory address of the object is modified.
        - Examples:
            ~ Tuples
            ~ String
'''

# Define a mutable object
test_array = [100,200,300,400,500]
# Print the memory location of test_array
print("Memory location of test_array is - {} ".format(id(test_array)))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 10
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 11
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 12
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 13
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 14
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 15
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 16
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 17
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

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