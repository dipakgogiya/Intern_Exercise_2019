x = lambda a : a +10
print(x(5))


#Map Function is without lambda function
def square(x):
	"""
	@Func :- It will manage the square of each element
	@Param :- x is the argument name and it's type is integer
	@Returrn :- It will return the square of each element
	"""
	return x*x
	
print map(square,range(1,6))

#Map function with lambda function
print map(lambda x:x*x,range(1,6)) #square of each element in the given range

print map(lambda x,y:x+y,range(1,6),range(1,6)) #Addition of two range lists elements

#Find even numbers without using filter()
for i in range(1,11):
	if i % 2 == 0:
		print i

#Find even numbers usig filter()
print filter(lambda x : x%2==0,range(1,11))
print reduce(lambda x,y : x*y,[1,2,3,4,5])

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)



