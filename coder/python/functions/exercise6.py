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

    In this example we will see the code object that's associated with python functions.
    It helps us understand how the functions work internally.

    Let's say we have a function ::

        def func_tests():
            return True

        The code object can be obtained as func_tests.__code__

         func_tests.__code__

         Output ::
            <code object func_tests at 0x01BD30F0, file "<stdin>", line 1>
'''

#Function without Arguments
def func_tests():
    '''
        Example: Execute as func_tests()
    '''
    return True


#Function with Arguments
def func_tests_args(arg_a,arg_b):
    '''
        Example: Execute as func_tests_args(10,20)
    '''
    return arg_a * arg_b

if __name__ == "__main__":
  
  # Output of individual functions
  print(func_tests())
  print(func_tests_args(100,200))

  # Print the code objects of functions func_tests and func_tests_args
  print("Code Object of function func_tests - {} ".format(func_tests.__code__))
  print("Code Object of function func_tests_args - {} ".format(func_tests_args.__code__))

  # Modify the functions internals
  # The logic of function func_tests_args now applies to function func_tests
  # Hence after this we must call function func_tests with arguments arg_a, arg_b
  # But as you see above function func_tests doesn't take any arguments.
  # After modifying the code object as shown below function func_tests will have to be called with arguments.

  func_tests.__code__ = func_tests_args.__code__

  # Output of individual functions after the code object manipulation.
  print(func_tests(10,20))
  print(func_tests_args(100,200))  