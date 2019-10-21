#Python Decorator
def uppercase_decorator(function):
    """
    @Func :- It will manage the any function
    @Param1 :- function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def wrapper():
	"""
        @Func :- It will manage the any function
        @return :- It will return the wrapper function to original function
        """
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    """
    @Func :- It simple return the string
    @Return :- it will return the any type of value 
    """
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print decorate()

#Using @ Symbol
@uppercase_decorator
def say_hi():
    """
    @Func :- It simple return the string
    @Return :- it will return the any type of value 
    """
    return 'hello there this is again called'

print say_hi()

#Applying Multiple Decorators to a Single Function
def split_string(function):
    """
    @Func :- It will manage the func1() and func2() function
    @Param1 :- any_function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def wrapper():
	"""
        @Func :- It will manage the any function
        @return :- It will return the wrapper function to original function
        """
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string  #it call first one
@uppercase_decorator  #it call second one
def say_hi():
    """
    @Func :- It simple return the string
    @Return :- it will return the any type of value 
    """
    return 'hello there it'
print say_hi()

#Accepting Arguments in Decorator Functions

def decorator_with_arguments(function):
    """
    @Func :- It will manage the any function
    @Param1 :- any_function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def wrapper_accepting_arguments(arg1, arg2):
	"""
        @Func :- It will manage the any function
	@Param1 :- arg1 is the first argument of wrapper function and it's type is string
	@Param2 :- arg2 is the second argument of wrapper function and it's type is string
        @return :- It will return the wrapper function to original function
        """
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    """
    @Func :- It will manage the any function
    @Param1 :- city_one is the first argumen and it's type is string
    @Param2 :- city_two is the second argument and it's type is string
    """
    print("Cities I love are {0} and {1}".format(city_one, city_two))
    
cities("Rajkot", "Ahmedabad")

#Defining General Purpose Decorators

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    """
    @Func :- It will manage the any function
    @Param1 :- any_function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    """
    @Func :- It will simple print string
    """
    print("No arguments here.")

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    """
    @Func :- It will simple print int values
    @Param1 :- a is the first parameter and it's type is integer
    @Param2 :- b is the second parameter and it's type is integer
    @Param3 :- c is the third parameter and it's type is integer

    """
    print(a, b, c)

function_with_arguments(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    """
    @Func :- It simple return the string 
    """
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")

