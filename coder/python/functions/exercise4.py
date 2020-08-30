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

# Write a function that use all types of args
# Positional, tuple and Keyword args
def func_calc_values(x,y,*args,**kwargs):

    # Aim : Calculate sum of all values 
    _total_sum = 0
      
    # Iterate the tuple and add to the total sum
    for each_num in args:
        _total_sum+= each_num

    # Iterate Kwargs dict and add to total sum
    for each_num_key,each_num_val in kwargs.items():
        _total_sum+=each_num_val
      
    # Finally add x,y to iter
    _total_sum += x+y

    # Return the final ValueError
    return _total_sum

result = func_calc_values(100,200,10,20,30,40,50,a=1000,b=200,c=300,d=50)
print(result)



# Write a function to use positional and default arguments

def func_calc_values(x,y,z=5000):

    # Aim : Calculate sum of all values 
    _total_sum = 0
      
    # Finally add x,y to iter
    _total_sum += x+y+z
    # Return the final ValueError
    return _total_sum

result = func_calc_values(100,200,10)
print(result)

result = func_calc_values(100,200)
print(result)
