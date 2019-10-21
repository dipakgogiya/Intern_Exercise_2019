
def decorator_function(any_function):
    """
    @Func :- It will manage the func() and add() function
    @Param1 :- any_function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def wrapper_function(*args,**kwargs):
        """
        @Func :- It will manage the func() and add() function
        @Param1 :- *args is the non-keyworded, variable-length argument list
        @Param2 :- **kwargs is the keyworded, variable-length argument list 
        @return :-  It will return the original function and akso return wrapper function
        """
        print "This is awsome function:"
        # any_function(*args,**kwargs)  :- For only func(a)
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def func(a):
    """
    @Func :- it will print the simple string
    """
    print("this is function with argument {}".format(a))
    
func(7)

@decorator_function
def add(a,b):
    """
    @Func :- It will calculate the square of the given list element
    @Param1 :- a is the second argument and it's type is integer
    @Param2 :- b is the second argument and it's type is integer
    @return :- It will return sum of two integers value
    """
    return a + b

print add(2,3)

