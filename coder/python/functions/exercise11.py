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

    In this example we will see the purpose of generators via functions.

    What are Generators?
      1. Generators are also iterables like Lists, Dicts..
      2. But Generators are also called as Lazy Iterators ...
      3. Lazy means they dont load all the values in the memory just like lists do.
      4. They yield each value one by one.
      5. For example ::

          Without Generators:
          --------------------
          - Let's say I have a list as [10,20,30......1000000] # This is huge list.
          - If i have to iterate and print the values in the list then all lists gets loaded in memory 
            and gets iterated as shown below;

            for data in huge_list:
                print(data)


          With Generators:
          --------------------
          - Let's say I have a list as [10,20,30......1000000] # This is huge list.
          - If i have to iterate and print the values in the list without data loaded in memory 
          - Generators use yield keyword.
          - Yield means generate only 1 value at a time.
          - In this case the entire list is not loaded into memory
          - Python refers to the memory location where the object huge list is stored.
          - It doesn't load all data, but sends data one by one.
          - Since it doesnt load huge data in memory - its faster and swift.
          - Writing Generator Code for List Processing :
  
              for data in huge_list:
                  yield data
    
    In this example we will see about memory used by python process in 2 scenarios:
        1. Without Generator :

            Refer function - func_array_parser_array

            As per the below example, a list is being populated with huge values and thus would result in MemoryError.

                Traceback (most recent call last):
                  File "exercise11.py", line 243, in <module>
                    func_array_parser_array(range(10,10000),range(100,20000),range(1000,5000),range(100,4000))
                  File "exercise11.py", line 235, in func_array_parser_array
                    master_array.extend(range(1,element))
                MemoryError

        2. With Generator :

            Refer function - func_array_parser_gen

            Generators doesn't store data in memory and thus we would not get MemoryError as above.

'''


# Import built-in modules
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

# Define a function to print the values in the Generator *
def func_gen_print_until_stop_iteration(gen_object):
    '''
      Print the values in the Generator Object.
      :param gen_object: Generator Object.
    '''
    try:
      # While Loop will run until all values in generator is exhausted.
      while True:
        gen_object.__next__()
    except StopIteration as error:
      # This block will get hit once all values are exhausted.
      print("All Records in Generator have been processed successfully!")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 3 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a simple and time consuming function for expensive operations.
def func_array_parser_gen(*arrays):
    '''
        Parse arrays and filter the records.
        A Decorator is applied to this function to calculate the time taken.
        :param arrays: N number of arrays - tuple args
        * Perform multiple operations inside the function *
        Execution : Pass multiple arrays
            # Create a Generator object
            gen_object = func_array_parser_gen(range(10,10000),range(100,20000),range(1000,5000),range(100,4000))
            # Generator invoke
            func_gen_print_until_stop_iteration(gen_object)
    '''
    # Master Array for adding data
    master_array = []
    # Iterate each array - for the sum
    for each_array in arrays:
        # Print memory stats
        print_memory_stats()
        for element in each_array:
            # Keep yielding the array - efficient way
            yield range(1,element)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a simple and time consuming function for expensive operations.
def func_array_parser_array(*arrays):
    '''
        Parse arrays and filter the records.
        A Decorator is applied to this function to calculate the time taken.
        :param arrays: N number of arrays - tuple args
        * Perform multiple operations inside the function *
        Execution : Pass multiple arrays
            func_array_parser_array(range(10,10000),range(100,20000),range(1000,5000),range(100,4000))            
    '''
    # Master Array for adding data
    master_array = []
    # Iterate each array - for the sum
    for each_array in arrays:
        print("Iterate each array - for the sum...")
        # Print memory stats
        print_memory_stats()
        # Iterate the array and do the processing
        for element in each_array:
            # Extend the array master_array with new array
            '''
                This will result in MemoryError since memory cant store so much of data.
                This is not an optimized way of coding.
            '''
            master_array.extend(range(1,element))
    # Return the array
    return master_array
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
