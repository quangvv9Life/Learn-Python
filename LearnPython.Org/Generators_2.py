# Write a generator function which returns the Fibonacci series. 
# They are calculated using the following formula: The first two numbers
#  of the series is always equal to 1, and each consecutive number returned
#  is the sum of the last two numbers.
#  Hint: Can you use only two variables in the generator function? 
# Remember that assignments can be done simultaneously. 
# The code will simultaneously switch the values of a and b.

# a = 1 
# b = 2
# a, b = b, a
# print(a + b)

# def Fib(i):
#     # for i in range(6):
#         a = i
#         b = i + 1
#         a, b = b, a 
#         yield (a,b)

# # for i in Fib(1):
# print(Fib(1))
    
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

import types
if type(fib()) == types.GeneratorType:
    print("Good, the fib function is a gen")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break


