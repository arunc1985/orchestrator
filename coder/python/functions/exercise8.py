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
    
    In this section we will see in-detail about memory consumed by python programs in case
    of huge and expensive operations.

    If we would try to perform any operations and if our system is not configured to it,
    We would get MemoryError as below;

        $ python exercise8.py
        Traceback (most recent call last):
          File "exercise8.py", line 163, in <module>
            func_huge_tests(ranges=10)
          File "exercise8.py", line 143, in func_huge_tests
            huge_array.extend(list(range(100,100000000)))
        MemoryError
'''

# Import built-in modules
import time
import pdb
import os

# Import module from pypi
import psutil
from memory_profiler import profile

                                        # Example 1 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define functions for memory profiling.
def print_memory_stats():
    '''
        This program uses psutil module for finding the memory consumed by the processes.
    '''
    # Check Memory Usage
    process_id = os.getpid()
    process_details = psutil.Process(process_id)
    # Get memory info
    memory_info = process_details.memory_info()
    memoryUse = memory_info[0]# Returns in bytes.
    memory_use_in_mb=memoryUse/1000000
    print("\n\n\n *** LIVE *** \n\n\n")
    print('Memory in Megabytes - Used by Python Process ::', memory_use_in_mb)
    print("\n Describe Python Process... {} \n\n".format(psutil.Process(process_id)))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Write a simple function and add huge lists to it in a loop.
@profile
def func_huge_tests(ranges):
    '''
        Add items to the array as much as ranges specified above.
        :param ranges: Number of loops to run.

        Execute this function as ::

         Example - func_huge_tests(ranges=10)

        NOTE ::
            Running this program will result in MemoryError,
            if we append as huge_array.extend(list(range(10,100000000)))
            This Program uses a library - psutil for gathering information on
            memory usage of a Process at OS Level.
    '''
    # Create an empty array
    huge_array = []
    # Iterate and add values
    while True:
        # Decrement the ranges
        ranges -= 1
        # Extend the huge array with a big list.
        huge_array.extend(list(range(10,1000000)))
        # Print the memory details.
        print_memory_stats()
        print("Length of huge_array = {} ".format(huge_array.__len__()))

        # Check the memory consumed by running a Sub-Process Command.
        if ranges == 0:
            return huge_array
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


if __name__ == "__main__":

    # Execute 
    func_huge_tests(ranges=15)