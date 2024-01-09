def greetings():
    "This is docstring of greetings function"
    print("Hello, world!")
    return
greetings()

# Calling a function in python
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return
printme("Hello, world yOU ARE HERRE!")
# Pass by reference vs value
def testfunction(arg):
    print("Id inside the function: ", id(arg))
var = "Hello"
testfunction(var)
# Function return value
def add(x,y):
    return x + y
 
print(add(10,20))

