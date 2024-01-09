# An argument prefixed with a single asterisk * for arvitary positional parameters
# sum of numbers
def add(*args):
    s = 0
    for x in args:
        s+=x
    return s
result = add(10,20,30,40)
print(result)
# The args variable prefixed with "*" stores all the values passed to it. Here args becomes a tuple. We can run a loop, over its items to add the numbers
def add(init, *args):
    s = init # 1
    for x in args: # 10,20,30,40
        s+=x
    return s
result = add(1, 10,20,30,40)
print(result)

# An argument prefixed with a two asterisk ** for arvitary positional parameters
def addr(**kwargs):
    for k,v in kwargs.items():
        print("{} : {} ".format(k,v))
addr(Name = "John", City = "Mubai")
# addr("John", "Mubai") # addr() takes 0 positional arguments but 2 were given
def percent(math, sci, **aptional):
    print("math: ", math)
    print("sci: ", sci)
    s = math +sci
    for k,v in aptional.items():
        print("{} {}".format(k,v))
        s = s +v
    return s / (len(aptional)+2)
result = percent(70,75, Eng=70, Math =50)
