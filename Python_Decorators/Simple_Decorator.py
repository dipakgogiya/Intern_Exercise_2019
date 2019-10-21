#Decorators - Enhance the functionality of other function
#@ use for decorators

def decorator_function(any_function):
    """
    @Func :- It will manage the func1() and func2() function
    @Param1 :- any_function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def wrapper_function():
        """
        @Func :- It will manage the func1() and func2() function
        @Param1 :- *args is the non-keyworded, variable-length argument list
        @Param2 :- **kwargs is the keyworded, variable-length argument list 
        @return :-  It will return the original function and akso return wrapper function
        """
        print "This is awesome function:"
        any_function()
    return wrapper_function
 
#this is awesome function
@decorator_function   #This is shortcut
def func1():
    """
    @Func :- it will print the simple string
    """
    print "This is function1:"
func1()
#this is awesome function
@decorator_function   #This is Shortcut    
def func2():
    """
    @Func :- it will print the simple string
    """
    print "This is function2:"
func2()

# var = decorator_function(func1)
# var() 
# var1 = decorator_function(func2)
# var1() 