# Functions as Objects/ First class functions

# In Python we can use functions in the following ways
# 1) Functions can be passed as argument into other functions
# 2 ) Functions can be returned from other functions
# 3) Functions can be stored into a variable
# 4 ) Functions can be stored in a list, dictionary, etc

# Passing functions as argument

# def greet():
#     return "Welcome!"

# def greet_with_name(func, name):
#     return func() + " " + name

# print(greet_with_name(greet, "John Doe"))

#  Returning functions from other functions

# outer function
# def outer():
#     # inner function
#     def inner():
#         return "Hello from Inner Function!"

#     return inner

# # storing the result of outer into test
# test = outer()
# print(test())

# storing function as a variable 

# def addTwo(n1, n2):
#     return n1 + n2

# # storing function addTwo in a variable
# sumOfTwo = addTwo

# # calling the variable , since sumOfTwo points to addTwo() in memory
# print(sumOfTwo(10, 10))


# Storing functions in list, dictrionary.

# creating two functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

# storing these two functions in a dictionary
operations = {
    # key : value
    "sum" : add,
    "difference" : subtract
}

print(operations["sum"](2,2))
print(operations["difference"](100, 10))

# # storing these functions in a list
# operations = [add, subtract]
# # index.       0.     1

# print(operations[0](2, 2))
# print(operations[1](100, 90))
