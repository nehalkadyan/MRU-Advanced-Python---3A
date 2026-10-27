# Higher Order Functions:

# A function that takes another function as argument
# or returns a new function is called as Higher Order Function

# Example Code:

# Function to make the input string capital

def make_letters_capital(text):
    return text.upper()

def process(func, text):
    return func(text)

print(process(make_letters_capital, "hello"))