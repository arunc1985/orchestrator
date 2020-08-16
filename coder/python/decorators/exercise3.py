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


# This class will serve as a decorator, it takes a function and it's arguments as inputs and returns result
# This class is for decorator without arguments

class DecoratorWithoutArguments:

	# Define the Constructor
	def __init__(self,function):
		'''
			:param function: Function to be decorated
		'''
		# Create an instance variable function
		self.function = function

	# Define method to execute the function(self.function)
	def __call__(self,*args,**kwargs):
		'''
			args,kwargs are arguments of function(self.function)
			It's executed as self.function(*args,**kwargs)
			It means the function will get executed with all of its arguments.
			You can do any pre-step before executing a function and
			post-steps after executing the function
		'''
		try:
			# Execute the function
			result = self.function(*args,**kwargs)
			# Return the result of the function
			return result
		except Exception as error:
			raise error



# This class will serve as a decorator, it takes a function and it's arguments as inputs and returns result
# This class is for decorator with arguments

class DecoratorWithArguments:

	# Define the Constructor
	def __init__(self,*deco_args,**deco_kwargs):
		'''
			:param function: Function to be decorated
		'''
		# Create an instance variable
		self.deco_args = deco_args
		self.deco_kwargs = deco_kwargs

	# Define method to execute the function(self.function)
	def __call__(self,function):
		'''
			args,kwargs are arguments of function(self.function)

			deco_args,deco_kwargs are arguments the decorator DecoratorWithArguments

			It's executed as self.function(*args,**kwargs)
			It means the function will get executed with all of its arguments.
			You can do any pre-step before executing a function and
			post-steps after executing the function
		'''
		# Refers to the function to which decorator is applied and its arguments.
		def wrapped_func_and_its_arguments(*args,**kwargs): 
			try:
				# Execute the function
				result = function(*args,**kwargs)
				# Return the result of the function
				return result
			except Exception as error:
				raise error
		return wrapped_func_and_its_arguments

# Test the decorator - class DecoratorWithoutArguments
@DecoratorWithoutArguments # This decorator is not having arguments
def test_decorator_exec(x,y,*args,**kwargs):
    maparray = []
    for i in args:
        maparray.append(i)
    maparray.extend([x,y])
    return maparray

# Test the decorator - class DecoratorWithArguments
@DecoratorWithArguments(True,False) # This decorator is having arguments
def test_decorator_exec_with_arguments(x,y,*args,**kwargs):
    maparray = []
    for i in args:
        maparray.append(i)
    maparray.extend([x,y])
    return maparray



# Execute
if __name__ == "__main__":
    result = test_decorator_exec_with_arguments(100,200,10,20,30,40,50,60,70,80,90,300,name='Arun',profession='Programmer')
    print(result)
