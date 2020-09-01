'''
    Lambdas:
        Lambdas are also type of functions in python, they are inline and
        they dont have def keyword.
    
    As you see in the statement below;
        
        x = lambda arga:arga*2

        Here x is a variable.
        lambda is the built-in keyword to create functions at run-time
        arga is the parameter to the function
        and arga*2 -> Body of the function.
            It takes an argument calculates multiplies by 2
            and returns the result. 

        In this statement x = lambda arga:arga*2
        Please note the symbol ":" , 
            -> To the left of ":" is the function definition
            -> To the right of ":" is the body of the function

        The above statement is as good as writing a full blown function with def keyword
            
            * * * * * * * * * * 
            def funcA(arga):
                return arga*2
            * * * * * * * * * * 
            
        So in lambda - the functions are written as a one-liner, but it does the same job as a
        function written full blown with def keyword.
'''

                                        # Example 1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Using lambda functions with map for filtering elements in an array
'''
    Python has built-in feature known as map.
    The map takes function as a first argument and iterable(s) as 2nd argument.
    Example:
        def functionA(array):
            new_array = []
            for i in array:
                new_array.append(i*i)
            return new_array

    Use Map to execute it :
        map(functionA,[1,2,3,4,5])
        map(functionA,[1,2,3,4,5,10,20,30,40,50])
        map(lambda arrayA: arrayA*100,[1,2,3,4,5,10,20,30,40,50])
'''
# Simple lambda with list comprehension to filter the values
return_squares = lambda arrayA: arrayA**2 
print("\n")
print("Example 1 Output :: ")
# Use maps for taking function with an iterable..
iterable = [10,15,20,25,30,35,40,45,50]

'''
    The below map function takes 2 args, 1st argument is a function and 2nd argument is the array.
    What happens when the following is executed: result_map = map(return_squares,[10,15,20,25,30,35,40,45,50]) is as follows;
    1. A map object is created with function as variable and argument as iterable.
    2. For each and every item in the iterable, the function return_squares is called to find the square of the item.
    3. The result gets stored in memory as a list.
    4. It can be expanded as list(map_result)
    5. It can also be expanded as ;
       for item in map_result:
           print(item)
'''
# Execute the function and iterable using built-in maps.
map_result = map(return_squares,iterable)
print(list(map_result))

'''
    Output ::
        Example 1 Output ::
        [100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]

'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''
    Using normal functions with map.
    The map takes function as a first argument and iterable(s) as 2nd argument.
    An iterable is a type that can be iterated upon for getting the values.
    For example : Following can be iterated... lists, dicts, tuples, set, strings...
'''
def return_type_var(variable):
    '''
        Return the type of the variable.
        The type of an object can be found as variable.__class__ or type(variable)
    '''
    return variable.__class__

# An iterable to be passed
iterable = [100,200.50,-300,True,False,"Hello World!",[1000,2000],(1000,2000),{1:1,2:2}]

print("\n")
print("Example 2 Output :: ")

'''
    The below map function takes 2 args, 1st argument is a function and 2nd argument is the array.
    What happens when the following is executed: map_result =  map(return_type_var,iterable) is as follows;
    1. A map object is created with function as variable and argument as iterable.
    2. For each and every item in the iterable, the function return_type_var is called to check
       the type of the item.
    3. The result gets stored in memory as a list.
    4. It can be expanded as list(map_result)
    5. It can also be expanded as ;
       for item in map_result:
           print(item)
'''
# Execute the function and iterable using built-in maps.
map_result =  map(return_type_var,iterable)
print(list(map_result))


'''
    Output ::
        Example 2 Output ::
        [<class 'int'>, <class 'float'>, <class 'int'>, <class 'bool'>, <class 'bool'>, <class 'str'>, 
        <class 'list'>, <class 'tuple'>, <class 'dict'>]

'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
