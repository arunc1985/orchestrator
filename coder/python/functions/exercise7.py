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


'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a function to print the values in the Generator *
def func_gen_print_records(gen_object):
    '''
      Print the values in the Generator Object.
      :param gen_object: Generator Object.
    '''
    # Iterate and yield using *yield* keyword
    for data in gen_object:
      '''
        All Records not loaded in memory.
        Send data one by one.
      '''
      print(data)


# Define a function to print the values in the Generator *
def func_gen_print_until_stop_iteration(gen_object):
    '''
      Print the values in the Generator Object.
      :param gen_object: Generator Object.
    '''
    try:
      # While Loop will run until all values in generator is exhausted.
      while True:
        print(gen_object.__next__())
    except StopIteration as error:
      # This block will get hit once all values are exhausted.
      print("All Records in Generator have been processed successfully!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Define a function to use generator and send the values.
def func_gen_tests(array):
    '''
      Function to iterate an array and yield the records.
      Execute this function as follows:
        # Define array
        array = [10,20,30,40,50 ....... 100000]
         Method 1 : func_gen_print_records(gen_object=func_gen_tests(array))
         Method 2 : func_gen_print_until_stop_iteration(gen_object=func_gen_tests(array))
         Output : Prints 10,20....99999
    '''
    # Iterate and yield using *yield* keyword
    for data in array:
      '''
        All Records not loaded in memory.
        Send data one by one.
      '''
      yield data

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Define a function to use generator and send the values.Use multiple yield statements.
def func_gen_tests_multiple(array):
    '''
      Function to iterate an array and yield the records.
      Execute this function as follows:
        # Define array
        array = [10,20,30,40,50]
         Method 1 : func_gen_print_records(gen_object=func_gen_tests(array))
         Method 2 : func_gen_print_until_stop_iteration(gen_object=func_gen_tests(array))
         Output : Prints 10,100,20,200,30,300,40,400,50,500
    '''
    # Iterate and yield using *yield* keyword
    # This function will yield each number followed by the number * 10, for all the numbers.
    for data in array:
      '''
        All Records not loaded in memory.
        Send data one by one.
      '''
      # Send Data
      yield data
      # Multiply by 10 and send data
      yield data * 10

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Define a function to use generator and send the values.Use multiple yield statements, with if-else conditions.
def func_gen_tests_multiple_if_else(int_var,array):
    '''
      Function to iterate an array and yield the records.
      :param int_var: An Integer
      :param array: List of values

      Execute this function as follows:
        # Define array
        array = [10,20,30,40,50,27,89,99,209,500]
         Method 1 : func_gen_print_records(int_var=5,gen_object=func_gen_tests(array))
         Method 2 : func_gen_print_until_stop_iteration(int_var=10,gen_object=func_gen_tests(array))
         Output : Prints 10,20,30,40,50,270,890,990,2090,500
    '''
    # Iterate and yield using *yield* keyword
    # This function will yield each number followed by the number * 10, for all the numbers.
    for data in array:
      '''
        All Records not loaded in memory.
        Send data one by one.
      '''
      # Send Data if divisible by number int_var else Multiply by 10 and send data
      yield data if data%int_var==0 else data * 10

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 4
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



                                        # Example 5
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

