count = 0
while count < 5 :
    count += 1
    print("Iteration no  %i"%(count))
print("End of while loop")
var = '0'
while var.isnumeric() == True:
    var = input('enter a number..')
    if var.isnumeric() == True:
        print("Your input:",var)
print("End of while loop")
## while else
count = 0
while count < 5:
    count += 1
    print("Iteration no %i"%(count))
else :
    print("While loop over, Now in else block")
print("End of while loop")
# the infinite loop
var = 1
while var == 1:
    num = int(input('enter a number:'))
    print("Your input:",num)
print("Goodbye")
