#Assigning Functions to Variables
def plus_one(number):
    """
    @Func :- It will perform addition one to number
    @Param1 :- number is a value which is type is integer
    @return :- It will return the addition of (1+number)
    """
    return number + 1

add_one = plus_one
print add_one(10)

#Defining Functions Inside other Functions
def plus_one(number):
    """
    @Func :- It will manage add_one() function
    @Param1 :- number is a value which is type is integer
    @return :- It will return the result given by add_one() function
    """
    def add_one(number):
        """
        @Func :- It will perform addition one to number
        @Param1 :- number is a value which is type is integer
        @return :- It will return the final result of main function
        """
        return number + 1
    result = add_one(number)
    return result
print plus_one(4)

#Passing Functions as Arguments to other Functions
def plus_one(number):
    """
    @Func :- It will perform addition one to number
    @Param1 :- number is a value which is type is integer
    @return :- It will return the addition of (1+number)
    """
    return number + 1

def function_call(function):
    """
    @Func :- It will accept another function as argument and manage it
    @Param1 :- function is the name of function and it's type is function
    @return :- It will return result of another function
    """
    number_to_add = 6
    return function(number_to_add)

print function_call(plus_one)

#Functions Returning other Functions

def hello_function():
    """
    @Func :- It will manage say_hi() function
    @return :- It will return result of it's inner function
    """
    def say_hi():
        """
        @Func :- It will return value
        @return :- It will return result
        """
        return "Hi"
    return say_hi

hello = hello_function()
print hello()
