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
'''

#Function without Arguments
def func_tests():
    '''
        Example: Execute as func_tests()
    '''
    return True

#Function with Arguments
def func_tests(x,y):
    '''
        Example: Execute as func_tests(10,20)
    '''
    return x*y

#Function with any n.o. Arguments
def func_tests_args(*args):
    '''
        Example: Execute as func_tests_args(10,20,25,30)
    '''
    x=0
    for i in args:
        x+=i
    return x


#Function with Keyword Arguments
def func_tests_kwargs(**kwargs):
    '''
        Example: Execute as func_tests_kwargs(x=10,y=20,z=30)
    '''
    for key,value in kwargs.items():
        print("Key = {} and Value = {} ".format(key,value))


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

if __name__ == "__main__":
    result = func_tests_nested(10,20)
    print(result)