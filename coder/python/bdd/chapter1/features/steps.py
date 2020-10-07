'''
    Write Classes & Methods to implement the Features and Scenarios given as part of the Feature File
'''

from behave import given, when, then

class Behave:
	
	@given('we have behave installed')
	def step_impl(context):
	    print("Hello World - we have behave installed")

	@when('we implement a test')
	def step_impl(context):
	    assert True is not False

	@then('behave will test it for us!')
	def step_impl(context):
	    assert context.failed is False