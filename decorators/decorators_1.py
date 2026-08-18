def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper

def printHello():
    print("Hello")

result = decorator(printHello)
# print(f"result : {result}")
result()
# print(f"result : {result}")


# def execute(operation):
#     operation()

# def printHelloWorld():
#     print("Hello World!")
#     print("Bye World")

# execute(printHelloWorld)




