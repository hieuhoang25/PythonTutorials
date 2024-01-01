print("Hello i am hieu \" \t tab \n hello \a")
#Format 
name = "Hieu"
age = 22
print("Hello I am %s " %(name), end=" \n ")
print("Hello I am %s " %(age), end=" \n ")
print("Hello I am %s, I am %i years old" %(name,age))
full = "Hello I am %s, I am %i years old" %(name,age)
print(full)

fullName = "Hoang Van Hieu"
# get a element
print(fullName[2]) # 1
print(fullName[-2])
# get string from 
print(fullName[2:5]) # 1 -> 4
# get
print(fullName[2:]) # 2 -> length -1
# get 
print(fullName[:5]) # 0 -> 4

# check length
my_string = "  Hello, world!  "
print(len(my_string))
# remove space
print(my_string.strip())
# upper case
print(my_string.upper())
# lower case
print(my_string.lower())
new_string = "Hello, world"
# replace
print(new_string.replace("world", "Hieu"))
# split
print(new_string.split(', '))

my_string = "Hello, World!"
print(my_string.startswith('Hello'))  # Output: True
print(my_string.endswith('World!'))    # Output: True
print('Hello' in my_string)  
print(my_string.find('World!'))