import time
def decorator_time_it(any_function):
    """
    @Func :- It will manage the calc_square and calc_cube function
    @Param1 :- any_function is the function name which is accept another function as it's argument and it's type is function
    @return :- It will return the wrapper function to original function
    """
    def wraper_function(*args,**kwargs):
        """
        @Func :- It will manage the calc_square and calc_cube function
        @Param1 :- *args is the non-keyworded, variable-length argument list
        @Param2 :- **kwargs is the keyworded, variable-length argument list 
        @return :-  It will return the result and original function and akso return wrapper function
        """
        start = time.time()
        result = any_function(*args,**kwargs)
        end =  time.time()
        print(any_function.__name__ + " took " + str((end-start)*1000) + " mil sec")
        return result
    return wraper_function

@decorator_time_it
def calc_square(numbers):
    """
    @Func :- It will calculate the square of the given list element
    @Param1 :- numbers is the list of numbers which is type is list
    @return :- It will return the final result in the list
    """
    result = []
    for number in numbers:
        result.append(number)
    return result

@decorator_time_it
def calc_cube(numbers):
    """
    @Func :- It will calculate the cube of the given list element
    @Param1 :- numbers is the list of numbers which is type is list
    @return :- It will return the final result in the list
    """
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
# for i in range(0,len(out_square)):
#     if i == 20:
#         break
#     print out_square[i]
