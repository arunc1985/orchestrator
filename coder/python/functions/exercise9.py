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
    
    ** Time Profiling **

        In this section we will see in-detail about time consumed by python programs in case
        of huge and expensive operations using built-in time module.
'''

# Import built-in modules
import time

                                        # Example 1 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a decorator to find the time taken for executing a block of code.


# Decorator to execute a function and return the result...
def time_profiler(function): # Wrapped Function
    def function_args(*args,**kwargs): # Args of the wrapped function

        # Before executing function - you can do any pre-steps
        # Execute the function
        #It's executed as self.function(*args,**kwargs)
        #It means the function will get executed with all of its arguments.
        # Set the Start time
        start_time = time.time()
        print("\n")
        print("-"*50)
        print("Execute Function - {} ".format(function.__name__))
        result = function(*args,**kwargs)   
        # Set the End time
        end_time = time.time()
        # Find the total time
        total_time = int(end_time-start_time)
        # Print the time in Seconds.
        print("Total time(Seconds) taken to execute function - {} is - {} seconds .".format(function.__name__,total_time))
        print("Total time(Minutes) taken to execute function - {} is - {} minutes .".format(function.__name__,total_time/60))
        print("\n")
        print("-"*50)
        # After executing function - you can do any post-steps
        return result
    return function_args

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 2 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a simple and time consuming function for expensive operations.
@time_profiler
def func_array_parser(*arrays):
    '''
        Parse arrays and filter the records.
        A Decorator is applied to this function to calculate the time taken.
        :param arrays: N number of arrays - tuple args
        * Perform multiple operations inside the function *
        Execution : Pass multiple arrays
            result = func_array_parser(range(10,1000),range(10,10000),range(100,5000),range(500,100000))
            print(result)
    '''
    for each_array in arrays:

        # Calculate sum of all numbers        
        def calc_sum():
            print("Calculate sum of all numbers")
            array_sum=0
            for element in each_array:
                array_sum+=element
            return array_sum

        # Calculate the Product of all numbers
        def calc_prd():
            print("Calculate the Product of all numbers")
            array_prd=0
            for element in each_array:
                array_prd+= element * 10
            return array_prd

        # Do multiple Iterations        
        def iterations():
            iter_sum = 0
            print("Do multiple Iterations")
            for element in each_array:
                for num in range(1,element):
                    iter_sum+=num
            return iter_sum

        # Execute the functions
        def driver():
            print("\n\n")
            print("Main Block :: Execute the functions in an order")
            # Call the Sum Method
            calc_sum()
            # Call the Prd Method
            calc_prd()
            # Call the Iterations Method
            iterations()
            print("\n\n")
        driver()# Execute the driver

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 