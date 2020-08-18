'''
# Write Decorators and apply to source-code
A Decorator is also a python function that takes a function and its arguments as input,
executes it and returns the final result.

The Decorators can also be written as a class and be applied to other functions/methods.

Basically decorators come in 2 types,

    1. Decorator with Arguments
    2. Decorator without Arguments

    Example of decorator without arguments
    **************************************

    @decorator # This decorator is not having arguments.
    def funcA(x,y):
        return True

    Example of decorator with arguments
    ************************************

    @decorator("hello",10,20) # This decorator is having arguments as "hello",10,20
    def funcA(x,y):
        return True

Sample decorator that is not having any arguments will be looking as below;
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def decorator_function(function):
    # param function denotes the function to be decorated

    def execute_function(*args,**kwargs):
        # param *args,**kwargs denotes the arguments of the function to be decorated

        # command function(*args,**kwargs) -> will execute the function to be decorated with all of its argument
        result = function(*args,**kwargs)

        # Return the result of the function after execution
        return result 

    # Return this function so that the outer function will call and execute it
    return decorator_function 

Sample decorator that is having any arguments will be looking as below;
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def decorator_function_arguments(*deco_args,**deco_kwargs):
    """
    *** NOTE :: Please be informed that *** 
    # param *deco_args,**deco_kwargs denotes the arguments of the decorator function 
    and not the function to be decorated.
    """
    
    def decorator_function(function):
        # param function denotes the function to be decorated
        
        def execute_function(*args,**kwargs):
            # param *args,**kwargs denotes the arguments of the function to be decorated

            # command function(*args,**kwargs) -> will execute the function to be decorated with all of its argument
            result = function(*args,**kwargs)

            # Return the result of the function after execution
            return result 

        # Return this function so that the outer function will call and execute it
        return execute_function 

    # Return this function so that the outer function will call and execute it
    return decorator_function 

'''


'''
    Write Decorators and apply to source-code
    Apply multiple decorators to the same function and return final output
    When a function has multiple decorators, it gets executed an in order.
    For example let's say function funcA has 2 decorators
    @deco1
    @deco2
    def funcA():
        pass
    -> deco2 gets called and executes first, followed by deco1.
'''

# Decorator to execute a function and return the result...
def decorator_exec_final(function): # Wrapped Function
    def function_args(*args,**kwargs): # Args of the wrapped function

        # Before executing function - you can do any pre-steps
        # Execute the function
        #It's executed as self.function(*args,**kwargs)
        #It means the function will get executed with all of its arguments.
        result = function(*args,**kwargs)   
        # After executing function - you can do any post-steps
        return result*50 # Multiply final result by 10 and return.
    return function_args

# Decorator to execute a function and return the result...
def decorator_exec_main(function): # Wrapped Function
    def function_args(*args,**kwargs): # Args of the wrapped function

        # Before executing function - you can do any pre-steps
        # Execute the function
        #It's executed as self.function(*args,**kwargs)
        #It means the function will get executed with all of its arguments.

        result = function(*args,**kwargs)       
        # After executing function - you can do any post-steps
        return result*10 # Multiply final result by 10 and return.
    return function_args

# A function to do simple multiplication - Apply multiple decorators to this function
'''
    When this function is executed,
        1. It first gets executed by decorator decorator_exec_main and result is taken.
        2. The result from Step-1 is passed to decorator_exec_final, multiplied and returned.

            -> So in this case function apply_tests is first executed by decorator_exec_main
            -> Let's say you execute the function apply_tests , like this apply_tests(10,20)
            -> When it first gets executed by decorator_exec_main, result becomes (10*20)*10 = 2000
            -> This result 2000 is passed to the next decorator in order - decorator_exec_final
               and the result becomes as , 2000 * 50 = 100000
            -> So Final result is 100000
'''
@decorator_exec_final # Called 2nd
@decorator_exec_main # Called 1st - Output as 2000
def apply_tests(x,y):
    '''
        Order of Execution:
            1. Function apply_tests will be executed by deco decorator_exec_main
            2. Deco Function decorator_exec_main will be exec by deco decorator_exec_final
    '''
    return x*y

if __name__ == "__main__":

    # Execute
    final_result = apply_tests(10,20)
    print("Final Result is - {} ".format(final_result))