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

# Write a simple function to zip an iterable and return values

def function_zip_records(arrayA,arrayB,arrayC):
    '''
        Use built-in zip function to iterate on the iterable(array)
        and sum the values. Return the final sum.
        :param arrayA: An array of type list
        :param arrayB: An array of type list
        :param arrayC: An array of type list
        :return : Sum of all numbers in all lists
        :exception : Continue...
        : Execution Procedure:
            arrayA,arrayB,arrayC = [1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]
            sum_of_all_numbers = function_zip_records(arrayA,arrayB,arrayC)
            print(sum_of_all_numbers)
        When a zip function is applied over multiple iterables;
            -> It takes a value at a time from each iterable
            -> It does until all values are exhausted
        Example :
            arrayA,arrayB,arrayC = [1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]
            When you zip for elemA,elemB,elemC in zip(arrayA,arrayB,arrayC)
            It takes elements in an order as per index.
            0th index from arrayA,arrayB,arrayC THEN
            1st index from arrayA,arrayB,arrayC THEN
            2nd index from arrayA,arrayB,arrayC etc...
            Shown below ;

                1,10,100
                2,20,200
                3,30,300
                ....
                ....
    '''
    # Define a var to calculate the sum
    _sum = 0
    # Use zip built-in function to itreate on all arrays at same time
    for elemA,elemB,elemC in zip(arrayA,arrayB,arrayC):
        try:
            # Calc sum of all values
            _sum+= elemA+elemB+elemC
        except Exception as error:
            print(error)
            # Continue is used to prevent exception and process next record in the list
            continue 
    return _sum


if __name__ == "__main__":
    arrayA,arrayB,arrayC = [1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]
    sum_of_all_numbers = function_zip_records(arrayA,arrayB,arrayC)
    print(sum_of_all_numbers)
