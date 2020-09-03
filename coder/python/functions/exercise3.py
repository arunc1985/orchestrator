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

# Import functools module fore reduce operations...
import functools

                                        # Example 1 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 1 :: Simple lambda to take an argument, multiply by 2 and return final value.
result = lambda arga:arga*2
print("\n")
print("Example 1 Output :: ")
print(result(50)) # Result will be 100

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 2 ::  Simple lambda to take 2 arguments, multiply and return final value.
result = lambda arga,argb:arga*argb
print("\n")
print("Example 2 Output :: ")
print(result(50,2)) # Result will be 100

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Example 3 
# Simple lambda to take 2 arguments, multiply and return final value.
# Twist the lambda with if conditions
result = lambda arga,argb:arga*argb if argb>0 and arga>0 else "Please provide positive values"
print("\n")
print("Example 3 Output :: ")
print(result(50,2)) # Result will be 100
print(result(50,-10)) # Result will be Please provide positive values

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Example 4
# Simple lambda to take 3 arguments, calcuate as per action parameter and return final value.
# Twist the lambda with multiple if conditions
result = lambda arga,argb,action:(arga*argb) if action=='PRD' \
         else (arga+argb) if action=='SUM' \
         else (arga**argb) if action=='POW' \
         else "Please enter valid options"
print("\n")
print("Example 4 Output :: ")
print(result(50,2,"PRD")) # Result will be 100
print(result(50,5,"SUM")) # Result will be 55
print(result(50,2,"POW")) # Result will be 2500
print(result(50,2,"POWER")) # Result will be Please enter valid options

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 5
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Example 5
# Simple lambda to take an iterable(List) and an element as arguments
# It returns True if element_search is in arrayA else False

result = lambda arrayA,element_search:True if element_search in arrayA else False
print("\n")
print("Example 5 Output :: ")
print(result(arrayA=[1,2,3,4,5],element_search=100)) # Returns False
print(result(arrayA=[1,2,3,4,5],element_search=1)) # Returns True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 6
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Example 6
# lambda function with built-in filters
# In this example we will use built-in filter function along with lambda
# Filter function is used for filtering an iterable based on a condition
# Ex: Let's say we have an arrayA=[10,20,30,40,50], from this filter all elements > 25
# Ex: Let's say we have an arrayA=[10,20,30,42,51], from this filter all elements divisible by 10
# Ex: Let's say we have an arrayA=[2,3,4,6,8], from this filter all elements divisible by 2
# filter takes 2 arguments, 1. lambda function with condition 2. Iterable
# filter(lambda with condition , iterable)

# Define a lambda with condition as element divisible by 10
lambda_stmt = lambda array_element:array_element%10==0
# Filter only the elements that satisfy the above condition
result = filter(lambda_stmt,range(100,200))# range(100,200) -> 100,101,102...199

'''
# For the given range of values range(100,200), the filter function calls lambda and applies condition
# The condition is array_element%10==0 -> Check if the given number in the iterable is divisible by 10
# The filter function applies the condition for all elements in the array and filters the values
# Ex: When we pass filter(lambda_stmt,range(100,200)), what happens is as follows
    1. filter function takes 2 argument , 1. lambda_stmt and 2. range(100,200)
    2. For each and every element in this array range(100,200)
    3. It applies the filter condition lambda_stmt (lambda array_element:array_element%10==0)
    4. The filtered values get added to memory internally
    5. When we expand the result as list(result), it gives all the filtered values
'''

print("\n")
print("Example 6 Output :: ")
print(list(result))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 7
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# lambda function with built-in filters
# In this example we will use built-in filter function along with lambda
# Filter function is used for filtering an iterable based on a condition
# Ex: Let's say we have an arrayA=[10,20,30,40,50], from this filter all elements > 25
# Ex: Let's say we have an arrayA=[10,20,30,42,51], from this filter all elements divisible by 10
# Ex: Let's say we have an arrayA=[2,3,4,6,8], from this filter all elements divisible by 2
# filter takes 2 arguments, 1. lambda function with condition 2. Iterable
# filter(lambda with condition , iterable)
# In the example below we apply multiple condition as "and",
# array_element%10==0 and array_element%100==0

# Define a lambda with condition as element divisible by 10 and divisible by 100
lambda_stmt = lambda array_element:array_element%10==0 and array_element%100==0
# Filter only the elements that satisfy the above condition
result = filter(lambda_stmt,range(100,200))

print("\n")
print("Example 7 Output :: ")
print(list(result))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 8
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Using lambda functions with list comprehension for filtering elements in an array
# List comprehension are short-hand expressions for full blown for-loop
'''
    Lets say we have below for loop
    result = []
    for element in arrayA:
        if element>10:
            result.append(element)
    return result # This result is a new list compared to arrayA

    This can be converted using list comprehension as follows
    # This result is a new list compared to arrayA
    result = [element for element in arrayA if element > 10]

    Same can be done for multiple for loops
    result = []
    for elementA in arrayA:
        for elementB in arrayB:
            if elementA > 0 and element>0:
                result.append(elementA*elementB)
    return result
    
    [elementA*elementB for elementA in arrayA for elementB in arrayB if elementA > 0 and element>0]

    This can be converted using list comprehension as follows
    result = [elementA*elementB for elementA in arrayA for elementB in arrayB if elementA > 0 and element>0]
'''
# Simple lambda with list comprehension to filter the values
result = lambda arrayA:[element for element in arrayA if element%10==0]
print("\n")
print("Example 8 Output :: ")
print(result([10,15,20,25,30,35,40,45,50]))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 9
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Using lambda functions with list comprehension for filtering elements in an array
# In this function we will use lambda with 2 arguments and filter the elements
# List comprehension are short-hand expressions for full blown for-loop


print("\n")
print("Example 9 Output :: ")
# Simple lambda with list comprehension to filter the values
result = lambda arrayA,element_divide_by:[element for element in arrayA if element%element_divide_by==0]
print(result(arrayA=[10,15,20,25,30,35,40,45,50,100,200,500],element_divide_by=100))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 10
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Using lambda functions with list comprehension for filtering elements in an array
# In this function we will use lambda with 2 arguments and filter the elements
# In this example , We will also use multiple levels of for-loop *
# List comprehension are short-hand expressions for full blown for-loop

# Simple lambda with list comprehension to filter the values
'''
    The below function takes 3 arguments namely
    arrayA, arrayB, element_check
    arrayA -> List , arrayB -> List , element_check -> Integer

    It runs for loop for arrays arrayA, arrayB
    It applies condition if element in arrayA and element in arrayB are >er than element_check
        if YES then it calculates the product
    It does so for each and every element in arrayA, arrayB and result is stored in memory
    Finally the result is returned

    The below lambda function can also be written using normal python function

    def filter_element(arrayA,arrayB,element_check):
        result = []
        for elementA in arrayA:
            for elementB in arrayB:
                if elementA>element_check and elementB>element_check:
                    result.append(elementA*elementB)
        return result
'''
# Write lambda statement to acheive above mentioned function..

result = lambda arrayA,arrayB,element_check:\
         [elementA*elementB \
         for elementA in arrayA \
         for elementB in arrayB \
         if elementA>element_check and elementB>element_check]

print("\n")
print("Example 10 Output :: ")

print(result(arrayA=[10,20,30,40,50],arrayB=[60,70,80,90,100],element_check=0))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 11
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 11 ::  Simple lambda to take an iterable sort and return the sorted new array

# Lambda function that takes an argument and return the same argument - no other action.
lambda_function = lambda item_in_list:item_in_list
print("\n")
print("Example 11 Output :: ")
# Array to be sorted
array_to_sort = [10,1,20,30,3,4,5,6,9,11,-1,-10,20]
sorted_array = sorted(array_to_sort)
print(sorted_array)
# Sort array using key as lambda function
sorted_array = sorted(array_to_sort,key=lambda_function)
print(sorted_array)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 12
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 12 ::  Simple lambda to take an iterable sort and return the sorted new array

# Lambda function that taken an argument and multiply by 2 and return the result.
lambda_function = lambda item_in_list:item_in_list*2
print("\n")
print("Example 12 Output :: ")
# Array to be sorted
array_to_sort = [10,1,20,-30,3,4,5,6,9,11,-1,-10,20]
sorted_array = sorted(array_to_sort)
print(sorted_array)
# Sort array using key as lambda function
sorted_array = sorted(array_to_sort,key=lambda_function)
print(sorted_array)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 13
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 13 ::  Simple lambda to take an iterable sort and return the sorted new array

# Lambda function that taken an argument and form the square of an argument and return the result.
# The original array would get sorted based on the squared values.

lambda_function = lambda item_in_list:item_in_list ** 2
print("\n")
print("Example 13 Output :: ")
# Array to be sorted
array_to_sort = [10,1,20,-30,3,4,5,6,9,11,-1,-10,20]
sorted_array = sorted(array_to_sort)
print(sorted_array)

'''
    Sort array using key as lambda function. In the below example even though we have -ve values such as -30, -1, -10 
    in the array [10,1,20,-30,3,4,5,6,9,11,-1,-10,20] , the final output would look as follows;
    [1, -1, 3, 4, 5, 6, 9, 10, -10, 11, 20, 20, -30]
    
    This is because in the lambda function  lambda item_in_list:item_in_list ** 2,
    We had taken the square of each number as item_in_list ** 2.
    Hence negative numbers like -10,-1,-30 becomes positive.
    Hence if we can see the array as below ;
    [1, -1, 3, 4, 5, 6, 9, 10, -10, 11, 20, 20, -30]
    It's computed as good as [1, 1, 9, 16, 25, 36, 81, 100, 100, 121, 400, 400, 900]

    * But the final result will be the original entries based on computation.
    Final Output :: [1, -1, 3, 4, 5, 6, 9, 10, -10, 11, 20, 20, -30]

'''
sorted_array = sorted(array_to_sort,key=lambda_function)
print(sorted_array)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 14
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 14 ::  Simple lambda to take a dictionary, sort based on keys and values.

# Lambda function to sort a dictionary based on keys
maps = {1:1,2:1,3:2,4:40,10:9,7:6,10:30,5:300}

print("\n")
print("Example 14 Output :: ")

# Lambda function to sort a dictionary based on values
result =  sorted(maps.items(),key=lambda x:x[1])
print("Sort dictionary by values - {} ".format(result))

# Lambda function to sort a dictionary based on keys
result =  sorted(maps.items(),key=lambda x:x[0])
print("Sort dictionary by keys - {} ".format(result))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 15
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 15 ::  Simple lambda along with reduce to take a array, find sum of elements in the array

# Define an Iterable
iterable = range(10,20) #[10,11,12,...19]

'''
    How reduce works for finding the sum of iterables... iterable = range(10,20)
    reduce takes 2 arguments, 1. Function and 2. Iterable.
    In this case the iterable is range(10,20) expanded as follows;
    [10,11,12,13,14,15,16,17,18,19]
    [21] [12,13,14,15,16,17,18,19]
    [33] [13,14,15,16,17,18,19]
    ......

    As you see below the reduce function is defined as below;
    functools.reduce(lambda x,y:x+y, iterable)

    It takes 1st arg as lambda function - lambda x,y:x+y and 
             2nd arg as iterable - range(10,20)

    reduce works on the principle of folding, it takes 2 numbers at a time, 
    calculates the result and
    accumulates result with the 3rd..
    and so on so-forth untill all the numbers are exhausted.

    When the following command is run - functools.reduce(lambda x,y:x+y, iterable)
    What happens is as follows;

        1. reduce function at first takes 10,11 
           and finds the result as 21. -> 10,11 are the first 2 elements.
        2. 21 + 12 = 33 -> Next element is 12
        3. 33 + 13 = 46 -> Next element is 13
        4. 46 + 14 = 60 -> Next element is 14
        5. 60 + 15 = 75 -> Next element is 15
        6. 75 + 16 = 91 -> Next element is 16
        7. 91 + 17 = 108 -> Next element is 17
        8. 108 + 18 = 126 -> Next element is 18
        9. 126 + 19 = 145 -> Next element is 19

        Final Result is :: 145
'''
# Define a reduce function with lambda to find the sum
result = functools.reduce(lambda x,y:x+y, iterable)
print("\n")
print("Example 15 Output :: ")
print(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




                                        # Example 16
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 16 ::  Simple lambda along with reduce to take a array, find product of elements in the array

# Define an Iterable
iterable = range(5,10)

'''
    How reduce works for finding the product of iterables... iterable = range(10,20)
    reduce takes 2 arguments, 1. Function and 2. Iterable.
    In this case the iterable is range(10,20) expanded as follows;
    [5,6,7,8,9]
    As you see below the reduce function is defined as below;
    functools.reduce(lambda x,y:x*y, iterable)

    It takes 1st arg as lambda function - lambda x,y:x+y and 2nd arg as iterable - range(10,20)
    reduce works on the principle of folding, it takes 2 numbers at a time, calculates the result and
    accumulates result with the 3rd..and so on so-forth untill all the numbers are exhausted.

    When the following command is run - functools.reduce(lambda x,y:x*y, iterable)
    What happens is as follows;

        1. reduce function at first takes 5,6 and finds the result as 30. -> 5,6 are the first 2 elements.
        2. 30 * 7 = 210 -> Next element is 7
        3. 210 * 8 = 1680 -> Next element is 8
        4. 1680 * 9 = 15120 -> Next element is 9

        Final Result is :: 15120
'''
# Define a reduce function with lambda to find the sum
result = functools.reduce(lambda x,y:x*y, iterable)
print("\n")
print("Example 16 Output :: ")
print(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 17
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Using lambda functions with dictionary comprehension for filtering elements in an array
# Dictionary comprehension are short-hand expressions for full blown dictionary...

'''
    Lets say we have below for loop for iterating on a dictionary
    result = {}
    for key,val in dictionary.items():
        if key>10 and val>10:
            result[key]=value
    return result

    The for loop can be replaced as follows;
    result = {key:val for key,val in dictionary.items() if key>10 and val>10}
    
'''
# Simple lambda with dictionary comprehension to filter the values based on if condition...
result = lambda dictionary,val_check:{key:val for key,val in dictionary.items() if val>val_check and key>val_check}

print("\n")
print("Example 17 Output :: ")

# Define a dictionary
dictionary = {3:9,5:25,8:64,10:100,15:150,20:200,25:200}
print(result(dictionary=dictionary,val_check=5))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 18
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Using lambda functions with generator expressions.

'''
    Lets say we have below for loop for iterating on a dictionary
    result = {}
    for key,val in dictionary.items():
        if key>10 and val>10:
            result[key]=value
    return result

    The for loop can be replaced into generator expression as follows;
    result = (key for key,val in dictionary.items() if val>val_check and key>val_check)
    
    A Generator is an object which has to be expanded and there are 2 ways to expand.

    1. Using lists
    2. Using StopIteration

    Let's say I have a simple generator object gen_x.

    To know the values inside gen_x :

        1. Using Lists

            for each_val in gen_x:
                print(each_val)

        2. Using StopIteration

            try:
                while True:
                    print(gen_x.__next__())
            except StopIteration:
                print("All values exhausted from Generator...")

        Note:: Once a generator value is obtained it will be exhausted from memory. It will not be available.

'''

# Define a function to handle generator expression.

def generate_data(generator_expression):
    '''
        :param generator_expression : A Generator object to be iterated.
    '''
    try:
        while True:
            print(generator_expression.__next__())
    except StopIteration:
        print("All values exhausted from Generator...")
        return True

# Simple lambda with generator expression to filter the values based on if condition 
result = lambda dictionary,val_check:(key for key,val in dictionary.items() \
                                      if val>val_check and key>val_check)

print("\n")
print("Example 18 Output :: ")

# Define a dictionary
dictionary = {3:9,5:25,8:64,10:100,15:150,20:200,25:200}
# Generate values from the generator expression . This call results in generator object..result(dictionary=dictionary,val_check=10)
generate_data(result(dictionary=dictionary,val_check=10))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 19
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Use lambda with reduce and dictionary.

'''
    In the example below we are calculating the sum of all key,value pairs of a dictionary
    using reduce.
    Example :
        {3:9,5:25,8:64,10:100,15:150,20:200,25:200}

   The following lambda will result in output as 834 ...

        3+9+5+25+8+64+10+100+15+150+20+200+25+200 = 834

    func_reduce_lambda = lambda x,y:sum(x) \
       if x.__class__ == ().__class__ else x+sum(y)

    result = functools.reduce(func_reduce, dictionary.items())
    print(result)


'''
def func_reduce(x,y):
  '''
    This function takes 2 args namely x,y
    It denotes the key:value pair of the dictionary.
    When reduce function is applied, key:value pairs are
    processed in an order...
    Example:
      dictionary = {3:9,5:25,8:64,10:100,15:150,20:200,25:200}
      reduce function takes 2 args at once..
      In the first iteration we will get..
      (3,9),(5,25) which becomes as 3+9+5+25 = 42
      In the first iteration both x,y are in tuple format..

      In the second iteration on-wards x will be an int..

      That's why we have this condition to check if x is tuple or int..

       * sum(x) if x.__class__ == ().__class__ else x

      42, (8,64) -> 42 is the result from Step 1 above..
      Here 42 is an int... and in this step the result will be
      42 + 8 + 64 = 114
      Likewise all records are processed..

  '''
  x_add = sum(x) if x.__class__ == ().__class__ else x
  return x_add+sum(y)

# Define an iterable..
dictionary = {3:9,5:25,8:64,10:100,15:150,20:200,25:200}

# Without Lambda 
result = functools.reduce(func_reduce, dictionary.items())
print("\n")
print("Example 19 Output :: ")
print(result)

# With Lambda 
func_reduce_lambda = lambda x,y:sum(x) \
   if x.__class__ == ().__class__ else x+sum(y)

result = functools.reduce(func_reduce, dictionary.items())
print("\n")
print(result)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 20
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Use lambda with reduce and strings.

# Define a string..
test_string = "Hello World!1985!"

print("\n")
print("Example 20 Output :: ")

# Lambda to check if a variable of type string..
print((lambda x:x.__class__==str)(test_string))
# Output will be True since test_string is a string...

'''
lambda with reduce -
 Check for str types in a var,concat and return...
 The below lambda iterates on string Hello World!1985! and checks if each char is of type str..
 if x.__class__==str else "NULL" All the chars are of type str..
 Hence the final output is : Hello World!1985!
'''
print(functools.reduce(lambda x,y:x+y \
if x.__class__==str else "NULL",test_string))

'''
  Check if there are no spaces in the string.
  If any space found , change it as NULL. Output of below statement will be : NULLWorld!1985!
  Since the string is "Hello World!1985!" After Hello we have a " " space...

  In the lambda we have a condition as ;
    if not y.strip() == '' else "NULL"
  So while iterating the string since it finds an empty space... if changes the string as "NULL"
  Then it iterates the remaining part of the string World!1985! and adds NULL to World!1985!

  Hence the final answer is NULLWorld!1985!
'''
print(functools.reduce(lambda x,y:x+y \
if not y.strip() == '' else "NULL",test_string))

print("\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 21
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Use lambda with list comprehension and files.
'''
    Read a file and check for occurrence of patterns in files.
    Read line by line and filter the records that has the pattern.
'''

# Write a python function to read the file using ContextManager.

def file_read(file_path):
    '''
        Read file and return contents as a list.
        :param file_path: Full Path of the file.
        :return : File Contents
    '''
    with open(file_path,'r') as reader:
        return reader.readlines()


# Define the path of the file to be read.
file_path = '../classes/README.txt'
# Get file contents
file_contents = file_read(file_path)
# Define a Pattern to Search
pattern_to_search = "__init__"


print("\n")
print("Example 21 Output :: ")

# Filter and print all lines in the file that has __init__ using list comprehension
print([data.lstrip().rstrip() for data in file_contents if data.__contains__(pattern_to_search)])

print("\n")

# Filter and print all lines in the file that has __init__ using dict comprehension
print({index:data.lstrip().rstrip() for index,data in enumerate(file_contents) \
      if data.__contains__(pattern_to_search)})
print("\n")

# Do above tasks using lambda
# lambda with dict comprehension for filtering records in file.

func_lambda = lambda records,pattern:\
             {index:data.lstrip().rstrip() \
                for index,data in enumerate(file_contents) \
                if data.__contains__(pattern)}

print(func_lambda(records=file_contents, pattern=pattern_to_search))     

print("\n")

# lambda with list comprehension for filtering records in file.           

func_lambda = lambda records,pattern:\
             [data.lstrip().rstrip() \
                for index,data in enumerate(file_contents) \
                if data.__contains__(pattern)]

print(func_lambda(records=file_contents, pattern=pattern_to_search))     

print("\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 