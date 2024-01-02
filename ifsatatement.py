distcount = 0
amount = 1200

if amount > 1000:
    distcount = amount * 10 //100

print("amount: " , amount - distcount)

################################################################
# if else basic
age = 25

print("age: " , age)

if age >= 18 :
    age + 1
    print("age: " , age)
    print("eligible to vote")
else:
    print(" not eligible to vote")

################################################################
# elif statement long
if (amount > 1000) :
    distcount = amount * 20 / 100
else :
    if  amount > 5000 :
       distcount = amount * 10/100
    else :
        if amount > 5000:
            distcount = amount * 5 / 100
        else :
            distcount = 0

################################################################
# elif statement short
if (amount > 1000) :
    distcount = amount * 20 / 100
elif  amount > 5000 :
       distcount = amount * 10/100
elif amount > 5000:
        distcount = amount * 5 / 100
else :  distcount = 0
            