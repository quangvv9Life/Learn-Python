# If we want to pass keyword arguement in a function or method, we use 
# an arguement called **kwargs which allows us to pass the variable length
# of keyword arguements to the function
# We can us double asterisk ** before the parameter name to denote this type
# of arguement
# The arguements are passed as a dictionary and these arguments make a dictionary
# inside function with name same as the parameter excluding double asterisk **

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
