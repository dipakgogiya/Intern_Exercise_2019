import time

def calc_square(numbers):
    """
    @Func :- It will calculate the square of the given list element
    @Param1 :- numbers is the list of numbers which is type is list
    @return :- It will return the final result in the list
    """
    start = time.time()
    result = []
    for number in numbers:
        result.append(number)
    end = time.time()
    print("Calculate square took " + str((end-start)*1000) + " mil sec")
    return result


def calc_cube(numbers):
    """
    @Func :- It will calculate the cube of the given list element
    @Param1 :- numbers is the list of numbers which is type is list
    @return :- It will return the final result in the list
    """
    result = []
    start = time.time()
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("Calculate square took " + str((end-start)*1000) + " mil sec")
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

