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

# Lambda function that taken an argument and return the same argument - no other action.
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
