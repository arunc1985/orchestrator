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

    Function Argument Types:
    ------------------------
        
        * There are 4 kinds of arguments to any given function. *

            1. Positional Arguments
            -----------------------
                
                Description ::
                --------------
                    
                    - Positional Arguments are passed in an order from left -> right .
                    - A Function can have any n.o. positional arguments .
                    - It's mandatory to pass values to all the positional arguments .
                    - Its mandate to pass values for all these arguments.
                    - If we dont pass any of the value it would result in an exception.

                Example ::
                ----------
                    
                    # A Simple function to add all the arguments in the function and return the final value.

                    def function(posa,posb,posc,posd):
                        # Add the numbers and return the final value.
                        return posa+posb+posc+posd
                    
                    This function has 4 arguments which are positional.
                    Its mandate to pass values for all these arguments.
                    If we dont pass any of the value it would result in an exception.

                Execution of above function ::
                ------------------------------

                    - function(10,20,30,40) # Valid - Has all the 4 Arguments.

                    - function(10,20,30) # Exception - Has only 3 Arguments.

                    - function(10,30,40) # Exception - Has only 3 Arguments.

                    - function(20,30,40) # Exception - Has only 3 Arguments.

            2. Tuple Arguments
            ------------------

                Description ::
                --------------
                    
                    - Tuple Arguments are denoted by * 
                    - A tuple argument can take any number of values. There is no limit.
                    - Unlike Positional Arguments tuple arguments gives freedom to pass any number of values.
                    - It's not mandatory to pass value to the tuple arguments .
                    - The arguments can be passed in any order, no restrictions .
                
                Example ::
                ----------
                    
                    # A Simple function to add all the arguments in the function and return the final value.
                    
                    def function(*args):
                        # Add the numbers and return the final value.

                        # Define a Counter
                        set_counter = 0

                        # For each iteration increment the counter by 1
                        
                        for data in args:
                            set_counter += 1
                        return set_counter
                
                Execution of above function ::
                ------------------------------
                    
                    - function(10,20,30,40) # Valid - Output is 4

                    - function(10,20,30) # Valid - Output is 3

                    - function(10,30) # Valid - Output is 2

                    - function(40) # Valid - Output is 1
                    
                    - function() # Valid - Output is 0.
                        - When no arguments are passed the output is 0, since variable set_counter is initialized as 0 .
                        - Variable set_counter is not incremented .
                        - The below for loop will not get executed since args is not passed.
                            for data in args:
                                set_counter += 1

            3. Keyword Arguments
            --------------------

                Description ::
                --------------
                    
                    - Keyword Arguments are denoted by **
                    - A keyword argument can take any number of values. There is no limit.
                    - keyword arguments are passed in key:value pairs.
                    - Unlike Positional Arguments keyword arguments gives freedom to pass any number of values.
                    - It's not mandatory to pass value to the keyword arguments .
                    - The arguments can be passed in any order, no restrictions .
                    - Keyword arguments are stored as dictionary.
                    - Keyword arguments are iterated as the way we iterate dictionary.
                        - for key,value in kwargs.items():
                              print(key,value)  
                
                Example ::
                ----------
                    
                    # A Simple function to add all the arguments in the function and return the final value.
                    
                    def function(**kwargs):
                        # Add the numbers and return the final value.

                        # Define a Counter
                        set_counter = 0

                        # For each iteration increment the counter by 1
                        
                        for key,value in kwargs.items():
                            set_counter += 1
                        return set_counter
                
                Execution of above function ::
                ------------------------------
                    
                    - function(x=10,y=20,z=30,a=40) # Valid - Output is 4

                    - function(x=10,y=20,z=30) # Valid - Output is 3

                    - function(x=10,z=30) # Valid - Output is 2

                    - function(y=40) # Valid - Output is 1

                    - function() # Valid - Output is 0.
                        - When no arguments are passed the output is 0, since variable set_counter is initialized as 0 .
                        - Variable set_counter is not incremented .
                        - The below for loop will not get executed since kwargs is not passed.
                            for key,value in kwargs.items():
                                set_counter += 1

            4. Default Arguments
            ---------------------

                Description ::
                --------------
                    
                    - Default Arguments are passed to the function as default values to arguments.
                    - They get initialized at the time of function creation.
                    - def function(x=10,y=20,z=30,a=40,b=50) during function creation will initialize the values as;
                          x=10,y=20,z=30,a=40,b=50
                    - Unlike Positional Arguments Default Arguments gives freedom to pass any number of values.                    
                    - The arguments can be passed in any order, no restrictions .
                    - It's not mandatory to pass value to the Default Arguments .
                        - During execution, If the values are not passed the default values will apply.
                        - During execution, If the values are passed the new values will apply and the
                          default values will not be taken.
                    - They look similar to positional arguments, but have some default values associated with it .


                Example ::
                ----------
                    
                    # A Simple function to add all the arguments in the function and return the final value.

                    def function(x=10,y=20,z=30,a=40,b=50):
                        # Add the numbers and return the final value.
                        return x+y+z+a+b

                Execution of above function ::
                ------------------------------
                    
                    # Check without modifying the default arguments
                    ------------------------------------------------
                        # Refer below, all default arguments are taken by default  - Output is 150.
                        - function(x=10,y=20,z=30,a=40) # Valid - Output is 150                
                        
                        # Refer below, arguments a,b are taken by default  - Output is 150.
                        - function(x=10,y=20,z=30) # Valid - Output is 150.
                        
                        # Refer below, arguments y,z are taken by default  - Output is 150.
                        - function(x=10,a=40) # Valid - Output is 150.
                        
                        # Refer below, arguments x,y,z are taken by default  - Output is 150.
                        - function(a=40) # Valid - Output is 150.
                    
                    # Check by modifying the default arguments
                    ------------------------------------------------
                        # Refer below, all default arguments are taken by default  - Output is 150.
                        - function(x=10,y=20,z=30,a=40) # Valid - Output is 150                
                        
                        # Refer below, arguments a,b are passed new values  - Output is 360.
                        - function(x=10,y=20,z=30,a=100,b=200) # Valid - Output is 360.
                        
                        # Refer below, arguments x,y,z,a,b are passed new values - Output is 306
                        - function(x=1,y=2,z=3,a=100,b=200) # Valid - Output is 306.

                    # Check by passing the default arguments in any order
                    ------------------------------------------------
                        # Refer below, arguments can be passed in any order - no issues at all.
                        - function(a=40,z=10,c=20,b=100,y=500) # Valid - Output is 670.

                        # Refer below, arguments can be passed in any order - no issues at all.
                        - function(z=10,c=20,b=0,y=500,a=40) # Valid - Output is 570.

                        # Refer below, arguments can be passed in any order - no issues at all.
                        - function(a=4,c=2,b=1,z=1,y=5) # Valid - Output is 13.

                        # Refer below, arguments can be passed in any order - no issues at all.
                        - function(z=10,y=10,x=10,b=10,a=10) # Valid - Output is 50.

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
        Example: 
            Execute as func_tests_args(10,20,25,30)
            Execute as func_tests_args()
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
# Example of positional and default arguments
def print_name(location,profession,fname='Arun',lname='Chandramouli'):
  """
    Params location and profession and positional args:
      -> Values must be passed else it will raise an Exception
      -> Values must be passed in an order

      Examples of Valid calls ::

        result = print_name("Chennai","Sofware")
        print(result)
        result = print_name("Bangalore","Sofware","Binita","Prasad")
        print(result)
        result = print_name("Bangalore","Sofware",lname="Prasad",fname="Binita")
        print(result)

      Examples of In-valid calls ::

        result = print_name() # Will return Exception
        print(result)
        result = print_name("Bangalore") # Will return Exception
        print(result)

    Params fname and lname are default arguments

      -> For default arguments the values get initialized during function creation.

      -> Even if we dont pass any values we still will not get any exception .

      -> If we pass any value the arguments will be reinitialized and it will take new values that we pass..

      Examples of Valid calls ::

        result = print_name("Chennai","Sofware")
        print(result)
        result = print_name("Bangalore","Sofware","Binita","Prasad")
        print(result)
        result = print_name("Bangalore","Sofware",lname="Prasad",fname="Binita")
        print(result)

        result = print_name()
        print(result)
        result = print_name("Bangalore")
        print(result)

    Execute as ::

    if __name__ == "__main__":

      result = print_name("Chennai","Sofware")
      print(result)

      result = print_name("Bangalore","Sofware","Binita","Prasad")
      print(result)


      result = print_name("Bangalore","Sofware",lname="Prasad",fname="Binita")
      print(result)



  """
  return fname + " " + lname

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 6
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Write a function and pass many arguments
# Example of positional and default arguments

def func_array(original_array,result_array = []):

  """
    Parameter original_array is a positional argument .
      -> Values must be passed, else it will raise an exception .

    Parameter result_array is a default argument .
      -> Even if we dont pass any values it wont raise any exception .
      -> If we pass values it will re-initialize and take the new value.

      In this case result_array is a default argument , an empty array.
      If we execute it as below with the default values :
       -> The result_array will get affected multiple times .
       -> The result_array will get appended and populated for each call.
       -> The array in the same memory location will get affected multiple times.

       Example ::

          STEP 1 ::
            result = func_array([1,2,3,4,5])
            print(result) # [2,4,6,8,10]

          STEP 2 ::
            result = func_array([1,2,3,4,5])
            print(result) # [2,4,6,8,10,2,4,6,8,10]
            The 2nd time we run it also contains the result of Step 1
            This is because result_array is a mutable argument and it gets
            affected in the same memory location.
          
          STEP 3 ::

            result = func_array([1,2,3,4,5],result_array=[100,200,300])
            print(result) # [100,200,300,2,4,6,8,10]

            In this case the result_array parameter is reinitialized
            and it will not contain the execution result of Step 1 and Step 2.

        Execute as ::

            if __name__ == "__main__":
              result = func_array([1,2,3,4,5])
              print(result)

              result = func_array([1,2,3,4,5])
              print(result)

              result = func_array([1,2,3,4,5],result_array=[100,200,300])
              print(result)
              
              result = func_array([1,2,3,4,5],result_array=[100,200,300])
              print(result)
              

  """
  
  # Iterate the original_array and multiply each number by 2...
  for each_val in original_array:
    # multiply by 2 and append to new array
    result_array.append(each_val*2)
  # Return the new modified array
  return result_array

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                          # Example 7
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Write a function and pass many arguments
# Example of tuple arguments

def func_array(*numbers):

  """
    Parameter numbers is a tuple argument .
    We can pass any number of values to this function.
    Even if we dont pass any value, it will not give any exception.

    Example ::

        result = func_array(1,2,3,4,5)
        print(result) # 15

        result = func_array()
        print(result) # 0
  """
  
  # Initialize the calc_sum as 0
  calc_sum = 0
  # Iterate the tuple * numbers * and find the sum of all the numbers.
  for each_val in numbers:
    calc_sum += each_val
  return calc_sum

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                          # Example 8
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

  #Function with Keyword Arguments
def func_tests_args_kwargs(*args,**kwargs):
    '''
      Function Creation :
       - kwargs is a keyword argument ... **
       - It gets stored as a python dictionary in memory
       - We need to iterate the dict and get the values     
        Example: Execute as func_tests_kwargs(x=10,y=20,z=30)

        *args and **kwargs are both optional arguments and
        they dont raise any error even if you dont pass any values...

        Pass value to both *args, **kwargs
        Pass value to *args alone
        Pass value to **kwargs alone
        Dont Pass value to both *args, **kwargs
    '''
    # Iterate the tuple args and get the values
    print("\nIterate the tuple args and get the values\n")
    for items in args:
      print(items)
    # Iterate the keyword args(dict) and print the values
    print("\nIterate the keyword args(dict) and print the values\n")
    for key,value in kwargs.items():
        print("Key = {} and Value = {} ".format(key,value))

# Pass value to both *args, **kwargs
print("\n\nPass value to both *args, **kwargs\n\n")
func_tests_args_kwargs(1,2,3,4,5,6,7,8,9,10,0,name='Arun',location='Chennai',profession="Programmer")

# Pass value to *args alone
print("\n\nPass value to *args alone\n\n")
func_tests_args_kwargs(1,2,3,4,5,6,7,8,9,10,0)

# Pass value to **kwargs alone
print("\n\nPass value to **kwargs alone\n\n")
func_tests_args_kwargs(name='Arun',location='Chennai',profession="Programmer")

# Dont Pass value to both *args, **kwargs
print("\n\nDont Pass value to both *args, **kwargs\n\n")
func_tests_args_kwargs()

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
