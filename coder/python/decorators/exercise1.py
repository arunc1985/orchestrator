# Write Decorators and apply to source-code

# Type 1 : Decorator without arguments. This will take function and it's args as input, execute and return output

def decorator_exec(function): # Wrapped Function
    def function_args(*args,**kwargs): # Args of the wrapped function
        print("Args of the function {} are {} and {} ".format(function.__name__,args,kwargs))
        # Execute the function
        result = function(*args,**kwargs)
        # Prepare final result
        kwargs['fin_result'] = result
        print("Result of function {} is {} ".format(function.__name__,kwargs))
        return result
    return function_args

'''
# Type 2 : Decorator with arguments. 
This will take function and it's args as input, it will also take arguments to the decorator
Then execute and return output
'''
def decorator_exec_with_args(*deco_args,**deco_kwargs): # Args of decorator
    def decorator_wrapped_func(function): # Wrapped Function
        def function_args(*func_args,**func_kwargs): # Args of the wrapped function
            print("Args of the function {} are {} and {} ".format(function.__name__,func_args,func_kwargs))
            # Execute the function
            result = function(*func_args,**func_kwargs)
            print("Result of function {} is {} ".format(function.__name__,result))
            return result
        return function_args
    return decorator_wrapped_func


# Test the above decorator with examples

# Test Type 1 decorator
@decorator_exec # This decorator is not having arguments
def test_decorator_exec(x,y,*args,**kwargs):
    maparray = []
    for i in args:
        maparray.append(i)
    maparray.extend([x,y])
    return maparray

# Test Type 2 decorator
@decorator_exec_with_args(mapper_range=range(1000,2000)) # This decorator is having arguments
def test_decorator_exec_with_args(x,y,*args,**kwargs):
    maparray = []
    for i in args:
        maparray.append(i)
    maparray.extend([x,y])
    return maparray



if __name__ == "__main__":
    test_decorator_exec_with_args(100,200,10,20,30,40,50,60,70,80,90,300,name='Arun',profession='Programmer')