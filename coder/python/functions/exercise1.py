'''
    Python functions are re-usable piece of code that can have multiple or no arguments.
    Basically the function can be classified as follows;
    1. Function with Arguments
    2. Function without arguments
    
    Example of Function without Arguments
    - - - - - - - - - - - - - - - - - - - 
    def func_tests():
        return True

    Example of Function with Arguments
    - - - - - - - - - - - - - - - - - -
    def func_tests(x,y):
        return x*y

    Also a function can be of normal type or nested types.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        1. Normal Function : 
        
        This type of function is simple and returns at 1 level, it doesn't have nesting.
        It will be executed directly and results will be returned

        Example of a normal Function
        - - - - - - - - - - - - - - - 
        def func_tests():
            return True

        2. Nested Function : 

        This type of function is complex and returns after multiple calls.
        It will be executed at nested level and results will be returned.
        The nested functions are also called as ** Closures ** .

        Example of a nested Function
        - - - - - - - - - - - - - - - 
        def func_tests_nested(x,y):
            
            def func_tests_level1():
                # Arguments from outer function func_tests_nested is passed inside, executed, results returned...
                return x*y
             # Inner function is executed and returned, it will be called and executed by outer function func_tests_nested ...
            return func_tests_level1()

        It's also possible to have a class embedded inside of a function
        def func_tests_nested(x,y):
            class Alpha:
                def __init__(self):
                    self.x,self.y = x,y

                def methodA(self):
                    return True

                def methodB(self):
                    return True
            return Alpha(x,y).methodB()

    By default None gets returned, if a function doesn't return anything .


    How Functions are created by Python Interpreter ?
    -------------------------------------------------


    # Write a simple function to print hello world with a name.
    def hello_world(name):
        """
            :param name: Name to the printed.   
            return Hello World with name..
        """
        return "Hello World ! {} ".format(name)

        """
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
        """

'''

                                        # Example 1 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''
    Define a simple function that doesnt take any arguments.
    Example: def func_tests

    1. func_tests is the name of the function.
    2. This function def func_tests doesn't take any arguments.
    3. At run time python interpreter converts this function name func_tests
       as function object <func_tests> without any arguments. The objects are stored in the heap memory.
    4. To execute the below function call as follows;

        result = func_tests()
        print(result)
        
        - Here func_tests in the function object.
        - Here result is a variable that stores the execution of function func_tests()
        - The variable result points to a memory location that has the execution result of func_tests()
        - The variable result is from the stack memory and the function object is from the heap memory.
        - In general the variables are in the stack memory and the real object are in heap memory.
        - To know more about stack and heap memory please refer 
            --- https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html

'''
#Function without Arguments
def func_tests():
    '''
        On execution just return True
            result = func_tests()
            print(result) # Output is True
    '''
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Function with Arguments
def func_tests(x,y):
    '''
        On execution just return True
            result = func_tests(10,100)
            print(result) # Output is 1000
    '''
    return x*y

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Function with any n.o. Arguments
def func_tests_args(*args):
    '''
        Example: Execute as func_tests_args(10,20,25,30)
        func_tests_args()
    '''
    x=0
    for i in args:
        x+=i
    return x

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        
                                        # Example 4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Function with Keyword Arguments
def func_tests_kwargs(**kwargs):
    '''
        Example: Execute as func_tests_kwargs(x=10,y=20,z=30)
    '''
    for key,value in kwargs.items():
        print("Key = {} and Value = {} ".format(key,value))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 5
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Nested function
def func_tests_nested(x,y):
    '''
        Example: Execute as func_tests_nested(10,20)
    '''
    def func_tests_level1():
        # Arguments from outer function func_tests_nested is passed inside, executed, results returned...
        return x*y
     # Inner function is returned, it will be called and executed by outer function func_tests_nested ...
    return func_tests_level1()*2 # Result is further multiplied by 2 and returned...

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 6
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Write a function and pass many arguments
def print_name(*names):
  '''
    Print the name and location
    *names is known as tuple arguments in python
    What are tuple args?
    It means args that are seperated by a "," .
    You can pass any n.o. arguments to the function
    Tuple args are diff from positional args.
    If you dont pass any vals to these args, it will not
    raise any error...  
  '''
  for each_name in names:
    print("My name is {} ".format(each_name))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
