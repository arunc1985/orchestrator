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

    Mutables: 
        - Once a mutable object is created:

            - Can be modified after creation.
            - Memory address of the object remains the same after modification.
            - Examples:
                ~ Lists
                ~ Dictionary
                ~ Set
        - We can modify/customize a mutable object.
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
  1. Add one more element 
  2. Change the value of an element in a given index
  3. Delete an element
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
      
      final_result_array = func_mutables(input_array)
  3. The contents of original input_array will be different
     from the new array final_result_array
"""

# Define an input array
input_array = [1,2,3,4,5,6]
# Execute the function
final_result_array = func_mutables(input_array)
print("Original Array is - {} ".format(input_array))
print("Final Result is - {} ".format(final_result_array))
print("Memory loc of input array - {} ".format(id(input_array)))
print("Memory loc of new array - {} ".format(id(final_result_array)))

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