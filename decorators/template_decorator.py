# Decorator is a function that takes in function as an argument
# and returns a new function with a modified result
# It does not modify the original function
def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper

@decorator
def printHello():
    print("Hello")

printHello()