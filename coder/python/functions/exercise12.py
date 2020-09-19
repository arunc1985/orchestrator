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

                                        # Example 0
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

      gen_object.throw is used to throw any exception while processing
      records in an order.

      You can use and throw any built-in exception types of custome user-defined exception.

      This can be of good use while processing data pipelines.
      Add an if-condition and throw.
    
      Example ::
          if curr_item > 500:
            gen_object.throw(ValueError("Limit Reached and not required to proceed further !"))


    '''
    try:
      # While Loop will run until all values in generator is exhausted.
      while True:
        curr_item = gen_object.__next__()
        print(curr_item)
        # Raise an exception and exit if value crossed certain limit.
        if curr_item > 500:
          gen_object.throw(ValueError("Limit Reached and not required to proceed further !"))

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
          array = range(10,100)

          # STEP 1 ::
          # Creating the Generator Object - Calling function with args will not execute it.
          # Calling function with argument will actually create a generator object and keep it in memory.
          print("STEP 1 :: Creating the Generator Object")
          gen_object=func_gen_tests(array)
          print("Generator Object :: {} ".format(gen_object))

          # STEP 2 ::
          # List all the value inside the generator object ..Expand the Genrator and get all records.
          print("STEP 2 :: List all the value inside the generator object.")
          func_gen_print_records(gen_object=gen_object)

          # Q: Is it possible to unpack the same gen object more than once ?  
          # A: No, Because Python deletes/purges the data inside of gen object once it has been unpacked.
          # It will not store those data in memory once its unpacked.
          # A Gen object is optimized - you can iterate only once and unpack, then its deleted.
          func_gen_print_records(gen_object=gen_object)

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
      Function to iterate an array and yield the records multiple times.
      
      ** Its possible to have any number of yield statements in a function **

      Execute this function as follows:

          # Define array
          array = [1,2,3,4,5]

          # STEP 1 ::
          # Creating the Generator Object - Calling function with args will not execute it.
          # Calling function with argument will actually create a generator object and keep it in memory.
          print("STEP 1 :: Creating the Generator Object")
          gen_object=func_gen_tests_multiple(array)

          print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
          print("Generator Object :: {} ".format(gen_object))

          # STEP 2 ::
          # List all the value inside the generator object ..Expand the Genrator and get all records.
          print("STEP 2 :: List all the value inside the generator object.")
          print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
          func_gen_print_records(gen_object=gen_object)

          # STEP 3 ::
          # Repeat STEP 2 and List all the value inside the generator object.
          print("STEP 3 :: Repeat STEP 2 and List all the value inside the generator object.")
          print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
          # This STEP will not yield any records since it has been already done in STET 2
          func_gen_print_records(gen_object=gen_object)


          # Q: Is it possible to unpack the same gen object more than once ?  
          # A: No, Because Python deletes/purges the data inside of gen object once it has been unpacked.
          # It will not store those data in memory once its unpacked.
          # A Gen object is optimized - you can iterate only once and unpack, then its deleted.
          func_gen_print_records(gen_object=gen_object)

      What happens with multiple yield
      In this case the array [1,2,3,4,5]will get yielded as follows;
        yield 1
        yield 1 * 10
        yield 2
        yield 2 * 10
        yield 3
        yield 3 * 10
        yield 4
        yield 4 * 10
        yield 5
        yield 5 * 10
        
        Which will give output as 1,10,2,20,3,30,4,40,5,50

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
      # Yield the number to the power of 2 
      yield data ** 2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Define a function to use generator and send the values.Use multiple yield statements, with if-else conditions.
def func_gen_tests_multiple_if_else(int_var,array):
    '''
      Function to iterate an array and yield the records.
      :param int_var: An Integer
      :param array: List of values

      # Define array
      array = range(100,200)# Starting with 100 and ending with 199

      # STEP 1 ::
      # Creating the Generator Object - Calling function with args will not execute it.
      # Calling function with argument will actually create a generator object and keep it in memory.
      print("STEP 1 :: Creating the Generator Object")
      print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
      print("Generator Object :: {} ".format(gen_object))

      # STEP 2 ::
      # List all the value inside the generator object ..Expand the Genrator and get all records.
      print("STEP 2 :: List all the value inside the generator object.")
      print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
      func_gen_print_records(gen_object=gen_object)

      # STEP 3 ::
      # Repeat STEP 2 and List all the value inside the generator object.
      print("STEP 3 :: Repeat STEP 2 and List all the value inside the generator object.")
      print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
      # This STEP will not yield any records since it has been already done in STET 2
      func_gen_print_records(gen_object=gen_object)

    '''
    # Iterate and yield using *yield* keyword
    # This function will yield each number followed by the number * 10, for all the numbers.
    for data in array:
      '''
        All Records not loaded in memory.
        Send data one by one.
      '''
      # Send Data if divisible by number int_var else Multiply by 10 and send data
      yield data if data%int_var==0 else "Number - {} is not divisible by - {} ".format(data,int_var)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Define a function to use generator and send the values.Use multiple yield statements, with if-else conditions.
def func_gen_tests_multiple_if_else_args(int_var,*args):
    '''
      Function to iterate an array and yield the records.
      :param int_var: An Integer
      :pararm args: Tuple Arguments..


      # STEP 1 ::
      # Creating the Generator Object - Calling function with args will not execute it.
      # Calling function with argument will actually create a generator object and keep it in memory.

      print("STEP 1 :: Creating the Generator Object")
      gen_object=func_gen_tests_multiple_if_else_args(5,10,11,20,30,40,45,25,55,50,60,65)
      print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
      print("Generator Object :: {} ".format(gen_object))

      # STEP 2 ::
      # List all the value inside the generator object ..Expand the Genrator and get all records.
      print("STEP 2 :: List all the value inside the generator object.")
      print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
      func_gen_print_records(gen_object=gen_object)

      # STEP 3 ::
      # Repeat STEP 2 and List all the value inside the generator object.
      print("STEP 3 :: Repeat STEP 2 and List all the value inside the generator object.")
      print("Generator Object is - {} and stored at location - {} ".format(gen_object,id(gen_object)))
      # This STEP will not yield any records since it has been already done in STET 2
      func_gen_print_records(gen_object=gen_object)

    '''
    # Iterate and yield using *yield* keyword
    # This function will yield each number followed by the number * 10, for all the numbers.
    for curr_item_in_tuple in args:
      '''
        All Records not loaded in memory.
        Send data one by one.
      '''
      # Send a dictionary - If divisible by int_var multiply by 10 and send else the original number.
      yield {curr_item_in_tuple:curr_item_in_tuple * 10} if curr_item_in_tuple%int_var==0 \
            else {curr_item_in_tuple:curr_item_in_tuple}
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 5
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Define a function to use generator and send the values.Use yield from statement
def func_gen_tests_from(args):
  """
  
    Use yield from to generate the values.
    Run as :
      gen_object = func_gen_tests_from(1,2,3,4,5,6,7,8,9,10,11)
      func_gen_print_until_stop_iteration(gen_object)

    yield from -> Will automatically start For-Loop internally and generate the values.

    Without yield from
    ------------------

      for each_element in args:
        yield each_element

    With yield from
    ------------------

      yield from args


  """
  yield from args

    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

if __name__ == "__main__":

    gen_object = func_gen_tests_from(range(100,5000))
    func_gen_print_until_stop_iteration(gen_object)
