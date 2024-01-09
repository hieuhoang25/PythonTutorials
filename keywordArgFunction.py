def printinfo(name, age):
    "This prints a passed infor into this functions."
    print("Name: ", name)
    print("Age: ", age)

# call  by positional arguments
printinfo("Hieu", 24)
# call by keyword arguments
printinfo(name="Hieu", age=24)

printinfo("Hieu", age=24)
#printinfo(name="Hieu", 24) #Positional argument cannot appear after keyword argumentsPylance
